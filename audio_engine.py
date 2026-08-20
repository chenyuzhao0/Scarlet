import time
import sounddevice as sd
import numpy as np

def start_audio_listener(event_queue):
    def audio_callback(indata, frames, time_info, status):
        volume_norm = np.linalg.norm(indata) / np.sqrt(len(indata))

        if volume_norm > 30:
            print(f"\n[Audio Engine] Voice detected! (Level: {int(volume_norm)})")
            event_queue.put("Scarlet")

    stream = sd.InputStream(
        samplerate=16000,
        channels=1,
        dtype='int16',
        blocksize=1280,
        callback=audio_callback
    )
    stream.start()
    return stream