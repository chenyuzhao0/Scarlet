import time
from states import State
import queue

def main():

    current_state = State.STANDBY
    event_queue = queue.Queue()

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
                print("Listening...")
            elif current_state == State.PROCESSING:
                print("Processing...")
            elif current_state == State.ACTION:
                print("Action...")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Scarlet is powering down")

if __name__ == "__main__":
    main()