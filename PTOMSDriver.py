# from PTOMS import PTOMS
# from Employee import Employee
# from ptoms_GUI import ptoms_GUI

import os
from datetime import date

if __name__ == "__main__":

  # final_PTOMS = PTOMS("Company", "Accounting")

  # emp1 = Employee(1, "Ben Johnson", date(2015,3,12))
  # emp2 = Employee(2, "Mary Smith", date(2013,6,17))
  # emp3 = Employee(3, "Constance Foote", date(2018,1,3))
  # emp4 = Employee(4, "Kevin Taylor", date(2009,11,27))

  # final_PTOMS.newPtoRecord(
  #   1,
  #   25,
  #   25,
  #   emp1
  # )

  # final_PTOMS.newPtoRecord(
  #   2,
  #   29,
  #   29,
  #   emp2
  # )

  # final_PTOMS.newPtoRecord(
  #   3,
  #   26,
  #   26,
  #   emp3
  # )

  # final_PTOMS.newPtoRecord(
  #   4,
  #   27,
  #   27,
  #   emp4
  # )

  # final_PTOMS.newPtoRule(10)


  # BEGIN cycling through GUIs

  # grab the current working directory
  cwd = os.getcwd()
  print(cwd)
  # join the current directory with the user authentication gui file name
  startingGUI = os.path.join(cwd, 'user_authentication_GUI.py')

  # execute the gui python file specifically.
  os.system(f'python {startingGUI}')

  # gui 2 - ptoms_GUI.py - "main menu"
  gui2 = os.path.join(cwd, 'ptoms_GUI.py')
  os.system(f'python {gui2}')

  # gui 3 - pto_record_GUI.py
  # NOTE: where is this opened from? not from the previous ptoms_GUI.py file? change accordingly before presentation
  gui3 = os.path.join(cwd, 'pto_record_GUI.py')
  os.system(f"python {gui3}")

  # gui 4 - pto_request_GUI.py
  # unable to get this one working 11/28... not sure what it does or what it looks like

  # return to  ptoms_GUI.py (main menu)
  os.system(f"python {gui2}")

  # NOTE: PTO Calendar is not used... might want to incldue that for the demonstration!!

  # Please include placeholder data for Wednesday's demo

  # In summary, navigability and interaction between front-end and back-end need to be improved before final submission


  

  