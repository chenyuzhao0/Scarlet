import time
from states import State
import queue
from audio_engine import start_audio_listener, record_speech, is_silent

def main():
    current_state = State.STANDBY
    event_queue = queue.Queue()
    recorded_audio = None

    stream = start_audio_listener(event_queue, model_name="alexa")
    print("--- Scarlet Voice Assistant ---")
    print("Status: STANDBY (Speak into your mic to activate)\n")

    try:
        while current_state != State.SHUTDOWN:
            if current_state == State.STANDBY:
                try:
                    event = event_queue.get_nowait()
                    if event == "Scarlet":
                        current_state = State.LISTENING
                except queue.Empty:
                    pass

            elif current_state == State.LISTENING:
                print("[Scarlet] I am listening to you...")
                audio_buffer = record_speech(duration=3)
                if is_silent(audio_buffer):
                    print("No speech detected. Returning to STANDBY.")
                    current_state = State.STANDBY
                    print("\nSTANDBY (Ready)\n")
                else:
                    print("[Scarlet] Audio captured successfully")
                    recorded_audio = audio_buffer
                    current_state = State.PROCESSING

            elif current_state == State.PROCESSING:
                print("Scarlet: Processing your request...")
                time.sleep(1.5)

                while not event_queue.empty():
                    try:
                        event_queue.get_nowait()
                    except queue.Empty:
                        break

                current_state = State.STANDBY
                print("\nSTANDBY (Ready)\n")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Scarlet is powering down")
    finally:
        stream.stop()
        stream.close()

if __name__ == "__main__":
    main()