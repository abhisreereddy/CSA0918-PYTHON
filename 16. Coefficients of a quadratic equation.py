import cmath
def quadratic_roots(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
roots = quadratic_roots(a, b, c)
print("Roots:")
for root in roots:
    print(root)
