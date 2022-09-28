#Creating attributes with the help of constructors
#constructors allows us to specify what should happen when our object is being constructed
#It is also called initializing an object

class User:
    
    def __init__(self,user_id,username): #initializing attributed
        #init function is going to be called every time when a new object is created
        self.id = user_id
        self.username=username
        self.followers = 0
        
user_1=User("001","Hajra")
print(user_1.id)

user_2=User("002","Hadia")
print(user_2.id)
print(user_2.username)
print(user_2.followers)
