# General Scheduling in UCT (Zulu military time)
import pytz
import appAuth, twitpost
from datetime import datetime


    # scheduler = sched.scheduler(time.time, time.sleep)
    # def print_event(name):
    #     print('EVENT: {0} {1}'.format(time.time(), name))

    # print('START: {0}'.format(time.time()))
    # scheduler.enter(2, 1, print_event, ('first',))
    # scheduler.enter(4, 1, print_event, ('second',))

    # scheduler.run()


while True:
    tcur = datetime.utcnow().replace(tzinfo = pytz.utc)



    # 2.5 hours pre-trading day in UCT
    if (tcur.hour >= 11 and tcur.hour < 13) or (tcur.hour == 13 and tcur.minute < 30):


    # not in trading day
    else:

