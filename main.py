import tkinter as tk
from styles import center, Colors, Sizes
import pages


window = tk.Tk()
window.title('English Test')
window.iconbitmap("media/icon.ico")
window.geometry(f'{Sizes.window_WIDTH}x{Sizes.window_HEIGHT}')
window.resizable(False, False)

pages.main_frame(window)