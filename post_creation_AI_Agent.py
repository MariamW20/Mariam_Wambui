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

# Daily motivational messages
messages = {
    "Monday": "New week, new goals. Believe in yourself and start strong. 💪 #MindfulMonday",
    "Tuesday": "Take one bold step today. Growth begins outside your comfort zone. 🚀 #TakeActionTuesday",
    "Wednesday": "Pause. Breathe. You’re doing better than you think. ✨ #WellnessWednesday",
    "Thursday": "Small steps every day lead to big changes. Keep going. 🚶‍♀️ #ThoughtfulThursday",
    "Friday": "Celebrate your wins, no matter how small. You made it! 🎉 #FeelGoodFriday",
    "Saturday": "Let go of the rush. Recharge. Reconnect. 🌿 #SelfcareSaturday",
    "Sunday": "Slow down. Rest is productive too. Let today be your pause. 🌸 #SereneSunday"
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

schedule.every().day.at("10:00").do(post_daily_message)

logging.info("Scheduler started. Awaiting next post time...")
while True:
    schedule.run_pending()
    time.sleep(60)
