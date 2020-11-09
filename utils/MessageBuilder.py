import json
import random

class MessageBuilder:

    def build_birthday_message(self, birthday):
        random_message = self.get_random_birthday_message(birthday.language, birthday.gender)
        birthday.message = random_message.replace('_', birthday.name)

    def get_random_birthday_message(self, language, gender):
        with open('birthday_messages.json') as f:
            messages = json.load(f)

        return random.choice(messages[gender][language])




