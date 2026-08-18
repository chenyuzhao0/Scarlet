import time

def main():
    is_running = True
    event = "running"

    try:
        while is_running:
            if event == "Scarlet, sleep":
                is_running = False
            print(event)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Scarlet is powering down")

if __name__ == "__main__":
    main()