from tkinter import *
from config_enums import *

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

window.mainloop()
