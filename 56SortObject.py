from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User('Bucky', 43),
    User('Sally', 15),
    User('Sally', 5),
    User('Sally', 3),
    User('Tuna', 61),
    User('Brain', 2),
    User('Joby', 77),
    User('Amanda', 9)
]

# for user in users:
#     print(user)
#
# print('------')
# for user in sorted(users, key=attrgetter('user_id')):
#     print(user)

print('------')
for user in sorted(users, key=attrgetter('name', 'user_id')):
    print(user)