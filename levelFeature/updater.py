import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from . import constants


def read_csv(csv_file):

    with open(csv_file, "r") as file:
        for line in file:
            pass

    # Extracts data from most recent entry
    sr_num = int(line.split(',')[0])
    time = line.split(',')[1]
    level = int(line.split(',')[2])

    new_reading = {"sr_num": sr_num, "time": time, "reading_value": level}

    requests.delete(constants.DELETE_READINGS)
    print('Deleted tasks')

    resp = requests.post(constants.POST_LATEST, json=new_reading)
    print('Created task. ID: {}'.format(resp.json()["id"]))


def start():
    csv_path = os.path.abspath('./levelFeature/example_csv.csv')

    scheduler = BackgroundScheduler()
    scheduler.add_job(read_csv, 'interval', minutes=10, args=[csv_path])
    scheduler.start()
