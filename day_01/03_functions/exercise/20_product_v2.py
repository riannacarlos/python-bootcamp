num1 = int(input("Give number:"))
num2 = int(input("Give number:"))
num3 = int(input("Give number:"))


def product(x, y, z=1):
    total = x * y * z
    print(total)


product(num1, num2, num3)
product(num1,num2)

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 10
