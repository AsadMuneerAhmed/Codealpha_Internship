print("========================")
print("Welcom to my chatbaot")
print("========================")

def greet():
    print("Bot: Hello! How are you?")
def what_function():
    print("Bot: A function is a named block of code that performs a specific task.")
def how_are_you():
    print("Bot: That's great")

def joke():
    print("Bot: Ok tell me")
    print("Why did the computer go to the doctor?")

def answer_why():
    print("Bot: Because it caught a virus! 😄")

def how_are_you_user():
     print("Bot: I'm fine, thanks!")

def hey():
    print("Bot: Hello long time no see")
     
def what_about_you():
    print("Bot: I'm fine, thanks!")
    print(" Bot: Do you have any question")
    
while True:
 user_input = input("You: ").strip().lower() 
 if(user_input=="hello"):
      greet()
 elif(user_input=="i am fine"):
     how_are_you()
 elif(user_input=="hey"):
     hey()
 elif(user_input=="what is function?"):
     what_function()
 elif(user_input=="how are you"):
    how_are_you_user()
 elif(user_input=="what about you?"):
      what_about_you()
 elif(user_input=="i am fine"):
       print("Bot: That's great to hear!")
 elif(user_input=="what is your name?"):
     print( "Bot: I am Nova")
 elif(user_input=="tell me a joke"): 
   joke() 
 elif(user_input == "why"):
    answer_why()
 elif(user_input=="bye"):
     print("Bot: Bye! Have a nice day!")
     break
 else:
   print("Bot: Sorry, I didn't understand that.")
