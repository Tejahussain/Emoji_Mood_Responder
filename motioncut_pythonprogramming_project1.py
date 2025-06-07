# Step 1: Create a dictionary for mood → emoji + message
mood_dict = {
    "happy": ("😊", "Keep smiling, you're doing great!"),
    "sad": ("😢", "It's okay to feel sad. Better days are coming!"),
    "angry": ("😠", "Take a deep breath. Stay calm."),
    "excited": ("🤩", "That's awesome! Enjoy the moment!"),
    "tired": ("😴", "Rest is important. Take care!"),
    "anxious": ("😬", "You're stronger than you think. Stay grounded."),
    "lonely": ("🥺", "You're not alone. Reach out to someone you trust."),
    "awful": ("😖", "Bad days happen. Be kind to yourself."),
    "relaxed": ("😌", "That's great. Enjoy the peace!"),
    "bored": ("😐", "Try something new. Even small changes help!"),
    "confused": ("😕", "It's okay to not have all the answers right now."),
    "loved": ("🥰", "You are cherished and appreciated!"),
    "grateful": ("🙏", "Gratitude is a gift. Keep sharing it."),
    "inspired": ("🌟", "Let that spark turn into action!")
}

# Step 2–5: Keep running until user types 'exit'
print("Welcome to the Emoji Mood Responder!")
print("Type how you're feeling (or type 'exit' to stop):")

while True:
    mood_input = input("\nYour mood: ").lower()
    
    if mood_input == "exit":
        print("👋 Goodbye! Take care of your emotions!")
        break
    
    if mood_input in mood_dict:
        emoji, message = mood_dict[mood_input]
    else:
        emoji, message = "🤔", "Hmm, I don't recognize that feeling, but I'm here for you!"
    
    print(f"{emoji} {message}")
