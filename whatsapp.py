import pywhatkit
import random
from datetime import datetime

# Lists of messages
sweet_greetings = [
    "Good morning, Omi! Have a fantastic day ahead.",
    "Morning, beautiful! Hope you slept well.",
    "Rise and shine, Omi! You're amazing.",
    "Good morning, sunshine! Ready to conquer the day?",
    "Hey there, good morning! Sending you a virtual hug.",
    "Wake up, sleepyhead! The world needs your smile today.",
    "Good morning, Omi! Let's make today great.",
    "Morning, love! Can't wait to see you later.",
    "Good morning, my dear Omi! You mean the world to me.",
    "Hey Omi, rise and shine! Hope your day is as wonderful as you.",
    "Good morning, gorgeous! You're the reason I smile every day.",
    "Morning, Omi! Sending you lots of love.",
    "Good morning, my love! Have a fantastic day.",
    "Rise and shine, Omi! Today is your day.",
    "Good morning, beautiful! You light up my life.",
    "Hey there, good morning! Let's make today amazing.",
    "Good morning, Omi! Hope your day is as wonderful as you.",
    "Morning, love! You're my sunshine.",
    "Good morning, my dear Omi! Thinking of you.",
    "Hey Omi, rise and shine! Have a great day."
]

sweet_good_mornings = [
    "Good morning, my love! Wishing you a day as bright as your smile.",
    "Morning, Omi! Hope you have a wonderful day.",
    "Good morning, beautiful! I can't wait to see you.",
    "Rise and shine, sweetheart! Today is going to be amazing.",
    "Good morning, my dear Omi! Sending you all my love.",
    "Morning, sunshine! You make every day better.",
    "Good morning, Omi! Let's make today special.",
    "Hey there, good morning! Can't stop thinking about you.",
    "Good morning, love! Hope you have an incredible day.",
    "Rise and shine, Omi! You're the best part of my day.",
    "Good morning, beautiful! Hope you slept well.",
    "Morning, Omi! Can't wait to see you later.",
    "Good morning, my love! You mean the world to me.",
    "Hey Omi, rise and shine! Hope your day is as wonderful as you.",
    "Good morning, gorgeous! You're the reason I smile every day.",
    "Morning, love! Sending you lots of hugs and kisses.",
    "Good morning, my dear Omi! Have a fantastic day.",
    "Rise and shine, Omi! Today is your day.",
    "Good morning, beautiful! You light up my life.",
    "Hey there, good morning! Let's make today amazing."
]

sweet_lunch_texts = [
    "Hey Omi, just wanted to say I love you. Enjoy your lunch!",
    "Thinking of you, Omi! Hope you have a delicious lunch.",
    "Hi Omi, hope you're having a great day. Enjoy your lunch!",
    "Lunch time, love! Don't forget to eat something yummy.",
    "Hey Omi, just a reminder that you're amazing. Have a great lunch!",
    "Hi love, just wanted to send you a little lunch time love. Enjoy!",
    "Hope you're having a fantastic day, Omi! Enjoy your lunch break.",
    "Hey beautiful, just thinking of you. Have a lovely lunch!",
    "Lunch time, Omi! Make sure to take a break and enjoy.",
    "Hi Omi, hope you're having a productive day. Don't skip lunch!",
    "Just wanted to send you a little love during lunch, Omi. Enjoy!",
    "Hey love, hope your day is going well. Have a great lunch!",
    "Lunch time, beautiful! Don't forget to take a break.",
    "Hi Omi, sending you hugs and kisses. Enjoy your lunch!",
    "Hope you're having a wonderful day, Omi. Lunch time love!",
    "Hi love, just a little message to brighten your lunch break. Enjoy!",
    "Lunch time, Omi! Take a moment to relax and enjoy.",
    "Hey beautiful, thinking of you. Hope you have a great lunch!",
    "Hi Omi, just wanted to send you some lunch time love. Enjoy!",
    "Hope you're having a fantastic day, Omi. Enjoy your lunch!"
]

sweet_random_texts = [
    "Just wanted to say I love you, Omi!",
    "Thinking of you, beautiful!",
    "Hope you're having a great day, Omi.",
    "You mean the world to me, Omi.",
    "Can't wait to see you later, love!",
    "You're amazing, Omi!",
    "Sending you lots of love and hugs.",
    "Hope you're smiling right now, Omi.",
    "Just wanted to make you smile, beautiful.",
    "Thinking of you and your beautiful smile.",
    "You're always on my mind, Omi.",
    "Can't wait to be with you, love.",
    "You brighten up my day, Omi.",
    "Hope you're having an amazing day, beautiful.",
    "You're the best thing that ever happened to me, Omi.",
    "Just wanted to send you some love.",
    "Thinking of you, love. Have a great day!",
    "You're my sunshine, Omi.",
    "Hope you're having a fantastic day, beautiful.",
    "You're always in my thoughts, Omi."
]

sweet_mid_morning_texts = [
    "Just wanted to say I love you, Omi!",
    "Thinking of you, beautiful!",
    "Hope you're having a great morning, Omi.",
    "You mean the world to me, Omi.",
    "Can't wait to see you later, love!",
    "You're amazing, Omi!",
    "Sending you lots of love and hugs.",
    "Hope you're smiling right now, Omi.",
    "Just wanted to make you smile, beautiful.",
    "Thinking of you and your beautiful smile.",
    "You're always on my mind, Omi.",
    "Can't wait to be with you, love.",
    "You brighten up my day, Omi.",
    "Hope you're having an amazing morning, beautiful.",
    "You're the best thing that ever happened to me, Omi.",
    "Just wanted to send you some love.",
    "Thinking of you, love. Have a great morning!",
    "You're my sunshine, Omi.",
    "Hope you're having a fantastic morning, beautiful.",
    "You're always in my thoughts, Omi."
]


def send_message(phone_number, message):
    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
    except:
        print("Failed to send message.")

def get_time_period():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 10:
        return "morning"
    elif 10 <= current_hour < 12:
        return "mid_morning"
    elif 12 <= current_hour < 14:
        return "lunch"
    elif 14 <= current_hour < 18:
        return "afternoon"
    elif 18 <= current_hour < 22:
        return "evening"
    else:
        return "random"

def get_message(time_period):
    if time_period == "morning":
        return random.choice(sweet_good_mornings)
    elif time_period == "mid_morning":
        return random.choice(sweet_mid_morning_texts)
    elif time_period == "lunch":
        return random.choice(sweet_lunch_texts)
    elif time_period == "afternoon" or time_period == "evening":
        return random.choice(sweet_greetings)
    else:
        return random.choice(sweet_random_texts)

def main():
    phone_number = "+254725571239"  # Replace with Omi's phone number
    time_period = get_time_period()
    message = get_message(time_period)
    send_message(phone_number, message)

if __name__ == "__main__":
    main()
