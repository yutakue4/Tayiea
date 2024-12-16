import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os
import tempfile

def play_text():
    text = text_entry.get()
    if text.strip():
        try:
            temp_file = os.path.join(tempfile.gettempdir(), "output.mp3")

            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception as e:
                    messagebox.showerror("Error", f"Cannot delete old file: {str(e)}")
                    return
            
            tts = gTTS(text=text, lang='en')
            tts.save(temp_file)

            playsound(temp_file)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال النص أولاً!")

def clear_text():
    text_entry.delete(0, tk.END)

def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

header = tk.Label(root, text="Text to Speech", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
header.pack(pady=10)

sub_header = tk.Label(root, text="Enter your text below:", font=("Arial", 12), bg="#f0f0f0", fg="#555")
sub_header.pack()

text_entry = tk.Entry(root, width=40, font=("Arial", 14), justify="center", bd=2, relief="solid")
text_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", width=10, command=play_text)
play_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12, "bold"), bg="#2196f3", fg="white", width=10, command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=10, command=exit_program)
exit_button.grid(row=0, column=2, padx=10)

footer = tk.Label(root, text="Developed by : Ahmed Tayiea", font=("Arial", 10), bg="#f0f0f0", fg="#999")
footer.pack(side="bottom", pady=10)

root.mainloop()