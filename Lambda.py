# def divide (x, y):
#     return (x/y)
# print(divide(10,2))

# divide = lambda x,y: x/y
# print(divide(10,2))
#
#
# print(lambda x : x * x * x,5)

# ----------------------------------Map------------------------


# def cube(x):
#     return (x*x*x)
#
#
l = [2, 5, 3, 7, 34, 665, 672, 1213, 546543, 6, 6, 474454]
# newl = []
# # for items in l:
# #     newl.append(cube(l))
# newl = list(map(lambda x:x*x*x,l))
#
# print(newl)

#----------------------Filter------------------
# def filter_function(f):
#     return (f>4)
#
# newl = list(filter(filter_function,l))
# print(newl)


# -------------------------------Reduce_____________________________________
# from functools import reduce
# sum=(reduce(lambda x,y:x+y,l))
# print(sum)

# --------------