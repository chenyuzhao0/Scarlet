import time
from states import State
import queue
from audio_engine import start_audio_listener

def main():
    current_state = State.STANDBY
    event_queue = queue.Queue()

    stream = start_audio_listener(event_queue)
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
                print("Scarlet: I am listening to you...")
                time.sleep(2)
                current_state = State.PROCESSING

            elif current_state == State.PROCESSING:
                print("Scarlet: Processing your request...")
                time.sleep(2)
                while not event_queue.empty():
                    try:
                        event_queue.get_nowait()
                    except queue.Empty:
                        break
                current_state = State.STANDBY
                print("\nScarlet is back in STANDBY.")

            elif current_state == State.ACTION:
                print("Action...")

            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Scarlet is powering down")
    finally:
        stream.stop()
        stream.close()

if __name__ == "__main__":
    main()