from PTOMS import PTOMS
from Employee import Employee
from ptoms_GUI import ptoms_GUI


from datetime import date

if __name__ == "__main__":
  final_PTOMS = PTOMS("Company", "Accounting")

  emp1 = Employee(1, "Ben Johnson", date(2015,3,12))
  emp2 = Employee(2, "Mary Smith", date(2013,6,17))
  emp3 = Employee(3, "Constance Foote", date(2018,1,3))
  emp4 = Employee(4, "Kevin Taylor", date(2009,11,27))

  final_PTOMS.newPtoRecord(
    1,
    25,
    25,
    emp1
  )

  final_PTOMS.newPtoRecord(
    2,
    29,
    29,
    emp2
  )

  final_PTOMS.newPtoRecord(
    3,
    26,
    26,
    emp3
  )

  final_PTOMS.newPtoRecord(
    4,
    27,
    27,
    emp4
  )

  final_PTOMS.newPtoRule(10)