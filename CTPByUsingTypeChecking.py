class Calculator:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b
        else:
            return "Invalid types"


calc = Calculator()
print(calc.add(5, 10))
print(calc.add("Hello", "World"))  