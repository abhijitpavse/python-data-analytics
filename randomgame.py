# # # 23 09 2026

# # import random

# # print(num=random.randint(1,10)) # unlike range function here '10' there is no upper limit all are exclusive


# # import random as r
# # print(num=r.randint(1,10))


# # Question: 2 Player Game
# # player 1                                        player 2
# # 1.roll
# # 2.hold
# # roll->dice=randint
# # 1-> score reset and pass the dice to player 2
# # 2,3,4,5,6 add the value to player1 score
# # hold -> score will remain same as it is but pass the dice to player 2
                                              
#                                                 # 1.roll
#                                                 # 2.hold
#                                                 # And same rule as player1

# # will run until oneoff players score 20

# import random
# player1_score=0
# player2_score=0
# player1_turn=True
# while player1_score<20 and player2_score<20:
#     dice=random.randint(1,6)
#     if player1_turn:
#         print("Player 1 turn")
#         if dice==1:
#             player1_score=0
#             player1_turn=False
#         else:
#             player1_score+=dice
#             player1_turn=False
#     else:
#         print("Player 2 turn")
#         if dice==1:
#             player2_score=0
#             player1_turn=True
#         else:
#             player2_score+=dice
#             player1_turn=True

# print("Player 1 score:",player1_score)
# print("Player 2 score:",player2_score)





import random

player1_score = 0
player2_score = 0
player1_turn = True

while player1_score < 20 and player2_score < 20:

    if player1_turn:
        print("\nPlayer 1 Turn")
        print("Player 1 Score:", player1_score)

        choice = int(input("Enter 1 to Roll or 2 to Hold: "))

        if choice == 1:
            dice = random.randint(1, 6)
            print("Player 1 rolled:", dice)

            if dice == 1:
                player1_score = 0
                print("Oops! Player 1 rolled 1. Score reset to 0.")
                player1_turn = False

            else:
                player1_score += dice
                print("Player 1 Score:", player1_score)

                if player1_score >= 20:
                    break

        #         # Player 1 gets another chance to roll/hold
        #         player1_turn = True

        # elif choice == 2:
        #     print("Player 1 chose to Hold.")
        #     player1_turn = False

        # else:
        #     print("Invalid choice! Please enter 1 or 2.")

    else:
        print("\nPlayer 2 Turn")
        print("Player 2 Score:", player2_score)

        choice = int(input("Enter 1 to Roll or 2 to Hold: "))

        if choice == 1:
            dice = random.randint(1, 6)
            print("Player 2 rolled:", dice)

            if dice == 1:
                player2_score = 0
                print("Oops! Player 2 rolled 1. Score reset to 0.")
                player1_turn = True

            else:
                player2_score += dice
                print("Player 2 Score:", player2_score)

                if player2_score >= 20:
                    break

        #         # Player 2 gets another chance to roll/hold
        #         player1_turn = False

        # elif choice == 2:
        #     print("Player 2 chose to Hold.")
        #     player1_turn = True

        # else:
        #     print("Invalid choice! Please enter 1 or 2.")


print("\n========== GAME OVER ==========")
print("Player 1 Score:", player1_score)
print("Player 2 Score:", player2_score)

if player1_score >= 20:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")