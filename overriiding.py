class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)


class Trainee(Employee):   # Using the inheritance class 'Employee'
    def setNumberOfWorkingHours(self):  # here you redefine the method of your basic class with your derivative class, means you are overriding
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()  ##make use the super function where the control is send back to your base class (Employee)



#Main Program
employee = Employee()
employee.setNumberOfWorkingHours()
print('Number of working hours of employee: ',end=' ')
employee.displayNumberOfWorkingHours()   
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print('Number of working hours of employee: ',end='')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print('Number of working hours trainee after reset: ',end='')
trainee.displayNumberOfWorkingHours()