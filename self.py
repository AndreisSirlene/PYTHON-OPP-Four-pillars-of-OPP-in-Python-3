class Employee:
    def employeeDetails(self): 
        self.name = 'Paul'

    @staticmethod
    def welcomeMessage():  # when you do not pass a paremeter, the static methods can to action
        print('Welcome to our Organization!')


employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()
 