import pyautogui
import time

# Define the coordinates and button types for C1 and C2
C1_coordinates = [
    (220, 160, 'left'),
    (220, 160, 'right'),
    (220, 400, 'left'),
    (570, 490, 'left')
]

C2_coordinates = [
    (220, 160, 'right'),
    (220, 363, 'left'),
    (570, 490, 'left')
]

sleep_time = 0.79

def execute_clicks(coordinates):
    for x, y, button in coordinates:
        pyautogui.click(x, y, button=button)
        time.sleep(sleep_time)

def run_iterations(c1_executions, c2_executions, iterations):
    for _ in range(iterations):
        print("Executing C1 clicks...")
        for _ in range(c1_executions):
            execute_clicks(C1_coordinates)
        
        print("Executing C2 clicks...")
        for _ in range(c2_executions):
            execute_clicks(C2_coordinates)
        
        print("One iteration finished.")

# Number of times C1 and C2 should be executed in one iteration
c1_executions = 3
c2_executions = 1

# Total number of iterations
iterations = 5


run_iterations(c1_executions, c2_executions, iterations)
