import random
from Data import Welcome

def WelcomeMessage():
    messages= Welcome.Welcome.message()
    print(random.choice(messages))
WelcomeMessage()