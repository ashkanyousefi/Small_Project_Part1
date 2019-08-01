names =  input('Enter the names: ').title().split(',')
assignments =  input('Enter assignment: ').split(',') 
grades =  input('Enter the grades for the students: ').split(',')

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

