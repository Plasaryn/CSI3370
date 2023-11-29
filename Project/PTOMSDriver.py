# from PTOMS import PTOMS
# from Employee import Employee
# from ptoms_GUI import ptoms_GUI

import os
from datetime import date

if __name__ == "__main__":

  # grab the current working directory
  test = os.getcwd()
  # join the current directory with the user authentication gui file name
  startingGUI = os.path.join(test, 'user_authentication_GUI.py')

  # execute the gui python file specifically.
  os.system(f'python {startingGUI}')
  # notice that the second window will not open until the prior window has closed. At the end of each event (button click), use exit() to close the current
  # window
  os.system(f'python {startingGUI}')

  