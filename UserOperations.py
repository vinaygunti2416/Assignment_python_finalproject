import json


class UserOperations:
    def __init__(self,name):
        self.name=name
        self.data=[]
        self.load_food_items()
        while True:
            choice = int(input("1) Place New Order\n2) Order History\n3) Update Profile\n4) Exit\n"))
            if choice == 1:
                self.placeOrder()
            elif choice == 2:
                self.orderHistory()
            elif choice == 3:
                self.updateProfile()
            elif choice == 4:
                exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
    def load_food_items(self):
            with open(r'E:\EdyodaPython\__20__final_project.py\FoodItems.json', 'r') as file:
                self.data= json.load(file)
    def write_food_items(self,data):
        with open(r'E:\EdyodaPython\__20__final_project.py\orderHistory.json','w') as addfile:
            json.dump(data,addfile,indent=4)
    def placeOrder(self):
       
       print("Place New Order")
       print("Available Food Items:")
       i=1
       for  item in self.data:
            print(f"{i}) {item['name']} ({item['quantity']}) [INR {item['price']}]")
            i+=1

       self.selected_items = []
       
           
       while True:
            try:
                choice = int(input("Select a food item (enter its number, or 0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.data):
                    self.selected_items.append(self.data[choice - 1])
                else:
                    print("Invalid choice. Please select a valid item.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

       if not self.selected_items:
            print("No items selected. Order canceled.")
       else:
            print("Selected Items:")
            total_cost = 0
            discount=0
            for item in self.selected_items:
                print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")
                total_cost += (item['price']-(item['discount']*item['price'])/100)
                discount+=item['price']
            discount-=total_cost
            print(f"Total Cost: INR {total_cost}")
            print(f'Discount :{discount}')
            odata={'name':self.name,'history':self.selected_items}
            with open(r'E:\EdyodaPython\__20__final_project.py\orderHistory.json','r') as file:
                ndata=json.load(file)
            
            ndata.append(odata)
            # print("odata:", odata)
            # print("data:", data)
            

            self.write_food_items(ndata)
            print("Order placed successfully!")


    def orderHistory(self):
        print("Viewing order history\n")
        order_history=[]
        with open(r'E:\EdyodaPython\__20__final_project.py\orderHistory.json','r') as file:
            data=json.load(file)
            
        for obj in data:
                if self.name == obj['name']:
                    order_history.append(obj['history'])
        if not order_history:
            print("No order history found.")
        else:
            for i in order_history:
                for order in i:
                    print(f"{order['name']} ({order['quantity']}) [INR {order['price']}]")
                print()


    def updateProfile(self):
        print("Updating user profile")
        with open(r'E:\EdyodaPython\__20__final_project.py\details.json', 'r') as file:
                credentials = json.load(file)
                
        for credit in credentials:
            if credit['name']==self.name:
                credit['name']=(input("Enter name :"))
                credit['phoneNumber']=int(input("Enter phoneNumber :"))
                credit['email']=(input("Enter email :"))
                credit['address']=(input("Enter address :"))
                credit['password']=(input("Enter password :"))
                
                with open(r'E:\EdyodaPython\__20__final_project.py\details.json','w') as w:
                    json.dump(credentials,w,indent=4)
                break
        else:
            print("No Profile found!!")


if __name__ == "__main__":
    user_operations = UserOperations("venkat")