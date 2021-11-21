# Accessing elements in the list
flowers = ['daisy', 'rose', 'sunflower']
# returns first element
print(f"output: {flowers[0]}")
# returns third element from the last
print(f"output: {flowers[-3]}")

# Modifying elements in the list
flowers.append('poppy')
flowers[0] = 'lavendar'
print(flowers)
# inserting elements in the list
flowers.insert(0, 'daisy')
print(flowers)
# removing an item for the list
del flowers[1]
print(flowers)
# pop method removes last item or the list unless the position specified
flowers.pop()
print(flowers)

# sorting the list
flowers.sort()
print(flowers)

# finding length
print(f"length of the list is :{len(flowers)}")



