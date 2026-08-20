import time
from states import State

def main():

    current_state = State.STANDBY

    try:
        while current_state != State.SHUTDOWN:
            if current_state == State.STANDBY:
                print("Wake up...")
            elif current_state == State.LISTENING:
                print("Listening...")
            elif current_state == State.PROCESSING:
                print("Processing...")
            elif current_state == State.ACTION:
                print("Action...")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Scarlet is powering down")

if __name__ == "__main__":
    main()