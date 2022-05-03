from tkinter import Button, Label, messagebox
import random
import settings
import sys

class Cell:
  all = []
  cell_count = settings.CELL_COUNT
  cell_count_label_object = None
  def __init__(self, x, y, is_mine = False):
      self.is_mine = is_mine 
      self.is_opened = False
      self.is_mine_candidate = False
      self.cell_btn_object = None
      self.x = x
      self.y = y

      #Append the object to the cell.all list 
      Cell.all.append(self)

  def create_btn_object(self, location):
    btn = Button(
      location,
      width = 12,
      height = 4,
    )
    btn.bind('<Button-1>', self.left_click_actions ) # Left click convention
    btn.bind('<Button-2>', self.right_click_actions ) # Right click convention
    self.cell_btn_object = btn

  @staticmethod #We don't want this for each cell; just for use case of the class, not the instance 
  def create_cell_count_label(location):
    lbl = Label(
      location,
      bg = "black",
      fg = 'white',
      text = f"Cells Left:{Cell.cell_count}",
      width = 12,
      height = 4,
      font = {"", 30}
    )
    Cell.cell_count_label_object = lbl

  
  def left_click_actions(self, event):
    if self.is_mine:
      self.show_mine()
    else:
      if self.surrounded_cells_mines_length == 0:
        for cell_obj in self.surrounded_cells:
          cell_obj.show_cell()
      self.show_cell()
      # If mine count is equal to the cells left count, player won
      if Cell.cell_count == settings.MINES_COUNT:
        messagebox.showinfo('Game Over', 'Congratulations! You won the game!')
    
    # Cancel Left and Right click events if cell is already opened:
    self.cell_btn_object.unbind('<Button-1>')
    self.cell_btn_object.unbind('<Button-2>')

  def get_cell_by_axis(self, x,y):
    # Return a cell object based on the value of x,y
    for cell in Cell.all:
      if cell.x == x and cell.y == y:
        return cell

  @property
  def surrounded_cells(self):
    cells = [
      self.get_cell_by_axis(self.x - 1, self.y -1),
      self.get_cell_by_axis(self.x - 1, self.y),
      self.get_cell_by_axis(self.x - 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y),
      self.get_cell_by_axis(self.x + 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y + 1)
    ]
    
    # List Comprehension
    cells = [cell for cell in cells if cell is not None]
    return cells
  
  @property
  def surrounded_cells_mines_length(self):
    counter = 0
    for cell in self.surrounded_cells:
      if cell.is_mine:
        counter += 1

    return counter  
  
  def show_cell(self):
    if not self.is_opened:
      Cell.cell_count -= 1
      self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)
      # Replace the text of cell count lable with the newer count
      if Cell.cell_count_label_object:
        Cell.cell_count_label_object.configure(
          text = f"Cells Left:{Cell.cell_count}"
        )
      # If this was a mine candidate, then for safety, we should
      # configure the background color to black 
      self.cell_btn_object.configure(
        highlightbackground = "black"
      ) 
    # Mark the cell as opened(Use is as the last line of the method)
    self.is_opened = True

  def show_mine(self):
    # Logic to interrupt the game and display a message that player lost! 
    self.cell_btn_object.configure(highlightbackground ='red')
    # on mac highlightbackground seems to work more consistently
    messagebox.showinfo('Game Over', 'You Clicked a Mine')
    sys.exit()


  def right_click_actions(self, event):
    if not self.is_mine_candidate:
      self.cell_btn_object.configure(
        highlightbackground = 'orange'
      )
      self.is_mine_candidate = True
    else:
      self.cell_btn_object.configure(
        highlightbackground = 'black'
      )
      self.is_mine_candidate = False

  @staticmethod
  def randomize_mines():
    picked_cells = random.sample(
      Cell.all, settings.MINES_COUNT
    )
    for picked_cell in picked_cells:
      picked_cell.is_mine = True
    
  
  # returns formatted string that make the objects a bit cleaner
  def __repr__(self):
    return f"Cell({self.x, self.y})"