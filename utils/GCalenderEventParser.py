from models import Birthday


class GCalendarEventParser:

    def parseToBirthday(self, event):
        description = event['description'].splitlines()

        # TODO: build check
        contact = description[0]
        name = description[1]
        language = description[2]
        gender = description[3]

        return Birthday.Birthday(contact, name, language, gender)
