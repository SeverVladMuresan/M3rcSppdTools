import sched
import time
import datetime


class SchedulingService:

    @staticmethod
    def schedule_in_next_even_half_hour(action):
        scheduler = sched.scheduler(time.time, time.sleep)
        delta = datetime.timedelta(minutes=30)
        now = datetime.datetime.now()
        future_run_rough = now + delta
        minute_replacement = 0 if future_run_rough.minute < 30 else 30
        next_even_half_hour = action.replace(microsecond=0, second=1, minute=minute_replacement)

        scheduler.enterabs(next_even_half_hour.timestamp(), 1, action)
        scheduler.run()
