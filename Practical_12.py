
 #Define a class Employee that stores information about employees in the company. The class should contain the following:
 # (i)   data members- count (to keep a record of all the objects being created for this class) and for every employee: an employee number, Name, Dept, Basic, DA and HRA.                                  
 # (ii)  function members:
             # a.  __init__ method to initialize and/or update the members. Add statements to ensure that the program is terminated if any of Basic, DA and HRA is set to a negative value. 
             #b.  function salary, that returns salary as the sum of Basic, DA and HRA. 
             # c.  __del__ function to decrease the number of objects created for the class.
             # d.  __str __ function to display the details of an employee along with the salary of an employee in a proper format
             
             

import sys


class Employee:
  count = 0

  def __init__(self, emp_no, name, dept, basic, da, hra):
    if basic < 0 or da < 0 or hra < 0:
      print(
          "Error: Basic, DA, and HRA cannot be negative. Terminating program."
          "[cite: 1]"
      )
      sys.exit(1)
    self.emp_no = emp_no
    self.name = name
    self.dept = dept
    self.basic = basic
    self.da = da
    self.hra = hra
    Employee.count += 1

  def salary(self):
    return self.basic + self.da + self.hra

  def __del__(self):
    Employee.count -= 1

  def __str__(self):
    return (
        f"Emp No: {self.emp_no}, Name: {self.name}, Dept: {self.dept}, Salary:"
        f" {self.salary()}[cite: 1]"
    )
    
    # --- Test / Example Usage (Required to see output) ---
if __name__ == "__main__":
  # Creating valid employee objects
  emp1 = Employee(101, "Alice Smith", "HR", 45000, 4000, 2500)
  emp2 = Employee(102, "Bob Jones", "IT", 60000, 6000, 4000)

  # Printing details using __str__
  print(emp1)
  print(emp2)

  # Checking total active employee count
  print(f"Total active employees: {Employee.count}")

  # Test for negative value termination (uncomment to test):
  # emp_bad = Employee(103, "Charlie", "Sales", -1000, 2000, 1000)