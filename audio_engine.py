import time
import sounddevice as sd
import numpy as np

def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"Audio status warning: {status}")

    volume_norm = np.linalg.norm(indata) / np.sqrt(len(indata))
    print(f"Audio chunk received | Signal Level: {int(volume_norm)}")

def test_microphone():
    samplerate = 16000
    blocksize = 1280

    print("Opening microphone stream... Speak into your mic.")
    try:
        with sd.InputStream(samplerate=samplerate,
                            channels=1,
                            dtype='int16',
                            blocksize=blocksize,
                            callback=audio_callback):
            while True:
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nMicrophone stream closed cleanly.")

if __name__ == "__main__":
    test_microphone()