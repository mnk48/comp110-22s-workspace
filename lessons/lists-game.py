"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()  # Setting up an empty list (constructor)
rolls.append(randint(1, 6))  # Method call 
rolls.append(randint(1, 6))
rolls.append(randint(1, 6))
print(rolls)

# Access an individual item 
print(rolls[0])
print(rolls[1])

#  Access the length of a list (mumber of items)
print(len(rolls))

#  Access the last item of a list
last_index: int = len(rolls) - 1
print(rolls[last_index])

