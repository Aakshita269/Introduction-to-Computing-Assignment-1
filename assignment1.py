#QUES 1:TO FIND AVERAGE OF THREE NUMBERS ENTERED BY THE USER.

print("\n \nAVERAGE CALCULATOR\n \n")

#TAKING THE INPUT OF NUMBERS FROM THE USER.
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

#TAKING THE AVERAGE OF THE NUMBERS INPUT BY THE USER.
avg=((num1+num2+num3)/3)

#PRINTING OUT THE AVERAGE OF THE NUMBERS ENTERED.
print(int(avg))




#QUES 2:TO COMPUTE A PERSON'S INCOME TAX.

print("\n \nINCOME TAX CALCULATOR\n \n")

#TAKING THE INPUT OF GROSS INCOME AND NUMBER OF DEPENDENTS FROM THE USER.
gross_inc=int(input("Enter your Gross Income in $(rounded off to the nearest integer):"))
dep=int(input("Enter the number of dependents(Enter 0 if none):"))

#CALCULATING TAXABLE INCOME AND TOTAL TAX.
tax_inc=gross_inc-10000-(3000*dep)
tax=tax_inc*(20/100)

#PRINTING OUT THE TOTAL CALCULATED INCOME TAX.
print("Your total income tax calculated is:",tax,"$")




#QUES 3:TO STORE DIFFERENT DATA TYPE VALUES INTO A LIST

print("\n \nSTUDENTS DETAILS LIST GENERATOR\n \n")

#TAKING THE INPUT OF STUDENTS DETAILS FROM THE USER
sid=int(input("Enter your SID:"))
name=str(input("Enter your Name:"))
gender=str(input("Enter your Gender(F(female),M(male),U(unknon):"))
course=str(input("Enter your Course Name:"))
CGPA=float(input("Enter your CGPA:"))

#PUTTING THE VALUES ENTERED BY THE USER IN A LIST
Student=[sid,name,gender,course,CGPA]

#PRINTING OUT THE LIST
print(Student)



#QUES 4:TO ENTER MARKS OF 5 STUDENTS INTO A LIST

print("\n \nENTERING MARKS OF DIFFERENT STUDENTS AND SORTING THEM\n \n")

#TAKING INPUT OF MARKS FROM 5 STUDENTS.
std_1=int(input("Enter Student 1 marks:"))
std_2=int(input("Enter Student 2 marks:"))
std_3=int(input("Enter Student 3 marks:"))
std_4=int(input("Enter Student 4 marks:"))
std_5=int(input("Enter Student 5 marks:"))

#MAKING A LIST OF THE MARKS ENTERED
marks=[std_1,std_2,std_3,std_4,std_5]

#PRINTING IT OUT IN A SORTED MANNER
marks.sort()
print(marks)





#QUES 5: A)TO PRINT A SPECIFIED LIST AFTER REMOVING 4TH ELEMENT

print("\n \nREMOVING AN ELEMENT FROM A SPECIFIED LIST\n \n")

#PRINTING THE ORIGINAL LIST
color = ['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
print("The original list:" )
print(color)
          
#DELETING ELEMENT NUMBER 4 FROM THE LIST AND PRINTING THE LIST
del color[3]
print("After removing the 4th element:")
print(color)


          
#QUES 5: B)TO REMOVE 'BLACK' AND 'PINK' AND REPLACE THEM WITH 'PURPLE'

print("\n \nREPLACING CERTAIN COLOURS IN THE LIST WITH ANOTHER COLOUR\n \n")

#PRINTING THE ORIGINAL LIST
color:['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
print("The original list:")
print(color)

#REPLACING ELEMENTS WITH ANOTHER ELEMENT AND PRINTING IT
color[3:5]=['PURPLE']
print("After replacing 'BLACK' and 'PINK' with 'PURPLE':")
print(color)
