# ms-game

This is a recreation of a project I found on freecodecamp by Jim. The goal was to continue to work on my Python skills.

# A Few Things To Note

I did this project on an M1 Mac Mini so there are a few things that were not supported for the mac os.


- The project originally called for using "bg = 'color'" when assigning colors to attributes. On mac os, "highlightbackground = 'color' " is more consistent and works better
- The original project called for using the ctypes library for displaying pop up messages. That does not seem to be supported, so using tkinter's "messagebox.showinfo("title", "message")" works well. Note that it takes two arguements; Title and message.
  - [Documentation](https://docs.python.org/3/library/tkinter.messagebox.html "Documentation Tkinter message prompts")


# Stack Used

- Python 3.10.0
- tkinter


