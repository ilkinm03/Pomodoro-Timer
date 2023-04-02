from tkinter import *
from config_enums import *

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

head_label = Label(text="Timer", bg=YELLOW, fg=GREEN)
head_label.config(font=(FONT_NAME, 40, "bold"))
head_label.grid(column=1, row=0)

window.mainloop()
