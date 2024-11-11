import mouse
import time
from pynput import keyboard

wait_time = 60 # Number of seconds to wait before moving the mouse

start_time = time.time()
last_position = mouse.get_position()
ver = "1.1"
rel = "11-11-2024"
keypressed = False

def on_keypress(key):
    global keypressed
    keypressed = True

keyboard_listener = keyboard.Listener(on_press=on_keypress)
keyboard_listener.start()
print("Screenlock preventer started. Close this window or press [CTRL]+[C] (Y) to stop.")

while (True):
    
    current_position = mouse.get_position()
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if ((last_position[0] != current_position[0]) | (last_position[1] != current_position[1])):
        last_position = current_position
        start_time = current_time

    if (keypressed):
        start_time = current_time
        keypressed = False
    
    if (elapsed_time >= wait_time):
        mouse.move(0, 0, absolute=True, duration=0.0)
        mouse.click('left')
        mouse.move(current_position[0], current_position[1], absolute=True, duration=0.0)
        start_time = current_time