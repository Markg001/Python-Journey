try:
    name= input("Enter Your Name:  ")
    year_born= input("Enter Your Birth Date: ")
    age= 2025 - int(year_born)
    print(f'You are {name} and your age is {age}.')
except Exception as e:
    print(e)

# Unpacking and Packing Tuples

lst =[2, 7]
numbers = range(*lst)
print(numbers)

rnd = ["Canada", "Brazil", "Japan", "Germany", "Kenya", "Australia", "India", "Argentina", "Sweden", "South Korea"]
Can, Br, *rest = rnd
print(Can, Br, *rest)

#UNPACKING Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) 

# Packing Arguments 
def sum_all(*args):
    s=0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6))

# Packing Dictionary 
def sum_dict(**args):
    for key in args:
        print("{key} = {args[key]}")
    return key
print(sum_dict(name="Mark", Country="Kenya", City="Nairobi", age="388"))
# Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

#zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

# exercise

#names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
#  Unpack the first five countries and store them in a variable nordic_countries, 
# store Estonia and Russia in es, and ru respectively.

names =  ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordiac_countries, es,ru =names
print("Nordic Countries:", nordiac_countries)
print("Estonia",es)
print("Russia", ru)