
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

# Sarah Castorena
# 2028049
amount = 0
count = 1
previous = None
while count <= 10:
   num = int(input('Enter a number: '))
    
   if (num % 2 == 0) and (previous is not None) and (previous % 2 == 0):

     amount = amount + 1   
   previous = num 
   count = count + 1   
print(amount)

