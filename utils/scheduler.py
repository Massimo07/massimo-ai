from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def schedule_cron_task(func, cron_str: str):
    minute, hour, day, month, dow = cron_str.split()
    scheduler.add_job(func, "cron",
        minute=minute, hour=hour, day=day, month=month, day_of_week=dow)

def start_scheduler():
    scheduler.start()
