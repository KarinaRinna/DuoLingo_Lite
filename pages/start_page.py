import


def go_to_menu(frame, name_input, window):
    name = name_input.get()
    User.name = name
    frame.destroy()
    menu_frame(window=window)


def main_frame(window):
    frame = tk.Frame(window, width=Size.window_WIDTH, height=Sizes.window_HEIGHT, bg=Colors.main_color)
    frame.pack()
    tk.Label(frame, text=StartPage.hello_text, font=Font.base_font, bg=Colors.main_color, )