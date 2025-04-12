import random

random_range = random.random()  # Random float between 0 and 1.
print(random_range)


random_number = random.randint(1, 10)  # Random integer between 1 and 10 
print(random_number)


random_number = random.uniform(1, 10)  # Random float between 1 and 10
print(random_number)


my_list = [10, 20, 30, 40, 50]
random_item = random.choice(my_list)  # Randomly selects an item from a sequence.
print(random_item)
