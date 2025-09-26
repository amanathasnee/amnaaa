# lst=["apple","banana","orange","pineapple"]
# for i in lst:
#     print(i)
# for i ,item in enumerate(lst,start=1):
#     print(i,item)
# lst1=[{"name": "apple", "quantity": 10, "price": 1.5},
#     {"name": "banana", "quantity": 20, "price": 0.5},
#     {"name": "orange", "quantity": 15, "price": 0.8},
#     {"name": "pineapple", "quantity": 5, "price": 3.0}]
# for i,item in enumerate(lst1):
#     print(str(i) + ". " + item['name'] + " - Quantity: " + str(item['quantity']) + ", Price: $" + str(item['price']))


# lst=["apple","banana","orange","pineapple"]
# fruits=[]
# for fruit in lst:
#     # fruits=[]
#     print("Enter details for :",fruit)
#     quantity = int(input("Quantity: "))
#     price = float(input("Price per unit: "))

#     fruit_info = {"name": fruit,"quantity": quantity,"price": price}
#     fruits.append(fruit_info)

# print("\nFinal list :")
# for item in fruits:
#     print(item)

# fruits=[]
# n=int(input("how many fruits u need to add: "))
# for i in range(n):
#     print("Enter details for :",i+1)
#     name = input("Name: ")
#     quantity = int(input("Quantity: "))
#     price = float(input("Price per unit: "))

#     fruit_info = {"name": name,"quantity": quantity,"price": price}
#     fruits.append(fruit_info)

# print("\nFinal list :")
# # for item in fruits:
# print(fruits)

fruits=[]
n=int(input("how many fruits u need to add: "))
for i in range(n):
    print("Enter details for :",i+1)
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    discount = float(input("Discount percentage (0 if none): "))
    discounted_price = price*(1-discount/100)

    fruit_info = {"name": name,"quantity": quantity,"price": price,"discount":discount,"discounted_price":discounted_price}
    fruits.append(fruit_info)

print("\nFinal list :")
print(fruits)
