# def even_num(num):
#     for i in range(1,num+1):
#         if i%2==0:
#             yield i
        
        
# numbers = even_num(7)
# for nums in numbers:

#     print(nums )     


  #LIST COMPERIHENSION   

# li=[1,2,3,4,6,7,8]

# square=[i    for i in li  if i%2==0 ]
# print(square)


#========================================================================================================
#GENERATOR COMPERHENSION :

square=(i**2 for i in range(1,11))

#for generator we need to use for loop to porint

for num in square:
    print(num)