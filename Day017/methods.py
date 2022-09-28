#Attributes are things that object has
#methods are the things that object does
#We can also create methods

class User:
    
    def __init__(self,user_id,username): #initializing attributed
        #init function is going to be called every time when a new object is created
        self.id = user_id
        self.username=username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User("001","Hajra")

user_2=User("002","Hadia")
user_1.follow(user_2)

print(user_2.followers)
print(user_2.following)
print(user_2.username)

print(user_1.followers)
print(user_1.following)
print(user_1.username) 