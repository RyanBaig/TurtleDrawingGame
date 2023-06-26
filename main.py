import threading
import turtle
import tkinter as tk
import keyboard

# Create a turtle instance
t = turtle.Turtle()

# Create a turtle screen and set the window size
screen = turtle.Screen()
screen.setup(width=1366, height=768)


# Define the turtle's movement functions
def move_forward():
    t.forward(100)


def move_backward():
    t.backward(100)


def turn_left():
    t.left(45)


def turn_right():
    t.right(45)


def restart():
    t.home()
    t.clear()


def exit_game():
    screen.bye()
    control_window.destroy()


# Thread target function to capture keyboard events
def keyboard_listener():
    keyboard.on_press_key("w", lambda _: move_forward())
    keyboard.on_press_key("s", lambda _: move_backward())
    keyboard.on_press_key("a", lambda _: turn_left())
    keyboard.on_press_key("d", lambda _: turn_right())
    keyboard.on_press_key("r", lambda _: restart())
    keyboard.on_press_key("x", lambda _: exit_game())


# Create and start the keyboard listener thread
keyboard_thread = threading.Thread(target=keyboard_listener)
keyboard_thread.start()

# Create the tkinter window
control_window = tk.Tk()

# Exit button
exit_button = tk.Button(control_window, text="OK", command=control_window.destroy)
control_window.title("Controls")
exit_button.pack()

# Label
exit_button_text = tk.Label(control_window, text="WASD to move around, R to restart and X to exit")
exit_button_text.pack()

# Run the turtle graphics
turtle.mainloop()

# Quit the tkinter window
control_window.quit()
