from utils import GCalendarAPI
from utils import GCalenderEventParser
from utils import MessageBuilder
from utils import MessageSender

from dotenv import load_dotenv
import os
import datetime

load_dotenv()

myGCalendarEventParser = GCalenderEventParser.GCalendarEventParser()
myGCalendarAPI = GCalendarAPI.GCalendarAPI()
myMessageBuilder = MessageBuilder.MessageBuilder()
myMessageSender = MessageSender.MessageSender()

myGCalendarAPI.authenticate()

time_min = datetime.datetime.now().isoformat() + 'Z'  # 'Z' indicates UTC time
time_max = (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat() + 'Z'  # 'Z' indicates UTC time

my_events = myGCalendarAPI.get_events(os.getenv("CALENDAR_ID"), time_min, time_max)

if not my_events:
    print('No upcoming events found.')
    exit()

for event in my_events:
    birthday = myGCalendarEventParser.parseToBirthday(event)
    myMessageBuilder.build_birthday_message(birthday)
    myMessageSender.send_message(birthday.contact, birthday.message)
