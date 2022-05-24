# def square(num):
#     sq=num**2
#     def cube():
#         new_num=sq*num
#         print(new_num)
#     return cube

# var=square(2)
# print(var)
# var()

#DECORATORS
#======================================================================================
from functools import wraps
import time

# def calculate_time(any_fun):
#     @wraps(any_fun)
#     def wrapper(*args,**kwargs):
#         t1=time.time()
#         new_value= any_fun(*args,**kwargs)
#         t2=time.time()
#         print(t2-t1)
#         return new_value
#     return wrapper    

# @calculate_time
# def func(t):
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     print("MY name is nimra")
#     return [t**2 for i in range(1,t+1)]
    

# print(func(10))    

#==================================================================================================

# def only_int(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         data_types=[]
#         for arg in args:
#             data_types.append(type(arg)==int)
#         if all(data_types):
#             print(func(*args,**kwargs))
            
#         else:
#             print("invalid")
          

#     return wrapper

# @only_int
# def total(*args):
#     total1=0
#     for i in args:
#         total1 +=i
#     return total1

# print(total(1,2,3,4))

#===============================================================================
# def only_int(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         data=[]
#         if all(type(arg)==int  for arg in args):
#             print(func(*args,**kwargs))
#     return wrapper

# @only_int
# def total(*args):
#     total1=0
#     for i in args:
#         total1 +=i
#     return total1

# print(total(1,2,3,4))

#=========================================================
# def only_datatypes(datatype):
#     def decocartor(function):
#         @wraps(function)
#         def wrapper(*args,**kwargs):
#             if all(type(arg)== datatype for arg in args):
#                 print(function(*args,**kwargs))
#         return wrapper
#     return decocartor

# @only_datatypes(str)   
# def string_join(*args):
#     string =''
#     for i in args:
#         string +=i
#     return string
# string_join('nimra','riaz') 


