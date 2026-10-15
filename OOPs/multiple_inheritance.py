# 15 10 2026

class Livingthing:
    def __init__(self):
        print("Livingthing initialized")

class Swimmer(Livingthing):
    def __init__(self):
        super().__init__()
        print("Swimmer initialized")   

class Flyer(Livingthing):
    def __init__(self):
        super().__init__()
        print("Flyer initialized")

class Duck(Swimmer, Flyer):
    def __init__(self):
        super().__init__()
        print("Duck initialized")

d = Duck()
# output order matches MRO: Duck -> Swimmer -> Flyer -> Livingthing
# MRO: Method Resolution Order

# Livingthing Initialized
# Flyer Initialized
# Swimmer Initialized
# Duck Initialized