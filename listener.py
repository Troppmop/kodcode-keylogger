from pynput import keyboard

class IKeyLogger:
    def start_logging(self):
        pass

    def stop_logging(self):
        pass

    def get_logged_keys(self) -> list[str]:
        pass

"""
stores keystrokes in memory (not in a file yet). to be used later by the other programs
"""
