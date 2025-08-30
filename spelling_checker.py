from tkinter import *
from textblob import TextBlob
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

# Main window setup
root = Tk()
root.title("Spelling Checker")
root.geometry("700x450")
root.config(bg="#121212")

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def check_spelling():
    text = enter_text.get().strip()
    if text:
        try:
            corrected_text = str(TextBlob(text).correct())
            spell.config(text="✅ Corrected: " + corrected_text)
            speak_text("Corrected sentence is: " + corrected_text)
        except:
            spell.config(text="❌ Could not process the input.")
            speak_text("Could not process the input.")
    else:
        spell.config(text="⚠️ Please enter some text.")
        speak_text("Please enter some text.")

# Heading
heading = Label(
    root,
    text="📝 Spelling Checker",
    font=("Trebuchet MS", 32, "bold"),
    bg="#121212", fg="#00adb5"
)
heading.pack(pady=(30, 10))

# Entry box
enter_text = Entry(
    root,
    justify="center",
    width=40,
    font=("Poppins", 20),
    bg="#1e1e1e", fg="#ffffff",
    insertbackground="white",
    borderwidth=2, relief="solid"
)
enter_text.pack(pady=10)
enter_text.focus()

# Check button
button = Button(
    root,
    text="Check Spelling",
    font=("Arial", 18, "bold"),
    fg="white", bg="#ff5722",
    activebackground="#e64a19",
    padx=20, pady=5,
    command=check_spelling
)
button.pack(pady=20)

# Output label
spell = Label(
    root,
    text="",
    font=("Poppins", 20),
    bg="#121212", fg="#00ffae"
)
spell.pack(pady=20)

# Run the app
root.mainloop()
