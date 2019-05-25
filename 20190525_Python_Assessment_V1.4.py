#20190523_Python_Assessment_V1.4
#Environment_Quiz_Game
#By Blake

#Variables
user_name=""
highScore=0
high_score=""
highScoreName="Empty"

#Lists- This list is for all of the queestions that are being used in the quiz
question_promts=[
        "Question One: (Input the letter of the answer you think is correct)\nWhat colour bin do you put general waste in?\n(A) Red\n(B) Yellow\n(C) Blue\nYour Answer: ",
        "Question Two:\nWhat type of shopping bag is the most eco-friendly?\n(A) Plastic\n(B) Paper\n(C) Reusable bags\n(D) Doesn't matter \nYour Answer: ",
        "Question Three:\nWhat  uses less water and is more eco-friendly?\n(A) Washing the dishes by hand\n(B) Using plasitc disposable plates\n(C) Using the hose outside\n(D) Using the dishwasher\nYour Answer: ",
        "Question Four:\nWhat is solar power?\n(A) Energy from the moon\n(B) Energy from a solar eclipse\n(C) Energy from the sun\n(D) Power harnessed from the peak of mount everest\nYour answer: ",
        "Question Five:\nWhich of these will help to save power?\n(A) Leaving your phone on charge all night\n(B) Turning lights of in rooms that aren't being used\n(C) Throwing away your toaster\n Your answer: "
]

#The class that promts the questions
class Question:
        def __init__(self, promt, answer, answers):
                self.promt = promt
                self.answer = answer
                self.answers = answers
                
#A list that matches the questions with their answers
questions = [
        Question(question_promts[0], "A",["A","B","C"]),
        Question(question_promts[1], "C",["A","B","C","D"]),
        Question(question_promts[2], "D",["A","B","C","D"]),
        Question(question_promts[3], "C",["A","B","C","D"]),
        Question(question_promts[4], "B",["A","B","C"])
]
                
#Setting up the functions

#fuction to collect the users name
def intro():
        global user_name
        print("Welcome to the Environment Quiz Game")
        user_name=input("What is your name?\n")
        mainMenu()
        
#Sets the name of the person who got the last high score
def HighScoreName():
        global highScoreName
        f = open("HighScoreName.txt", "r")
        if f.mode == 'r':
                contents_2 =f.read()
        highScoreName = contents_2
        
#setting the high score
def highScore():
        f = open("HighScore.txt", "r")
        if f.mode == 'r':
                contents =f.read()
                global highScore
                highScore=int(contents)

#Main menu function sets the main menu
def mainMenu():
        #Setting the variables to global to ensure we can use them inside the function
        global highScore
        global user_name
        global highScoreName
        userChoice=""
        print("Welcome to the environment quiz",user_name)
        #Prints the Users options in the main menu
        print("""Main menu:
        (S) Start the quiz 
        (H) View the HighScore
        (R) Reset the HighScore
        (X) Quit the game""")
        userChoice=input()
        if userChoice.upper() == "S": #.upper makes it able to pass both upper and lowercase inputs
                startQuiz(questions)#Starts the quiz
        elif userChoice.upper() == "H":
                print("The HighScore is:",highScore,"/5 set by: ",highScoreName)
                mainMenu()
        elif userChoice.upper() == "R":#Resets the highScore
                global  high_score
                highScore=0
                highScoreName="Empty"
                high_score=str(highScore)
                f=open("HighScore.txt","w")#opens the highScore file
                f.write(high_score)#Saves the high_score variable to file
                f.close()
                f=open("HighScoreName.txt","w") #Opens the HighScoreName file
                f.write(highScoreName)#Saves the highScoreName variable which has been set as "Empty" to the file 
                f.close()                
                mainMenu()
        elif userChoice.upper() == "X":#Quits the quiz
                exit()
        else:
                print("Please use a valid input") #Error checking for invalid inputs
                mainMenu()

#Function to start the quiz.
def startQuiz(questions):
        score=0
        for question in questions:
                valid = False
                while valid == False: #Puts the question on loop until vaild = True
                        answer = input(question.promt).upper()#Asks the question
                        if answer in question.answers: 
                                valid = True #If the input is in the list of answers it sets valid to true
                                if answer == question.answer:
                                        score +=1 #Adds one to the score each time you get a question right
                                        print("Thats correct\n")
                                else:
                                        print("Thats incorrect, the right answer is ",(question.answer),"\n")
                        else:
                                print("Invalid input\n") #If the input is not one of the answers it prints invalid input and loops back to the same question
                        
        print("You got ",str(score),"/",str(len(questions)),"Correct")
        global highScore
        global user_name
        if score>highScore:#If the score is bigger than the current highScore than it is saved
                highScore=0
                highScore += score
                high_score=str(highScore)
                f=open("HighScore.txt","w") #opens the highScore file
                f.write(high_score)#Saves the high_score variable to file
                f.close()
                f=open("HighScoreName.txt","w") #Opens the HighScoreName file
                f.write(user_name)#Saves the user_name of the one that got the high Score to the file
                f.close()
                HighScoreName()
        mainMenu()#Goes back too the main menu

#Main routine (Starts the functions)
HighScoreName()
highScore()
intro()