score = 0

print("\n=====QUIZ GAME=====")

science = input("which chemical element has the highest melting point of all pure elements ?\n"
                "a. Tungsten\n"
                "b. Carbon\n"
                "c.Rhenium\n"
                "d. Osmium\n"
                "your answer is: ")

if science == "b":
    print("correct")
    score = score + 1

else:
    print("Incorrect answer")


geography = input("what is the deepest known point in the Earth's oceans?\n"
                "a. puerto rico trench\n"
                "b. challenger deep\n"
                "c. java trench\n"
                "d. mariana trench\n"
                "your answe is: ")

if geography == "b":
    print("correct")
    score = score + 1

else:
    print("Incorrect answer")


geography = input("which country has the most time zones in the world?\n"
                "a. russia\n"
                "b. us\n"
                "c. france\n"
                "d. uk\n"
                "your answer is: ")

if geography == "c":
    print("correct")
    score = score + 1 

else:
    print("incorrect answer")


print("your score is:", score,"/3")


print("QUIZ OVER._.")