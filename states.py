import enum

class State(enum.Enum):
    STANDBY = 1
    LISTENING = 2
    PROCESSING = 3
    ACTION = 4
    SHUTDOWN = 5