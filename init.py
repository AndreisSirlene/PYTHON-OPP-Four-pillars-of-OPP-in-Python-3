class Employee: 

    def __init__(self, name): # Here the init method take a parameter and assigned
        # the atribute with that
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)

#Create a object for this class
employee = Employee('Marcos')
employeeTwo = Employee('Lucas')
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()