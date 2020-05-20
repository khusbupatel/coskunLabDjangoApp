import os
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler


def read_csv(csv_file):

    with open(csv_file, "r") as file:
        for line in file:
            pass

    # Extracts level reading from most recent entry
    level = int(line.split(',')[-1])

    # if level < 0:
    # send warning message to appear on front end


scheduler = BackgroundScheduler()
# scheduler.add_job(read_csv, CronTrigger.from_crontab('2 * * * *'), args=["example_csv.csv])
scheduler.add_job(read_csv, 'cron', hour='*', args=["example_csv.csv"])
scheduler.start()