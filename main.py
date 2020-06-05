import math

# yes = True
# while (yes):
# 	print("s")
# 	print("a")
# 	continue
# 	print("d")
# 	print("f")
# 	print("g")
	


# break ends 1 loop

# while yes:
# 	for i in range(10):
# 		print(i, "x")
# 		break
# 	break
	
list_int = [1,2,3,44,5,6,7]
y_2 = "helloworld"

# for num in y_2:
# 	print(num)

# for i in range(2, 12, 4):
# 	print(i)

# for i, x in enumerate(y_2):
# 	print(i, x)

grid = [[1,2,3],[4,5,6],[7,8,9]]

# for i in grid:
# 	for j in i:
# 		print(j, end=" ")
# 	print("")


def maxOf(x, y):
	if x > y:
		return x
	elif x < y:
		return y
	else:
		print(x,"=",y)
		return ""

"""
print board
take turn
check win


"""

x = input("Type your name:")
print(int(x))