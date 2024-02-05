import tkinter as tk

# Function to read the contents of welcome.txt
def read_welcome_text():
    try:
        with open("welcome.txt", "r") as file:
            welcome_text = file.read()
    except FileNotFoundError:
        welcome_text = "Welcome to our application!\n\n(No welcome message found)"
    return welcome_text

# Function to read the contents of username.txt
def read_username():
    try:
        with open("username.txt", "r") as file:
            username = file.read()
    except FileNotFoundError:
        username = "Guest"
    return username

# Function to read the contents of outro.txt
def read_outro_text():
    try:
        with open("outro.txt", "r") as file:
            outro_text = file.read()
    except FileNotFoundError:
        outro_text = "Thanks for using our application!"
    return outro_text

# Function to update the label text with typing animation
def update_text_with_typing(label, text):
    if text:
        label.config(text=label["text"] + text[0])
        label.after(1, update_text_with_typing, label, text[1:])
    else:
        # After typing animation is done, schedule username update after 5 seconds
        label.after(2000, update_username, label)

# Function to update the label text with username
def update_username(label):
    username = read_username()
    label.config(text=username, fg="cyan")
    # After username update, schedule outro text update after 5 seconds
    label.after(2000, update_outro_text, label)

# Function to update the label text with outro text
def update_outro_text(label):
    outro_text = read_outro_text()
    label.config(text=outro_text, fg="cyan")
    # After outro text update, schedule window closing after 5 seconds
    label.after(2000, root.destroy)

# Create the main application window
root = tk.Tk()

# Set the window title
root.attributes("-fullscreen", True)
root.title("Startup Message")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the background color to black
root.configure(bg="black")

# Read welcome message from welcome.txt
welcome_message = read_welcome_text()

# Create a label to display the welcome message
label = tk.Label(root, text="", fg="cyan", bg="black", font=("Courier", 10))
label.pack(expand=True)

# Update the label text with typing animation
update_text_with_typing(label, welcome_message)

# Run the Tkinter event loop
root.mainloop()
