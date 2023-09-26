import random
a=int(input("Enter HOw many times you want to play: "))
for i in range(0,a):
    rock="🪨"
    paper="🧻"
    scissors="✂"
    game_images=[rock,paper,scissors]
    user_choice=int(input("enter your choice:Type 0 for rock,1 for paper,2 for scissors.:"))
    


    if user_choice>2 or user_choice<0:
        print("You entered invalid number,You loose")
    else:
        print("You choose:")
        print(game_images[user_choice])
        computer_choice=random.randint(0,2)
        print("Computer choose:")
        print(game_images[computer_choice])
        if computer_choice==user_choice:
            print("Its draw")
        elif computer_choice==0 and user_choice==2:
            print("You loose")
        elif user_choice==0 and computer_choice==2:
            print("You win")
        elif computer_choice>user_choice:
            print("You loose")
        elif user_choice>computer_choice:
            print("You win")
