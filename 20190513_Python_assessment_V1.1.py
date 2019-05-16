#20190513_Python_Assessment_V1.1
#Environment_Quiz_Game
#By Blake

#Variables
user_name=""
highScore=0



#Lists
question_promts=["Question One: (Input the letter of the answer you think is correct)\nWhat colour bin do you put general waste in?\n(A) Red\n(B) Yellow\n(C) Blue\nYour Answer: ",
                 "Question Two:\nWhen using bags while shopping, what is more eco-friendly?\n(A) Plastic\n(B) Paper\n(C) Doesn't Matter\n(D) Using your own  reusable ones\nYour Answer: ",
                 "Question Three:\nWhat uses less water?\n(A) Washing the dishes by hand\n(B) Using the dishwasher\nYour Answer: "
]

class Question:
        def __init__(self, promt, answer):
                self.promt = promt
                self.answer = answer

questions = [
        Question(question_promts[0], "A"),
        Question(question_promts[1], "D"),
        Question(question_promts[2], "B")
]

                
#Setting up the functions
#fuction to collect the users name
def intro(user_name):
        print("Welcome to the Environment Quiz Game")
        user_name=input("What is your name?\n")
        mainMenu()
        
def mainMenu():
        userChoice=""
        print("Welcome to the environment quiz",user_name)
        print("""Main menu:
        (S) Start the quiz 
        (H) View the HighScore
        (X) Quit the game""")
        userChoice=input()
        if userChoice.upper() == "S": #.upper means it doesn't matter if you put an upper or lower case letter
                startQuiz(questions)#Starts the quiz
        elif userChoice.upper() == "H":
                print("The HighScore is:",highScore)
                mainMenu()
        elif userChoice.upper() == "X":
                exit()
        else:
                print("Please use a valid input") 
                mainMenu()

#Function to start the quiz.
def startQuiz(questions):
        score=0
        for question in questions:
                answer = input(question.promt).upper()
                if answer == question.answer:
                        score +=1
                        print("Thats correct\n")
                else:
                        print("Thats incorrect, the right answer is ",(question.answer),"\n")
        print("You got ",str(score),"/",str(len(questions)),"Correct")
        global highScore
        if score>highScore:
                highScore=0
                highScore+=score
        mainMenu()


intro(user_name)