import sys
import time

import mouse
from pynput import keyboard

class ScreenlockPreventerApp:
    WAIT_TIME = 60 # Number of seconds to wait before moving the mouse
    
    def __init__(self):
        self.is_running = True
        self.is_keypressed = False
        self.start_time = 0
        self.current_time = 0
        self.current_position = 0
        self.last_position = None
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keypress)
    
    def on_keypress(self, key):
            self.is_keypressed = True
    
    def run(self):
        while self.is_running:
            self.is_keypressed = False
            self.start_time = time.time()
            self.last_position = mouse.get_position()
            self.keyboard_listener.start()
            print("Screenlock preventer started. Close this window or press [CTRL]+[C] then [Y] to stop.")
            while (self.is_running):
                try:
                    self.current_position = mouse.get_position()
                    self.current_time = time.time()
                    self.elapsed_time = self.current_time - self.start_time
                    if ((self.last_position[0] != self.current_position[0]) or (self.last_position[1] != self.current_position[1])):
                        self.last_position = self.current_position
                        self.start_time = self.current_time
                    if (self.is_keypressed):
                        self.start_time = self.current_time
                        self.is_keypressed = False
                    if (self.elapsed_time >= self.WAIT_TIME):
                        mouse.move(0, 0, duration=0.0, absolute=True)
                        mouse.click('left')
                        mouse.move(self.current_position[0], self.current_position[1], duration=0.0, absolute=True)
                        self.start_time = self.current_time
                    time.sleep(1);
                except KeyboardInterrupt:
                    print("Stopping...")
                    sys.exit()

if __name__ == "__main__":
    app = ScreenlockPreventerApp()
    app.run()