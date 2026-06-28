prices = [10_000, 20, 3_000, 3, -200, 1_000]

# TODO: Print the first, third, and last item
#Approach 1: One by one
print("Current Price:", prices[0])
print("Current Price:",prices[2])
print("Current Price:", prices[-1])


#Approach 2: for loop
indices=[0,2,-1]
for index in indices:
    print("Current Price:", prices[index])
