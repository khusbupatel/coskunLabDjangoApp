import requests
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler


def read_csv(csv_file):

    with open(csv_file, "r") as file:
        for line in file:
            pass

    # Extracts data from most recent entry
    sr_num = int(line.split(',')[0])
    time = line.split(',')[1]
    level = int(line.split(',')[2])

    new_reading = {"sr_num": sr_num, "time": time, "reading_value": level}
    resp = requests.post('http://127.0.0.1:8000/post_reading/', json=new_reading)
    print('Created task. ID: {}'.format(resp.json()["id"]))


scheduler = BackgroundScheduler()
scheduler.add_job(read_csv, CronTrigger.from_crontab('2 * * * *'), args=[r'C:\Users\allis\Downloads\csv_file.csv'])
# scheduler.add_job(read_csv, 'cron', hour='*', args=[r'C:\Users\allis\Downloads\csv_file.csv'])
scheduler.start()
