# class Laptop:
#     def __init__(self,brand_name,price):
#         self.brand_name=brand_name
#         self.price=price


# l = Laptop('Dell',78)
# print(f'{l.brand_name}\n {l.price}') 

# class Laptop:
#     def __init__(self,brandname,price,model):
#         self.brandname=brandname
#         self.price=price         # these are instance variables
#         self.model=model
#         self.name=brandname+''+model

#     def new_price(self,discount):
#         self.discount=discount
#         diss=(self.price*discount)/100 
#         return self.price-diss 

# l = Laptop('Dell',2000,'m56')
# print(l.name) 
# print(l.new_price(20))   




# class Person:
#     def __init__(self,first_name,last_name,age,gender):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age= age
#         self.gender=gender

#     def user_data(self):
#         print(f'First Name :{self.first_name}\n Last Name :{self.last_name}\n Age :{self.age}\nGender :{self.gender}')    

# nam,l,a,g = input("enter your First name, enter your last name,enter age, enter gender").split(" ")
# p = Person(nam,l,a,g)
# p.user_data()     


# class Person:
#     count_instance=0
    
#     def __init__(self):
        
#           Person.count_instance += 1

# p=Person()
# p1=Person()
# p2=Person()
# print(Person.count_instance)

        

# p = Person()
# p1= Person()    


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def detail(self):
        return f'Name is {self.name}and your age is {self.age}'

class Newa(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender
p = Person('nimra',22)
n= Newa('nimra',22,'female')
print(n.detail())