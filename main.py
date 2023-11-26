from tkinter import *
import time
# TODO: Show total time that doesn't include breaks, as well as history from past times
# TODO: Create 3 tab bars, one for settings one for total time etc.
# TODO: Add background color option and shadow option as well
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_running = False

# Breaking down a problem into smaller bits

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer_running
    reps = 0
    timer_running = False

    # Reset every widget to start
    canvas.itemconfig(timer_text, text=f"25:00")
    modeL.config(text="Timer", fg=GREEN)
    tickL["text"] = ""
    startB["state"] = "active"

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer_running
    timer_running = True
    startB.config(state="disabled")
    reps += 1
    if (reps % 8) == 0:
        count_down(LONG_BREAK_MIN, 60)
        # test function
        # count_down(0, 5)

        modeL.config(text="Break", fg=RED)
    elif (reps % 2) == 1:
        count_down(WORK_MIN, 60)
         #test function
        #count_down(0, 5)

        modeL.config(text="Work", fg=PINK)
    else:
        count_down(SHORT_BREAK_MIN, 60)
        #test function
        #count_down(0, 5)

        modeL.config(text="Break", fg=GREEN)

    tick = ""
    if reps > 1:
        for i in range(1, reps, 2):
            tick += "✔"
        tickL.config(text=tick)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, second):
    global reps
    global timer_running
    if count >= 0 and timer_running:
        if count >= 9:
            if second == 60:
                canvas.itemconfig(timer_text, text=f"{count}:00")
                second = 0
            else:
                if second >= 9:
                    canvas.itemconfig(timer_text, text=f"{count}:{second}")
                else:
                    canvas.itemconfig(timer_text, text=f"{count}:0{second}")
        else:
            if second == 60:
                canvas.itemconfig(timer_text, text=f"0{count}:00")
                second = 0
            else:
                if second >= 9:
                    canvas.itemconfig(timer_text, text=f"0{count}:{second}")
                else:
                    canvas.itemconfig(timer_text, text=f"0{count}:0{second}")

        if second == 0 and count == 0:
            window.after(1000, count_down, count, second - 1)
        else:
            if second == 0:
                second = 60
                window.after(1000, count_down, count - 1, second - 1)
            else:
                window.after(1000, count_down, count, second - 1)
        if second == -1:
            start_timer()
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)
            # note -1 won't be shown on the screen as the start_timer will immediately be executed once second == -1
            # without this line of code we won't see 00:00, before the next timer starts
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# learn about windows tkinter

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

resetB = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
resetB.grid(row=3, column=3)

startB = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
startB.grid(row=3, column=1)

tickL = Label(text="", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
tickL.grid(row=4, column=2)

modeL = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
modeL.grid(row=1, column=2)


window.mainloop()
