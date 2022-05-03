from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()
root.configure(bg = 'black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

# Frames for the game space; top, left, and center
top_frame = Frame(
  root,
  bg = 'black', 
  width = settings.WIDTH,
  height = utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
  top_frame,
  bg = 'black',
  fg = 'white',
  text = 'Minesweeper Game',
  font = ('', 48)
)

game_title.place(
  x = utils.width_prct(40), y = 0
)

left_frame = Frame(
  root,
  bg = "black",
  width = utils.width_prct(25),
  height = utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
  root,
  bg = 'black',
  width = utils.width_prct(75),
  height = utils.height_prct(75)
)

center_frame.place(
  x = utils.width_prct(25),
  y = utils.height_prct(25)
)

# Loop for getting the Minesweeper grid to populate.
for x in range(settings.GRID_SIZE):
  for y in range(settings.GRID_SIZE):
    c = Cell(x, y)
    c.create_btn_object(center_frame)
    c.cell_btn_object.grid(
      column = x, row = y
    )

#Testing to see if the list has been instantiated with our x and y attributes
#print(len(Cell.all))

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x = 0, y = 0)

Cell.randomize_mines()

#tests that we have random "mines"
# for c in Cell.all:
#   print(c.is_mine)

#Run the window
root.mainloop()

