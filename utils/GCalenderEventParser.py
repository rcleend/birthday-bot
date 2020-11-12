from models import Birthday
import shlex


class GCalendarEventParser:

    def parseToBirthday(self, event):
        event = dict(token.split('=') for token in shlex.split(event['description']))

        return Birthday.Birthday(event['contact'], event['name'], event['language'], event['gender'])
