class User:
    def __init__(self,id,username):
        self.id = id
        self.username = username

user_1 = User("001","hirak")
user_2 = User("002","supriya")
print(user_1.username)
print(user_2.username)