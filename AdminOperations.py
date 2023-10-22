import json
import random

class AdminOperations:
    def __init__(self):
        self.data = []
        self.jsondataread()
        while True:
            choice = int(input('1) Add new food items\n2) Remove food items\n3) View list of food items\n4) Edit food items\n5) Exit\n'))
            if choice == 1:
                self.additem()
            elif choice == 2:
                self.removeitem()
            elif choice == 3:
                self.viewitem()
            elif choice == 4:
                self.edititem()
            elif choice == 5:
                self.jsondatawrite()
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def jsondataread(self):
        try:
            with open('FoodItems.json', 'r') as files:
                self.data = json.load(files)
        except FileNotFoundError:
            pass

    def jsondatawrite(self):
        with open('FoodItems.json', 'w') as files:
            json.dump(self.data, files, indent=4)

    def additem(self):
        foodid = random.randint(1, 1500)
        name = input('Enter Name of the food: ')
        quantity = input('Enter the Quantity: ')
        price = int(input('Enter the Price: '))
        discount = float(input('Enter the Discount (in %): '))
        stock = int(input('Enter the stock available: '))
        obj = {"name": name, "foodid": foodid, "quantity": quantity, "price": price, "discount": discount, "stock": stock}
        self.data.append(obj)
        print("Food item added successfully!")

    def removeitem(self):
        id=int(input("Enter food ID : "))
        for item in self.data:
            if id==item["foodid"]:
                self.data.remove(item)
                self.jsondatawrite()
                break
        else :
            print("Item not found")


    def viewitem(self):
        if not self.data:
            print("No food items available.")
        else:
            print("List of Food Items:")
            for item in self.data:
                print(f"Food ID: {item['foodid']}")
                print(f"Name: {item['name']}")
                print(f"Quantity: {item['quantity']}")
                print(f"Price: {item['price']}")
                print(f"Discount: {item['discount']}%")
                print(f"Stock: {item['stock']}")
                print("------------------------")

    def edititem(self):
        food_id_to_edit = int(input("Enter the Food ID of the item you want to edit: "))
        for item in self.data:
            if item['foodid'] == food_id_to_edit:
                print(f"Editing Food Item with Food ID: {food_id_to_edit}")
                print("------------------------")
                print(f"1. Name: {item['name']}")
                print(f"2. Quantity: {item['quantity']}")
                print(f"3. Price: {item['price']}")
                print(f"4. Discount: {item['discount']}%")
                print(f"5. Stock: {item['stock']}")
                print("------------------------")
                item["name"] = input('Enter Name of the food: ')
                item["quantity"] = input('Enter the Quantity: ')
                item["price"] = int(input('Enter the Price: '))
                item["discount"] = float(input('Enter the Discount (in %): '))
                item["stock"] = int(input('Enter the stock available: '))
                self.jsondatawrite()
                print("Food item edited successfully!")
                break
        else:
            print(f"No food item found with Food ID: {food_id_to_edit}")


# obj = AdminOperations()