from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler
import pymongo
import telebot
from woocommerce import API
from dotenv import load_dotenv
import os
import telebot

import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
load_dotenv()

# TOKEN = os.getenv("TOKEN")
DEBUG = (os.getenv("DEBUG") == "True")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

pipeline = 2
if pipeline == 1:
    load_dotenv(dotenv_path="bst.env")
if pipeline == 2:
    load_dotenv(dotenv_path="premium.env")

environment = os.getenv("environment")
sessionString = os.getenv("sessionString")
token = os.getenv("token")
ckey = os.getenv("ckey")
csecret = os.getenv("csecret")
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
channel_link = os.getenv("channel_link")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
heroku_url = os.getenv("heroku_url")
wordpress_url = os.getenv("wordpress_url")
debug = (os.getenv("debug") == "True")

print(f"Environment is {environment}")

sessionString = os.getenv("sessionString")
join_channel_markup = telebot.types.InlineKeyboardMarkup()
join_channel_button = telebot.types.InlineKeyboardButton(
    text="Join Now ✅", url=channel_link, callback_data="join_channel")
join_channel_markup.add(join_channel_button)

wcapi = API(
    timeout=10,
    url=wordpress_url,
    consumer_key=ckey,
    consumer_secret=csecret,
    wp_api=True,
    version="wc/v3",
    query_string_auth=True
)


bot = telebot.TeleBot(
    token,
    threaded=True
)


client = pymongo.MongoClient(db_host)

jobstores = {
    'default': MongoDBJobStore(client=client, database=db_name, HOST=db_host),
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    # 'default': ThreadPoolExecutor(20),
    # 'processpool': ProcessPoolExecutor(5)
}

job_defaults = {
    'max_instances': 3,
    'misfire_grace_time': 259200
}
scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc
)
