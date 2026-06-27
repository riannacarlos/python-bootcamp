num1 = int(input("Give number:"))
num2 = int(input("Give number:"))
num3 = int(input("Give number:"))


def product(x, y, z=1):
    total = x * y * z
    return total


result=product(num1, num2, num3)
result1=product(num1,num2)
print(result,result1)

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 10
