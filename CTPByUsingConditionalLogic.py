class Calculator:
    def add(self, *args):
        if len(args) == 2:
            print("Adding 2 numbers")
            return args[0] + args[1]
        elif len(args) == 3:
            print("Adding 3 numbers")
            return args[0] + args[1] + args[2]
        else:
            print("Unsupported number of arguments")
            return None

calc = Calculator()
print(calc.add(5, 10))          # Adding 2 numbers -> 15
print(calc.add(5, 10, 15))      # Adding 3 numbers -> 30
print(calc.add(5, 10, 15, 20))  # Unsupported number of arguments