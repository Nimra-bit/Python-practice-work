# print square of list 
# number =[1,2,3,4]

# def num_square(l):
#     square =[]
#     for i in l:
#         square.append(i**2)
#     return square

# print(num_square(number))

#********************************************************************************************************
#return the reverse of list

# def reverse(l):
#     reverse_list=[]
    
#     for i in range(len(l)):
#         pop_no= l.pop()
#         reverse_list.append(pop_no)
#     return reverse_list

# number= list(range(1,11))
# print(reverse(number))        
#
#[abc,xyz] ->>>> [cba , zyx]

# def reverse_string(l):
#      final_list =[]
#      for i in l:
#          final_list.append(i[::-1])
#      return final_list
# my_list=['abc','xyz']
# print(reverse_string(my_list))     

#MAKE ID LIST TO 2D LIST 
# def even_odd(l):
#     even_list=[]
#     odd_list = []
    
#     for i in l:
#         if i%2== 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     final_list=  [even_list,odd_list]
#     return final_list

# my_list=[1,2,3,4,5,6,7,8,9]
# print(even_odd(my_list))

#*********************************************************************************************************
#PRINT COMMON ELEMENTS LIST FROM TWO LISTS

# def  comon(l1,l2):
#     l3=[]
#     for i in l1:
#         if i in l2:
#             l3.append(i)
#     return l3            
# list1=[1,2,3,6,7]
# list2=[4,8,9,3,7]
# print(comon(list1,list2)) 
# **********************************************************************************************

#from typing import Type


# def finder(l):
    
#     count =0
#     for i in l:
#         if type(i)== list:
#             count+=1
        
#     return  count
# my_list = [1,2,3,[2,3,4]]
# print(finder(my_list))     



         
