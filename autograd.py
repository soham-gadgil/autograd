class Val:
    def __init__(self, x):
        self.x = x
        self.grad = 1
        self.left = None
        self.right = None
        self.op = "val"

    def __add__(self, other):
        new_val = Val(self.x + other.x)
        new_val.left = self 
        new_val.right = other
        new_val.op = "+"
        return new_val
    
    def __mul__(self, other):
        new_val = Val(self.x * other.x)
        new_val.left = self 
        new_val.right = other
        new_val.op = "*"
        return new_val
    
    def __truediv__(self, other):
        new_val = Val(self.x / other.x)
        new_val.left = self 
        new_val.right = other
        new_val.op = "/"
        return new_val
    
    def __sub__(self, other):
        new_val = Val(self.x - other.x)
        new_val.left = self 
        new_val.right = other
        new_val.op = "-"
        return new_val        

    def __str__(self):
        return str(self.x)

    def backwards(self):
        if self.op == "+":
            self.left.grad = self.left.grad
            self.right.grad = self.right.grad
        elif self.op == "-":
            self.left.grad = self.left.grad
            self.right.grad = self.right.grad
        elif self.op == "*":
            self.left.grad = self.grad * self.right.x
            self.right.grad = self.grad * self.left.x
        elif self.op == "/":
            self.left.grad = self.grad * (1 / self.right.x)
            self.right.grad = self.grad * (1 / self.left.x)
        
        if self.op != "val":
            self.left.backwards()
            self.right.backwards()


p1 = Val(2)
p2 = Val(4)
p3 = Val(2)

y = p1 + (p2 * p3)
y.backwards()
print(p1.grad)
print(p2.grad)
print(p3.grad)