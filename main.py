
import random
import pyttsx3
import time

# Initialize TTS Engine
engine = pyttsx3.init()

# Questions Data
questions = [
    {
        "question": "What is Ramanujan's birthdate?",
        "OptionsForThisQuestion": "The options for this question are:",
        "options": ["a) 22 December 1887", "b) 22 December 1889", "c) 22 December 1888", "d) 22 December 1886"],
        "chooseOptions": "Please choose the correct option.",
        "goodSentence": "The correct answer is:",
        "answer": "a",
        "explanation": "Ramanujan was born on 22 December 1887."
    },
    {
        "question": "In which mathematical field is Ramanujan known for his work?",
        "OptionsForThisQuestion": "The options for this question are:",
        "options": ["a) Number Theory", "b) Calculus", "c) Geometry", "d) Trigonometry"],
        "chooseOptions": "Please choose the correct option.",
        "goodSentence": "The correct answer is:",
        "answer": "a",
        "explanation": "Ramanujan made extraordinary contributions to number theory, including concepts like infinite series and mathematical analysis."
    },
    {
        "question": "Srinivasa Ramanujan was born in which village?",
        "OptionsForThisQuestion": "The options for this question are:",
        "options": ["a) Erode, Erode District, Tamil Nadu", "b) Kumbakonam, Thanjavur District, Tamil Nadu", 
                    "c) Ayilur, Erode District, Tamil Nadu", "d) Thiruvanaikoil, Tiruchirappalli District, Tamil Nadu"],
        "chooseOptions": "Please choose the correct option.",
        "goodSentence": "The correct answer is:",
        "answer": "a",
        "explanation": "Srinivasa Ramanujan was born in Erode, a village in the Erode district of Tamil Nadu."
    },
    {
        "question": "Which of the following numbers is NOT considered a Hardy-Ramanujan number?",
        "OptionsForThisQuestion":"And The Options for this Question are!",
        "options": ["a) 1729", "b) 4104", "c) 13832", "d) 25467"],
        "chooseOptions": "Please choose the Options for this Question",
        "goodSentence": "The Correct Answer for This Question is",
        "answer": "d",
        "explanation": " Numbers like 1729, 4104, and 13832 are Hardy-Ramanujan numbers as they can be expressed as the sum of two cubes in two different ways. However, 25467 does not have this property."
    },    
    {
        "question": "Which Prime Minister initiated the celebration of December 22 as National Mathematics Day?",
        "OptionsForThisQuestion":"And The Options for this Question are!",
        "options": ["a) Atal Bihari Vajpayee ", "b) Dr. Manmohan Singh", "c) Narendra Modi", "d) P. V. Narasimha Rao"],
        "chooseOptions": "Please choose the Option for this Question",
        "goodSentence": "The Correct Answer for This Question is",
        "answer": "b",
        "explanation": " The celebration was initiated by Dr. Manmohan Singh in 2012 to honor the contributions of Ramanujan."
    },    
    {
        "question": "From which year have we been celebrating December 22 as National Mathematics Day?",
        "OptionsForThisQuestion":"And The Options for this Question are!",
        "options": ["a) 2010", "b) 2011", "c) 2012", "d) 2013"],
        "chooseOptions": "Please choose the Options for this Question",
        "goodSentence": "The Correct Answer for This Question is",
        "answer": "c",
        "explanation": " December 22 was declared National Mathematics Day in 2012, on the 125th birth anniversary of Ramanujan."
    },    
    {
        "question": "4104 can be expressed as the sum of two cubes in how many different ways, as per the Hardy-Ramanujan number property?",
        "OptionsForThisQuestion":"And The Options for this Question are!",
        "options": ["a) One Way ", "b) Two Ways", "c) Three Ways", "d) Four Ways"],
        "chooseOptions": "Please choose the Option for this Question",
        "goodSentence": "The Correct Answer for This Question is",
        "answer": "b",
        "explanation": " 4104 can Be Expressed as 2^3 + 16^3 and 9^3 + 15^3, Making It A Hardy - Ramanujan Number."
    },    
    {
        "question": "Where did Ramanujan study and earn his Bachelor of Science degree?",
        "OptionsForThisQuestion":"And The Options for this Question are!",
        "options": ["a) Presidency College, Madras", "b) Cambridge University", "c) Erode Arts College", "d) Trinity College, London"],
        "chooseOptions": "Please choose the Options for this Question",
        "goodSentence": "The Correct Answer for This Question is",
        "answer": "d",
        "explanation": " Srinivasa Ramanujan earned his Bachelor of Science degree in 1916 from Trinity College, London.."
    },    
    {
        "question": "Who was Ramanujan's best friend at Cambridge?",
        "OptionsForThisQuestion":"And The Options for this Question are!",
        "options": ["a) G. H. Hardy ", "b) J. E. Littlewood", "c) Bertrand Russell", "d) Alfred North Whitehead"],
        "chooseOptions": "Please choose the Option for this Question",
        "goodSentence": "The Correct Answer for This Question is",
        "answer": "a",
        "explanation": " G. H. Hardy, a prominent British mathematician, was not only Ramanujan's mentor but also his closest friend during his time at Cambridge."
    },    
    {
        "question": "What was the name of the journal where Ramanujan published his first research paper?",
        "OptionsForThisQuestion": "The options for this question are:",
        "options": [
            "a) Journal of the Indian Mathematical Society",
            "b) Proceedings of the Cambridge Philosophical Society",
            "c) Transactions of the American Mathematical Society",
            "d) Annals of Mathematics" ],
        "chooseOptions": "Please choose the correct option.",
        "goodSentence": "The correct answer is:",
        "answer": "a",
        "explanation": "Ramanujan's first research paper, titled 'Some Properties of Bernoulli's Numbers,' was published in the Journal of the Indian Mathematical Society in 1911."
    },

     # Agar Afternoon Tak Aur Questions Milgayatho add kardhena.
]

# Function to Know the Greet
def greet_user():
    # Get the current hour in 24-hour format
    current_hour = time.localtime().tm_hour
    # The tm_hour attribute from time.localtime() will return an integer between 0 and 23, inclusive. This represents the current hour in 24-hour format.
    
    # Determining the greeting based on the hour
    if  current_hour >= 0 and current_hour < 12:
        greeting = "Good Morning"
    elif current_hour >= 12 and current_hour < 16:
        greeting = "Good Afternoon"
    elif current_hour >= 16 and current_hour <= 21:
        greeting = "Good Evening"
    else: # Exceptional Case for the Hours >= 10pm in 12 hrs Clock.
        greeting = "Hello"
    return greeting
# Welcome Message
def welcome():
    knowTheGreet = greet_user() # Function Calling
    for i in range(5):
        print("")
    for i in range(50):
        print(" ",end = '')
    print("Hello,", end = '')
    print(knowTheGreet)
    engine.say("Hello")
    engine.say(knowTheGreet)
    engine.runAndWait()
    engine.say("Welcome to the TTS-based quiz program on Srinivasa Ramanujan's life and his contributions to mathematics!")
    engine.runAndWait()
    user_name = ask_user_name() # Function calling
    gender = get_gender(user_name) # Function calling
    if gender == "male":
        message = f"Hello Mr. {user_name}, are you ready? Let's start the quiz!"
    elif gender == "female":
        message = f"Hello Ms. {user_name}, are you ready? Let's start the quiz!"
    else:
        message = f"Hello {user_name}, are you ready? Let's start the quiz!"
    print(message)
    engine.say(message)
    engine.runAndWait()

# Ask User Name
def ask_user_name():
    engine.say("Please enter your name to start the quiz program.")
    engine.runAndWait()
    return input("Please enter your name to start the quiz program: ")

# Predict Gender
def get_gender(name):
    try:
        response = requests.get(f"https://api.genderize.io?name={name}")
        response.raise_for_status()
        data = response.json()
        return data.get("gender", "unknown").lower()
    except Exception as e:
        return "unknown"

# Quiz Function
def quiz():
    score = 0
    random.shuffle(questions)
    counter = 1
    for q in questions:
        engine.say(f"lets Move To The Question Number{counter}")
        counter = counter + 1
        print("\n" + q["question"])
        engine.say(q["question"])
        engine.say(q["OptionsForThisQuestion"])
        for option in q["options"]:
            print(option)
            engine.say(option)
        # engine.runAndWait()
        engine.say(q["chooseOptions"])
        engine.runAndWait()
        answer = input("\nEnter your answer (a/b/c/d): ").strip().lower()
        if answer == q["answer"]:
            print("Correct!")
            engine.say("Correct!")
            score += 1
        else:
            print(f"{q['goodSentence']} {q['answer']}.")
            print("Explanation:", q["explanation"])
            engine.say(q["goodSentence"])
            engine.say(q["answer"])
            engine.say(q["explanation"])
        engine.runAndWait()

    print(f"\nYour final score is: {score}/{len(questions)}")
    engine.say(f"Your final score is {score} out of {len(questions)}")
    print("Thank You For Your Participation")
    engine.say("Thank You For Your Participation")
    engine.runAndWait()

# Main Program
if __name__ == "__main__":
    welcome()
    quiz()







