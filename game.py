import random
import tkinter as tk

root = tk.Tk()
root.title("🐍 Snake Water Gun Game")
root.geometry("350x400")
root.config(bg="#1e1e2f")

youDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDict = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}

title = tk.Label(root, text="Snake 🐍 Water 💧 Gun 🔫", 
                 font=("Arial Rounded MT Bold", 18), fg="white", bg="#1e1e2f")
title.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#00ffcc", bg="#1e1e2f")
result_label.pack(pady=10)

def play(choice):
    computer = random.choice([-1, 0, 1])
    you = youDict[choice]

    if computer == you:
        result = "It's a Draw 🤝"
        color = "yellow"
    elif (computer - you == -1 or computer - you == 2):
        result = "You Lose 💀"
        color = "red"
    else:
        result = "You Win 🏆"
        color = "lime"

    result_label.config(text=f"You chose {choice}\nComputer chose {reverseDict[computer]}\n\n{result}", fg=color)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=30)

buttons = [
    ("🐍 Snake", "#4CAF50"),
    ("💧 Water", "#2196F3"),
    ("🔫 Gun", "#FF5722")
]

for text, color in buttons:
    tk.Button(frame, text=text, bg=color, fg="white", font=("Arial", 12, "bold"),
              width=12, height=2, relief="raised",
              command=lambda c=text.split()[1]: play(c)).pack(pady=5)

footer.pack(side="bottom", pady=10)

root.mainloop()

