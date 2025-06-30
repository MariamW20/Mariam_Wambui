import os
import logging
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
import tweepy

# Load environment variables
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Client (v2)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Messages
messages = {
    "Monday": "Monday Motivation: Start your week with a positive mindset! #MondayMotivation",
    "Tuesday": "Tuesday Tips: Did you know that consistency is key to success? #TuesdayTips",
    "Wednesday": "Wednesday Wisdom: Keep pushing forward, you're halfway through the week! #WednesdayWisdom",
    "Thursday": "Thursday Thoughts: Reflect on your progress and set new goals! #ThursdayThoughts",
    "Friday": "Friday Fun: It's almost the weekend! What are your plans? #FridayFun",
    "Saturday": "Saturday Vibes: Take a break and enjoy some leisure time! #SaturdayVibes",
    "Sunday": "Sunday Reflections: Prepare for the week ahead and set your intentions! #SundayReflections"
}

def post_daily_message():
    today = datetime.now().strftime('%A')
    message = messages.get(today)
    if message:
        try:
            client.create_tweet(text=message)
            logging.info(f"Posted: {message}")
        except Exception as e:
            logging.error(f"Failed to post: {e}")

schedule.every().day.at("08:00").do(post_daily_message)

logging.info("Scheduler started. Awaiting next post time...")
while True:
    schedule.run_pending()
    time.sleep(60)
