from multipledispatch import dispatch
#Coffee Machine with Overloaded brew() Method
class CoffeeMachine:
    """A smart coffee machine that brews differently based on inputs."""
    
    @dispatch()
    def brew(self):
        print("Brewing a standard black coffee ")

    @dispatch(str)
    def brew(self, strength):
        print(f"Brewing a {strength} coffee ")

    @dispatch(int)
    def brew(self, sugar):
        print(f"Brewing coffee with {sugar} sugar cubes ")

    @dispatch(bool)
    def brew(self, add_milk):
        if add_milk:
            print("Brewing coffee with milk ")
        else:
            print("Brewing black coffee (no milk) ")

machine = CoffeeMachine()

machine.brew()           # Standard black coffee
machine.brew("strong")   # Strong coffee
machine.brew(2)          # Coffee with 2 sugars
machine.brew(True)       # Coffee with milk