import random
import nltk
from nltk.chat.util import Chat, reflections

# Downloading NLTK resources
nltk.download('punkt')

# Defining pairs of patterns and responses
pairs = [
    [
        r"(.*) feeling (.*)",
        ["I'm sorry to hear you're feeling %2. Can you tell me more about what's been on your mind?",
         "Feeling %2 can be tough. What's been contributing to this feeling?",
         "It sounds like you're experiencing %2. Would you like to share more details?"]
    ],
    [
        r"(.*) sad (.*)",
        ["It's okay to feel sad sometimes. Have you tried talking to someone you trust about this?",
         "Sadness can be overwhelming. Remember, it's important to acknowledge your feelings. Can you think of a time when you felt better?",
         "When I'm sad, I find it helpful to reflect on moments of joy. Can you recall a happy memory?"]
    ],
    [
        r"(.*) stressed (.*)",
        ["Stress can be a heavy burden. Have you considered trying mindfulness or breathing exercises?",
         "When stress takes over, it's essential to take a step back. Can you think of one thing that helps you relax?",
         "I understand that stress can be challenging. Sometimes, breaking tasks into smaller steps can make them more manageable."]
    ],
    [
        r"(.*) anxious (.*)",
        ["Anxiety can feel overwhelming, but remember to breathe deeply. Have you tried grounding techniques?",
         "When anxiety strikes, grounding exercises can help. Try describing your surroundings in detail.",
         "It's normal to feel anxious at times. Have you considered writing down your thoughts to gain perspective?"]
    ],
    [
        r"(.*) lonely (.*)",
        ["Loneliness is a tough feeling. Have you reached out to friends or family lately?",
         "When feeling lonely, it might help to engage in activities you enjoy. What hobbies make you feel alive?",
         "Connecting with others, even virtually, can ease loneliness. Is there someone you could call or message?"]
    ],
    [
        r"(.*) (depressed|depression) (.*)",
        ["Depression is a serious concern. Have you talked to a mental health professional about your feelings?",
         "When dealing with depression, self-care is crucial. Have you tried journaling your thoughts and feelings?",
         "It's important to seek support when feeling depressed. Have you considered joining a support group or talking to a therapist?"]
    ],
    [
        r"(.*) overwhelmed (.*)",
        ["Feeling overwhelmed can be paralyzing. Have you tried breaking your tasks into smaller, more manageable pieces?",
         "It's important to take breaks and give yourself time to rest. What activities help you unwind?",
         "When overwhelmed, it can help to prioritize your tasks. What's the most urgent thing you need to do right now?"]
    ],
    [
        r"(.*) guilty (.*)",
        ["Guilt can be a heavy emotion. Have you thought about what you can do to make amends?",
         "It's important to forgive yourself and learn from your experiences. What can you do differently next time?",
         "Everyone makes mistakes. What can you do to move forward in a positive way?"]
    ],
    [
        r"(.*) angry (.*)",
        ["Anger is a natural emotion. Have you tried expressing your feelings in a constructive way?",
         "When anger arises, taking deep breaths and counting to ten can help. What triggered your anger?",
         "It's okay to feel angry, but it's important to address it healthily. Have you considered talking to someone about what's bothering you?"]
    ],
    [
        r"(.*) hopeless (.*)",
        ["Feeling hopeless can be very difficult. Have you reached out to someone who can offer support?",
         "It's important to remember that feelings of hopelessness are temporary. Can you think of any small steps you can take to improve your situation?",
         "When feeling hopeless, connecting with a mental health professional can provide guidance. Have you considered this?"]
    ],
    [
        r"(.*) insecure (.*)",
        ["Insecurity can stem from various sources. What do you think is causing these feelings?",
         "It's important to recognize your strengths and achievements. Can you list a few things you are proud of?",
         "Talking to a trusted friend or counselor can help you work through feelings of insecurity. Have you tried this?"]
    ],
    [
        r"(.*) panic (.*)",
        ["Panic attacks can be frightening. Have you tried grounding techniques like focusing on your breath?",
         "When you feel panic rising, it can help to remind yourself that this feeling will pass. What usually helps you calm down?",
         "Consider speaking to a therapist who can teach you coping strategies for panic attacks. Have you reached out for professional help?"]
    ],
    [
        r"(.*) (bipolar|manic|mania) (.*)",
        ["Managing bipolar disorder can be challenging. Are you currently following a treatment plan?",
         "It's important to stay connected with your healthcare provider about your symptoms. How have you been feeling lately?",
         "Have you been able to maintain a routine and take your medications as prescribed?"]
    ],
    [
        r"(.*) PTSD (.*)",
        ["PTSD can deeply affect your life. Are you currently receiving treatment or therapy for it?",
         "It's important to practice self-care and reach out for support. Have you found any coping strategies that help?",
         "Talking to a mental health professional about your experiences can be very beneficial. Have you considered this?"]
    ],
    [
        r"(.*) (OCD|obsessive-compulsive) (.*)",
        ["Living with OCD can be tough. Are you currently in therapy or receiving treatment?",
         "It can help to practice exposure and response prevention techniques. Have you tried these?",
         "Discussing your symptoms with a mental health professional can provide you with strategies to manage them."]
    ],
    [
        r"(.*) quit",
        ["It was lovely talking to you. Remember, I'm always here if you need to talk again. Take care!"]
    ],
    [
        r"(.*)",
        ["I'm here to listen. Can you tell me more about how you're feeling?",
         "Your feelings are valid. Would you like to talk about it?",
         "I'm here to support you. What's been on your mind lately?"]
    ]
]

# Function to start the chatbot
def mental_health_chatbot():
    print("Hello, I'm your mental health chatbot. How can I assist you today? (Type 'quit' to exit)")
    chat = Chat(pairs, reflections)
    chat.converse()

# Running the chatbot
if __name__ == "__main__":
    mental_health_chatbot()
