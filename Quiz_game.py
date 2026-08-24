score = 0
playing = True

while playing:

    print("\n========KNOWLEDGE QUIZ=========")
    
    answer = input("Q1. A guy emotionally atatched to other guy what him called?\n"
                        "a. good boy\n"
                        "b. bad boy\n"
                        "c. gay\n"
                        "your answer is: ")
    
    if answer == "c":
        print(" correct")
        score = score + 1
    else:
        print("incorrect, you need some knowledge")
        
        answer = input("Q2. If you see a stick who's width is 5cm so, what you do with te stick?\n"
                        "a. sit on the stick\n"
                        "b. break the stick\n"
                        "c. through the stick\n"
                        "your answer is: ")

    if answer == "a":
        print("correct")
        score = score + 1
    
    else:
        print("incorrect, you need some knowledge")

        answer = input("Q3. If you see your friend who's more pretty then girl's so, what you do wit her?\n"
                        "a. beat him\n"
                        "b. sex with him\n"
                        "c. only imagining him\n"
                        "your answer is: ")
    
    if answer == "b":
        print("correct,you're such a my son")
        score = score + 1
    
    else:
        print("incorrect, you need some knowledge")

        print("your score is:", score,"/3")

        playing = False

print("Thank you for playing ;)")