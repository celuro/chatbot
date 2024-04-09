import random

# Keywords
greeting = ["Hello", "Hey", "Hi"]
weather = ["weather", "today"]
joke = ["me", "joke"]

# Amount of Responses
bot_greeting = ["What's up!", "Yo!", "How's it hanging!", "Hey!", "Hiya!", "Hello!",
                 "Hey!", "Hi!"]

bot_weather = ["The weather forecast for today is 19°C.", 
               "I expect the weather to be 19°C later.", 
               "The weather will be 19°C"]

bot_joke = ["Why did the chicken cross the road? To get to the other side!",
            "What did the pirate say when he turned 80? Aye matey!",
            "Why did the frog take the bus to work today? His car got toad away!"]

bot_error = ["I'm sorry, I don't understand. Can you try again?",
             "I don't understand, please try again.",
             "I do not have enough data to respond.",
             "I can't answer you, try again!"]

# We need to hold the user response in a variable to make it easier for the bot to respond
user_response = ""

# Introduction message to inform the user the program started
print("Welcome to the chatbot ^^")
print("-------------------------")

# Program ends if the user enters x
while(user_response != "exit"):
  print("Bot:", "Hello, I'm Bot! What can I help you with?")
  print("Type exit to quit")
  # I think responses based on keywords would be the way to go
  user_response = input("User: ")
  if(user_response == "exit"):
    print("Goodbye!")
  else:
    # Generates Random Responses based on user keywords
    if any(word in user_response for word in greeting):
      print("Bot:", random.choice(bot_greeting))
    elif any(word in user_response for word in weather):
      print("Bot:", random.choice(bot_weather))
    elif any(word in user_response for word in joke):
      print("Bot:", random.choice(bot_joke))
    else:
      print("Bot:", random.choice(bot_error))
