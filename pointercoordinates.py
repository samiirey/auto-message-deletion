import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # Get the current mouse position.
        print(f'\rMouse Position: x={x} y={y}', end="")
        time.sleep(0.1)  # Short delay to avoid flooding the console with messages.
except KeyboardInterrupt:
    print("\nProgram exited.")
