import random

r = random.randint(1,10)
print(r)

random_no_0_to_1 = random.random()
print(random_no_0_to_1)



random_float = random.uniform(1,10)
print(random_float)




random_choice = random.randint(0,1)
if random_choice == 0:
    print("Heads")
else:
    print("Tails")


