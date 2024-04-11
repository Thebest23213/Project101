import random

response=input("press y to roll again and n to exit(The first output is your roll): ")

while response =="y":
    no = random.randint(1,6)
    print(no)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if no == 2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[ 000 ]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 5:

        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 6:

        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
    else:
       response=input("press y to roll again and n to exit: ") 
    if response == "n":
        quit()
    
