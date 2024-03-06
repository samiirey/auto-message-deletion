import pyautogui

def move_cursor():
    # Get user input for X and Y coordinates
    x = input("Enter the X coordinate: ")
    y = input("Enter the Y coordinate: ")
    
    # Convert input to integers
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Please enter valid numbers for coordinates.")
        return

    # Move the cursor to the specified coordinates
    pyautogui.moveTo(x, y)

if __name__ == "__main__":
    move_cursor()
