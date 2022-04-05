# class User:
#     def __init__(self):
#         print("Hai new object")
# user1 = User()
# user1.id="1"
# user1.name="Anu"
# print(user1.id ,user1.name)
# user2 = User()
#
# user2.name="Arjun"
# user2.id="2"
# print(user2.id,user2.name)

class User:
    def __init__(self,id,name):
        self.ids=id
        self.names=name
        self.address="Asdfg"

user1=User("001","Anu")
user2=User("002","Arjun")
print(user1.ids,user1.names,user1.address)
print(user2.ids,user2.names)
print(user1.address)
print(user2.address)
user2.address="ertyi"
print(user2.address)