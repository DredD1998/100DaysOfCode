class User:
    def __init__(self,id,username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001","hirak")
user_2 = User("002","supriya")
user_1.follow(user_2)
print(f"user 1 following: {user_1.following},user 1 followers: {user_1.followers}")
print(f"user 2 following: {user_2.following},user 2 followers: {user_2.followers}")