items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)
print('squared(using for loop): {}'.format(squared))


squared = list(map(lambda x: x**2, items))
print('squared(using lambda, map): {}'.format(squared))


more_than_nine = list(filter(lambda x: x>9, squared))
print('more_than_nine: {}'.format(more_than_nine))

