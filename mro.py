#Method Resolution Order
class Grandparent:
    def trait(self):
        print("Kindness from Grandparent")

class Parent1(Grandparent):
    def trait(self):
        print("Creativity from Parent1")
        super().trait()  # Call next in MRO

class Parent2(Grandparent):
    def trait(self):
        print("Logic from Parent2")
        super().trait()  # Call next in MRO

class Child(Parent1, Parent2):
    def trait(self):
        print("Curiosity from Child")
        super().trait()  # Call next in MRO

# Check MRO
print(Child.__mro__)  # Output: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.Grandparent'>, <class 'object'>)

child = Child()
child.trait()