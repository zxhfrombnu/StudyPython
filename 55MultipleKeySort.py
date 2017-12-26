from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Robers'},
    {'fname': 'Tom', 'lname': 'Robers'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Robers'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bucky', 'lname': 'Dog'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('-----')
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)