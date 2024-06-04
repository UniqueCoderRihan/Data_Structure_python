
users = ["raihan","sharif","habib","Tanim","rashid","shariar"]

class raihan:
    def __init__(self,roll,age,gf):
        self.roll = roll
        self.age = age
        self.gf = gf
    def call(self):
        print(f"gf status",self.gf)

print(raihan(12,23,"nai Bhai gf").call())
users.append("NewUser")
users.pop()
users.append("Again User")
users.sort()
indexOFUser= users.index("raihan")
print(indexOFUser)
print(users)

# for i in range(len(users)):
#     print(users[i])

