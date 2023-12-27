from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import controller


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def print_display():
    entry_1.delete(0, "end")

    if controller.first_var_comp and controller.inp:
        entry_1.insert(0, f"{controller.first_var} {controller.choice} {''.join(map(str, controller.inp))}")
    elif controller.inp:
        entry_1.insert(0, ''.join(map(str, controller.inp)))
    else:
        entry_1.insert(0, str(controller.first_var) if controller.first_var is not None else '')



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Calculator")
window.geometry("393x770")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 770,
    width = 393,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    196.0,
    144.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    199.5,
    218.5,
    image=entry_image_1,
)
entry_1 = Entry(
    bd=0,
    bg="#AAAAAA",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=22.0,
    y=190.0,
    width=355.0,
    height=55.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.clear(), controller.reset(), print_display()),
    relief="flat"
)
button_1.place(
    x=24.0,
    y=297.0,
    width=75.0,
    height=75.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.toggle_sign(), print_display()),
    relief="flat"
)
button_2.place(
    x=115.0,
    y=297.0,
    width=75.0,
    height=75.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=203.0,
    y=297.0,
    width=75.0,
    height=75.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.set_choice('/'), print_display()),
    relief="flat"
)
button_4.place(
    x=294.0,
    y=297.0,
    width=75.0,
    height=75.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(1), print_display()),
    relief="flat"
)
button_5.place(
    x=24.0,
    y=388.0,
    width=75.0,
    height=75.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(2), print_display()),
    relief="flat"
)
button_6.place(
    x=115.0,
    y=388.0,
    width=75.0,
    height=75.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(3), print_display()),
    relief="flat"
)
button_7.place(
    x=203.0,
    y=388.0,
    width=75.0,
    height=75.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.set_choice('*'), print_display()),
    relief="flat"
)
button_8.place(
    x=294.0,
    y=388.0,
    width=75.0,
    height=75.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(4), print_display()),
    relief="flat"
)
button_9.place(
    x=24.0,
    y=479.0,
    width=75.0,
    height=75.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(5), print_display()),
    relief="flat"
)
button_10.place(
    x=115.0,
    y=479.0,
    width=75.0,
    height=75.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(6), print_display()),
    relief="flat"
)
button_11.place(
    x=203.0,
    y=479.0,
    width=75.0,
    height=75.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.set_choice('+'), print_display()),
    relief="flat"
)
button_12.place(
    x=294.0,
    y=479.0,
    width=75.0,
    height=75.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(7), print_display()),
    relief="flat"
)
button_13.place(
    x=24.0,
    y=570.0,
    width=75.0,
    height=75.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(8), print_display()),
    relief="flat"
)
button_14.place(
    x=115.0,
    y=570.0,
    width=75.0,
    height=75.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(9), print_display()),
    relief="flat"
)
button_15.place(
    x=203.0,
    y=570.0,
    width=75.0,
    height=75.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.set_choice('-'), print_display()),
    relief="flat"
)
button_16.place(
    x=294.0,
    y=570.0,
    width=75.0,
    height=75.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append('.'), print_display()),
    relief="flat"
)
button_17.place(
    x=203.0,
    y=661.0,
    width=75.0,
    height=75.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.calculate_result(entry_1), print_display()),
    relief="flat"
)
button_18.place(
    x=294.0,
    y=661.0,
    width=75.0,
    height=75.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (controller.inp.append(0), print_display()),
    relief="flat"
)
button_19.place(
    x=13.0,
    y=661.0,
    width=177.0,
    height=75.0
)
window.resizable(False, False)
window.mainloop()
