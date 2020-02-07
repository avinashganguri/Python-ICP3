class Employee():
    employeeCount =0
    salary =0
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family=family
        Employee.salary+=salary
        self.department=department
        Employee.employeeCount=Employee.employeeCount+1
    def printAllEmployees(self):
        print('Name: '+self.name+' Family: '+self.family+' Department: '+self.department)

    def averageSalary(self):
        self.avgSalary=Employee.salary/Employee.employeeCount
        print ('The average salary of the employees is')
        print (self.avgSalary)

class FullTimeEmployee(Employee):
    def __init__(self):
        Employee.averageSalary(self)



e1=Employee('Avinash','Ganguri',70000,'Software')
e1.printAllEmployees()

e2=Employee('Space','Impactor',77000,'IT')
e2.printAllEmployees()

f=FullTimeEmployee()