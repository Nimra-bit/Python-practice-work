#sum of n natural numbers:

# user_input= int(input("enter the number"))
# i=1
# sum =0
# while(i<= user_input):
#     sum=sum+i
#     i=i+1
# print(f"the sum of n natural number is : {sum}")    


#problem no 2

# num = input("enter more than one digit number")
# sum=0
# for i in range(0,len(num)):
#     sum= int(num[i])+sum
# print(sum)   
# 



# #PROBLEM NO 3:
# name = input("enter user name")
# temp_var=""
# i=0
# while(i<  len(name)):
#     if name[i] not in temp_var:
#         temp_var +=name[i]  #multiple char ka record rakhna hai is leye ya add karen ga
#         print(f"{name[i]}{name.count(name[i])}")
#         i +=1


# #GUESSING NUMBER GAME :
# import random
# wining_num = random.randint(1,100)
# num = int(input("enter the numb er between 1 and 100"))
# game_over = False
# count =1
# while not game_over:
#     if(num== wining_num):
        
#         print(f"you win the game !, You guess this num in {count} Times")
#         game_over=True
#     elif(num > wining_num):
#          print("Too high")
#          count +=1
#          num = int(input("enter the numb er between 1 and 100"))

#     elif(num< wining_num):
#          print("Too Low")
#          count+=1
#          num = int(input("enter the numb er between 1 and 100"))



#*********************************************************************

#3Rd argument is step argument 2 means aik num chor kr dusra print hpga like 1 3 5
# # #FOR ODD NUMBERS 
# for i in range(1,11,2):
#     print(i)

#this will print from 10,9,8
# for i in range(10,0,-1):
#     print(i)

#*********************************
#string in for loop in python can be acces in a very simple way for eg:
#we don't need to use indexing like name[i]
# name= "1253"
# sum = 0
# for i in name:
#     sum = sum+int(i)
# print(sum)


            

        



