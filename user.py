from authentication import *
from UserOperations import *
class user:
   
    def __init__(self,choice) :
        if choice==1:
            user.login(self)
        elif choice==2:
            user.register(self)
    
    def login(self):
        username=(input("Enter username :"))
        password=(input("Enter password :"))
        auth_instance = authentication()  
        flg,name = auth_instance.userlogin(username, password)
        if flg :
            # name = auth_instance.credentials[0]['name']
            UserOperations(name)
        else:
            print("Wrong password! unable to log in Try Again ")
            exit(1)
    def register(self):
        name=(input("Enter username :"))
        phoneNumber=(input("Enter phoneNumber :"))
        email=(input("Enter email :"))
        address=(input("Enter address :"))
        password=(input("Enter password :"))
        authentication().userRegister(name,phoneNumber,email,address,password)
        print("Registation Successful!\nlogin Again")
        
