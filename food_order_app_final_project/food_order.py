from food import *
from user import *

class food_order:
    global data 
    data = []
    def login(self,selection):
        admin_id = "admin@edyoda.com"
        admin_pin = "Admin1234"
        
        if selection == 1:
            print("\n-----Admin Login-----")
            username = input("\nPlease enter your username : ")
            password = input("Please enter your password : ")
            if admin_id == username and admin_pin == password:
                print("\n----Welcome Admin!----\n")
                
                while(True):
                    print("\n1.Add New Food Item \n2.Edit Food Item \n3.View Food Items List \n4.Remove Food Item \n5.Previous Page")
                    choice = int(input("Enter your choice : "))
                    food_order_obj = food_order()
                    food_order_obj.execute(choice)

            else:
                print("\nInvalid login credentials\n")

        elif selection == 2:
            while(True):
                    print("\n1.Register on application \n2.User login \n3.Previous page \n")
                    choice = int(input("Enter your choice : "))

                    if choice == 1:
                        print("\n---------------Register on the application------------------\n")
                        user_details_obj = food_order()
                        user_details_obj.details()
                        print("\nThanks for registering as new user,Please re-login \n")

                    elif choice == 2:

                        print("\n---------------User Login------------------\n")
                        old_user_email = input("\nPlease provide your email id: ")
                        old_user_password = input("Please provide your password: ")

                        for emails in self.user_list:
                            if emails.user_email == old_user_email and emails.user_password == old_user_password:
                                print("\n---Welcome User!---\n")

                                while(True):
                                    print("\n1.Place New Order \n2.Order History \n3.Update Profile \n4.View Profile \n")
                                    option = int(input("\nEnter your choice : "))
                                    user_order_obj = food_order()
                                    user_order_obj.user_option(option)
                            else:
                                print("\nInvalid credentials")
                    elif choice == 3:

                        selection = 0
                        while(selection<3):
                            print("\n----Welcome to Food Ordering App---- \n\n1.Admin login \n2.User login \n3.Exit\n")
                            selection = int(input("Enter your choice : "))
                            food_order_obj = food_order()
                            food_order_obj.login(selection)


        elif selection == 3:
            print("")

        else:
            print("\n Invalid Input \n")

# Below code represents new user registration details
    user_list = []
    
    def details(self):
            user_id = len(food_order.user_list)+1
            user_name = input("Enter your full name : ")
            user_contact = int(input("Enter your contact number without any prefix like (+91) : "))
            user_email = input("Enter your email id : ")
            user_address = input("Enter your address : ")
            user_password = input("Enter your preferred password : ")
            user_obj = user(user_id,user_name,user_contact,user_email,user_address,user_password)
            self.user_list.append(user_obj)
            


    
   # Below code describes "admin user food related functionality"
    food_list = []
    
    def execute(self,choice):
        if choice == 1:
            print("\n---------------Add Food Item------------------\n")
            food_id = len(food_order.food_list)+1
            food_name = input("Enter food item Name : ")
            food_quantity = input("Enter food item quantity along with units(gms/pieces) : ")
            food_price = input("Enter food item price (INR) : ")
            discount = float(input("Enter discount on food item (%) : "))
            stock = int(input("Enter available stock number of the food item : "))
            food_obj = food(food_id,food_name,food_quantity,food_price,discount,stock)
            self.food_list.append(food_obj)
            menu_item = food_name + "("+ food_quantity +")" + "[ INR" + food_price + "]" 
            data.append(menu_item)
            
        elif choice == 2:
            print("\n---------------Edit food Item------------------\n")
            food_id=int(input("Enter Food item id: "))

            for items in self.food_list:
                if items.food_id == food_id:
                    items.set_food_name(input("Enter food item Name: "))
                    items.set_food_quantity(input("Enter food item quantity: "))
                    items.set_food_price(float(input("Enter food itme price (INR): ")))
                    items.set_discount(float(input("Enter the discount of the food item (%): ")))
                    items.set_stock(int(input("Enter the available stock of the food item: ")))

        elif choice == 3:
            print("\n---------------Food Items List------------------\n")
            for i in range(len(self.food_list)):
                print(self.food_list[i])
                data.append(self.food_list[i])
                print("\n")          

        elif choice == 4:
            print("\n---------------Remove Food item------------------\n")
            found=False
            food_id = int(input("Enter the Food Item ID which you want to remove: "))
            for items in self.food_list:
                if items.food_id==food_id:
                    self.food_list.remove(items)
                    found=True
                    break
            if found==False:
                print("\nFood Item not found!")

        elif choice == 5:
            print("")

            selection = 0
            while(selection<3):
                print("\n----Welcome to Food Ordering App---- \n\n1.Admin login \n2.User login \n3.Exit\n")
                selection = int(input("Enter your choice : "))
                food_order_obj = food_order()
                food_order_obj.login(selection)

        else:
            print("\nInvalid Input")
            


# for user food selection options
    order_list = []
    preorder_list = []

    def user_option(self,option):
        if option == 1:
            print("---------------Place New Order------------------\n")
            print("Please find the list of Food items:\n")
            menu = []
            a = int(len(data)/2)
            b = 0
            for i in data:
                if b < a:
                    c = data[b]
                    menu.append(c)
                    b += 1
            for i in menu:
                print(i)
            x = [int(x) for x in input("\nPlease select food item:").split(",")]
            for i in x:
                self.preorder_list.append(data[i-1]) 
            print("Your Selected Items:\n",self.preorder_list)
            confirm = input("\nPlease enter 'Yes' to place order or 'No' to cancel the order:")
            if confirm == "Yes":
                print("\nHurray!\nYour Order is confirmed")
                for i in self.preorder_list:
                    self.order_list.append(i)
                self.preorder_list.clear()
            elif confirm == "No":
                print("\nYour Order has been cancelled")
                self.preorder_list.clear()

        elif option == 2:
            print("\n---------------Order History------------------\n")
            for i in range(len(self.order_list)):
                print(self.order_list[i])            

        elif option == 3:
            print("\n---------------Update Profile------------------\n")

            for profile in self.user_list:
                profile.set_user_name(input("Enter your full name: "))
                profile.set_user_contact(int(input("Enter your contact number: ")))
                profile.set_user_address(input("Enter your address: "))
                profile.set_user_password(input("Enter your password: "))

        elif option == 4:
            print("\n---------------View Profile------------------\n")
            for i in range(len(self.user_list)):
                print(self.user_list[i])
                print("\n")   

        else:
            print("Invalid Input")


# Below code represents various login options
selection = 0
while(selection<3):
    print("\n----Welcome to Food Ordering App---- \n\n1.Admin login \n2.User login \n3.Exit\n")
    selection = int(input("Enter your choice : "))
    food_order_obj = food_order()
    food_order_obj.login(selection)

