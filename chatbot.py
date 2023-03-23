pip install nltk

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

import random

def get_response(intents, intent):
    responses = intents[intent]['responses']
    return random.choice(responses)
  
intents = {
    'greeting': {
        'patterns': ['hi', 'hello', 'hey', 'good morning', 'good afternoon'],
        'responses': ['Hello!', 'Hi there!', 'Hey!', 'Good morning!', 'Good afternoon!']
    },
    'goodbye': {
        'patterns': ['bye', 'goodbye', 'see you later', 'take care', 'have a nice day'],
        'responses': ['Goodbye!', 'See you later!', 'Take care!', 'Have a nice day!', 'Farewell!']
    },
    'thanks': {
        'patterns': ['thank you', 'thanks', 'appreciate it', 'thank you so much'],
        'responses': ['You\'re welcome!', 'No problem!', 'Glad I could help.', 'My pleasure!']
    },
    'positive_feedback': {
        'patterns': ['great', 'awesome', 'amazing', 'fantastic'],
        'responses': ['Thank you!', 'I appreciate the positive feedback!', 'Glad you think so!', 'Thanks for letting me know!']
    },
    'negative_feedback': {
        'patterns': ['terrible', 'bad', 'not good', 'poor'],
        'responses': ['I\'m sorry to hear that.', 'I apologize for the inconvenience.', 'I will do better next time.', 'Thanks for your feedback.']
    },
    'joke': {
        'patterns': ['tell me a joke', 'make me laugh', 'do you know any jokes?'],
        'responses': ['Why don\'t scientists trust atoms? Because they make up everything!', 'What do you call a fake noodle? An impasta!', 'Why don\'t sharks live on land? Because they can\'t climb trees!', 'Why did the tomato turn red? Because it saw the salad dressing!']
    },
    'default': {
        'responses': ['I\'m sorry, I didn\'t understand.', 'Could you please repeat that?', 'I\'m not sure what you mean.']
    }
}

def chatbot_response(user_input):
    response_list = []  # Initialize an empty list to store the bot's responses
    tokens = preprocess(user_input)
    for intent in intents:
        if 'patterns' in intents[intent]:
            patterns = intents[intent]['patterns']
            matches = set(tokens) & set(patterns)
            if matches:
                response_list.append(get_response(intents, intent))
    if not response_list:  # If no intent matches the user input, use the default response
        response_list.append(get_response(intents, 'default'))
    return response_list

while True:
    user_input = input('You: ')
    bot_responses = chatbot_response(user_input)
    for response in bot_responses:
        print('Bot:', response)

