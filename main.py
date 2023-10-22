from user import user
from authentication import *
from AdminOperations import *

try:
    options=int(input("1)user\n2)admin\n3)exit\n"))
    if options==1:
        options=int(input("1)login\n2)Register\n3)exit\n"))
        if options==3:
            exit(1)
        user(options)
    elif options==2:
        password=input("Enter password :")
        flg=authentication().adminlogin(password)
        if flg:
            AdminOperations()
        else :
            print("Wrong password! unable to log in Try Again ")
            exit(1)
    else:
        exit(1)
except ValueError as e:
    print("Exception :-",e)
