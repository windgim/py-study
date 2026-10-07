import tkinter as tk
from datetime import datetime
from pathlib import Path

FILE_NAME = Path(__file__).parent / "text.txt"

root = tk.Tk()
root.title("Что мне делать, как мне жить?")
root.geometry("750x550")
root.configure(bg="black")

title = tk.Label(
    root,
    text="Мои текущие задачи",
    bg="black",
    fg="yellow",
    font=("Times New Roman", 30, "bold", "underline")
)
title.pack(pady=(35, 25))

frame = tk.Frame(root, bg="black")
frame.pack(fill="both", expand=True, padx=50)


def update():
    for widget in frame.winfo_children():
        widget.destroy()

    today = datetime.now().date()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as error:
        label = tk.Label(
            frame,
            text=f"Ошибка: {error}",
            bg="black",
            fg="red",
            font=("Arial", 15)
        )
        label.pack()
        return

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split("|", 1)

        if len(parts) != 2:
            continue

        date_text = parts[0].strip()
        task = parts[1].strip()

        try:
            task_date = datetime.strptime(
                date_text,
                "%Y-%m-%d"
            ).date()
        except ValueError:
            continue

        days = (task_date - today).days

        if days < 0:
            number = abs(days)

            if number == 1:
                word = "день"
            elif number in (2, 3, 4):
                word = "дня"
            else:
                word = "дней"

            text = f"Прошло {number} {word} от {task}"
            color = "#ff2020"

        elif days == 0:
            text = f"Прямо сейчас происходит {task}"
            color = "#ffb000"

        else:
            if days == 1:
                word = "день"
            elif days in (2, 3, 4):
                word = "дня"
            else:
                word = "дней"

            text = f"Осталось {days} {word} до {task}"
            color = "#c0c0c0"

        label = tk.Label(
            frame,
            text=text,
            bg="black",
            fg=color,
            font=("Arial", 15),
            anchor="w"
        )

        label.pack(
            fill="x",
            pady=3
        )

    root.after(60000, update)


update()

root.mainloop()
