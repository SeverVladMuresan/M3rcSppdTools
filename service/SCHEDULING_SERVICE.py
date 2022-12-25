import datetime


class SchedulingService:

    @staticmethod
    def get_next_even_half_hour():
        delta = datetime.timedelta(minutes=30)
        now = datetime.datetime.now()
        future_run_rough = now + delta
        minute_replacement = 0 if future_run_rough.minute < 30 else 30
        return future_run_rough.replace(microsecond=0, second=1, minute=minute_replacement)
