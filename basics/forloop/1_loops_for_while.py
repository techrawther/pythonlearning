alist = [1,4,5,6]
employeelist = ['pavan', 'saravana', 'pavan']
employee_id = [1,5,10]
age = [35,34,33]

# simple
##for each_number in alist:
##    print ( each_number)

## range
##for number in range(1, 100, 10):
##    print (number)

##for id, each_employee in enumerate(employeelist):
##    print (id, each_employee)

##for each_employee,eid,each_age in zip(employeelist,employee_id,age):
##    print (each_employee,eid,each_age)

count = 0
while(count < len(employeelist)):
      print(employeelist[count])
      count = count +1

            
      
