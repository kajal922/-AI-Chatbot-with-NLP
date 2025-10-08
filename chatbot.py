import nltk
from datetime import datetime

# First-time run ke liye nltk resources download
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections

# ------------------- Chatbot Pairs -------------------
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am your friendly chatbot.", "You can call me ChatBot."]
    ],
    [
        r"what is the time?",
        [f"The current time is {datetime.now().strftime('%H:%M:%S')}"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1!", "Hello %1, how can I assist you today?"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing fine!", "I'm good, thank you! How are you?"]
    ],
    [
        r"(.*) your name?",
        ["I’m ChatBot created with Python and NLTK."]
    ],
    [
        r"bye|exit|quit",
        ["Bye! Have a great day.", "Goodbye!"]
    ],
]

# ------------------- Chatbot -------------------
def chatbot():
    print("ChatBot: Hello! I am your chatbot. Type 'bye' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
