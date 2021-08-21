import random

def stop():
    stopexe = input("Press Return to continue...")
    return;

genuser=int(input("how many seeds would you like?\n>>> "))
type(genuser)


if genuser == 0:
    print("New Random Seeds:")
    print("")
    auto_seed_generation = [random.randint(-9223372036854775807,9223372036854775807) for ran in range (0,10)]
    print(auto_seed_generation)
    stop()
else:
    user_seed_generation = [random.randint(-9223372036854775807,9223372036854775807) for spec in range (0,genuser)]
    print(user_seed_generation)
    stop()

