from tkinter import *

root = Tk()
root.geometry('1440x720')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
  root,
  bg = 'red',
  width = 1440,
  height = 180
)

root.mainloop()

