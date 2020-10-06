# Check if an employee has achieved his weekly target or not
class Employee:
    name = 'John'
    designation = 'sales executive'
    salesOfTheWeek = 6
    def hasAchievedTarget(self):        # create a method like to create a function 
        if self.salesOfTheWeek >= 5:
            print('Target has been achieved')
        else:
            print('Target has not been achieved')

# Create an object for your class
employeeOne = Employee()
employeeOne.name
'Ben'# this is the output
employeeOne.hasAchievedTarget()
'Target has been achieved'   # will be the output
employeeTwo = Employee()
employeeTwo.name
'Ben'  # this is not the right to initialize the attributes of your object, for this is use special methods

###########

numbers = [1, 2, 3]
type(numbers)
< class 'list'>
numbers.append(4) # the append method will add the number to the list
numbers[1, 2, 3, 4] #this is the out put

