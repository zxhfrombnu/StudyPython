class Parent():
    def print_last_name(self):
        print("Robers")

class Child(Parent):
    def print_first_name(self):
        print("FirstName")

    def print_last_name(self):
        print("Snitzleberg")

child = Child()
child.print_first_name()
child.print_last_name()