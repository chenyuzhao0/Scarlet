import sounddevice as sd
import numpy as np
import openwakeword.utils
from openwakeword.model import Model

def start_audio_listener(event_queue, model_name ="alexa",threshold=0.5):
    openwakeword.utils.download_models()

    oww_model = Model(wakeword_models=[model_name], inference_framework="onnx")

    def audio_callback(indata, frames, time_info, status):
        if status:
            return

        audio_chunk = np.frombuffer(indata, dtype=np.int16)
        oww_model.predict(audio_chunk)

        for model in oww_model.prediction_buffer.keys():
            scores = list(oww_model.prediction_buffer[model])
            if scores and scores[-1] > threshold:
                event_queue.put("Scarlet")
                oww_model.reset()
        
    stream = sd.InputStream(
        samplerate=16000,
        channels=1,
        dtype='int16',
        blocksize=1280,
        callback=audio_callback
    )
    stream.start()
    return stream

def record_speech(duration=3, samplerate=16000):
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels = 1,
        dtype = 'int16'
    )
    sd.wait()
    return recording.flatten()

def is_silent(audio_data, threshold=25):
    if len(audio_data) == 0:
        return True
    volume_norm = np.linalg.norm(audio_data) /np.sqrt(len(audio_data))
    return volume_norm < threshold