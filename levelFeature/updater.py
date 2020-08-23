import os
from apscheduler.schedulers.background import BackgroundScheduler
from .models import LevelReading


def read_csv(csv_file):

    with open(csv_file, "r") as file:
        for line in file:
            pass

    # Extracts data from most recent entry
    sr_num = int(line.split(',')[0])
    time = line.split(',')[1]
    level = int(line.split(',')[2])

    LevelReading.objects.all().delete()
    print('Deleted reading.')

    new_reading = LevelReading(sr_num=sr_num, time=time, reading_value=level)
    new_reading.save()
    print('Added reading.')


def start():
    csv_path = os.path.abspath('./levelFeature/example_csv.csv')

    scheduler = BackgroundScheduler()
    scheduler.add_job(read_csv, 'interval', minutes=10, args=[csv_path])
    scheduler.start()
