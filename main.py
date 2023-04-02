from tkinter import *
from config_enums import *

reps = 0
timer: str | None = None


def start_timer():
    global reps
    reps += 1
    long_break_secs = LONG_BREAK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    work_secs = WORK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_secs)
        head_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        head_label.config(text="Break", fg=PINK)
    else:
        countdown(work_secs)
        head_label.config(text="Work", fg=GREEN)


def countdown(count):
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_count, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_marks = "✔" * (reps // 2)
        check_marks_label.config(text=check_marks)


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

head_label = Label(text="Timer", bg=YELLOW, fg=GREEN)
head_label.config(font=(FONT_NAME, 40, "bold"))
head_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_marks_label = Label()
check_marks_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
check_marks_label.grid(column=1, row=3)

window.mainloop()
