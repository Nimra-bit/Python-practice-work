# #PRINT LAST CHAR OF STRING 
# def last_char(name):
#     return name[-1]
# print(last_char("nimrariazjjdhdnt ")) 
# 
# 
# ***********************************************************************************
# PRINT THE NUM IS ODD OR EVEN
# def check(num):
#     if(num%2==0):
#         print("number is even")   #yaha return "even " ese nhe likh sakte hain 
#     else:
#         return "odd"
# check(8)    
# 

#**************************************************************************************

# def even(num):
#     if num%2==0:
#         return True
#     return False    
# if even(9)== True:
#     print("even")
# print("not even")    

#*********************************************************************************************
# def greatest(num1,num2):
#     if num1> num2:
#         return "num1 is greater"
#     else:
#        return "num2 is greater" 
# a=input("enter num 1")
# b=input("enter num 2")
# print(greatest(a,b))

# def greatest(num1,num2,num3):
#     if num1> num2 and num1>num3:
#         return "num1 is greater"
#     else:
#         if num2> num1 and num2>num3:
#             return "num2 is greater"
#     return "num 3 is greater"     
# a=input("enter num 1")
# b=input("enter num 2")
# c=input("enter num 3")
# print(greatest(a,b,c))
#*****************************************************************************************************
#FUNCTION INSEIDE FUNCTION EXAMPLE 

# def greatest(num1,num2):
#     if num1> num2:
#         return num1
#     else:
#        return num2 

# def greaters(num1,num2,num3):
#     bigger = greatest(num1,num2)
#     return greatest(bigger,num3)

# print(greaters(2,4,6))  

#*********************************************************************************************
#PALINDROME:

 
# def isplanidrome(name):
    
#     reverse = name[len(name)::-1]
#     if reverse == name:
#         print("yes")
#     else:
#         print("no")
# isplanidrome("madama")            

#************************************************************************************
#FIBONACCI SERIES:

#0 1 1 2 3 5 8 13 



    




