import os
import django

# 1. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_engine.settings")

# 2. Setup Django
django.setup()

# 3. Import your email function
from email_engine.views import send_thank_you_email



# 4. Define recipient list
users = [
    {"user_email": "gayatrisingh9317@gmail.com", "user_name": "Gayatri Singh"},
    {"user_email": "kartikeywariyal706@gmail.com", "user_name": "Kartikey Wariyal"},
    {"user_email": "riyagarjola0@gmail.com", "user_name": "Riya Garjola"},
    {"user_email": "utpalsharma110@gmail.com", "user_name": "Utpal Sharma"},
    {"user_email": "anurag.p00000@gmail.com", "user_name": "Anurag Parmar"},
    {"user_email": "mhifzan802@gmail.com", "user_name": "Mohd Hifzan"},
    {"user_email": "vedantrai1819@gmail.com", "user_name": "Vedant Rai"},
    {"user_email": "harshitapathak0123@gmail.com", "user_name": "HARSHITA PATHAK"},
    {"user_email": "lakshitakanwal25@gmail.com", "user_name": "Lakshita Kanwal"},
    {"user_email": "shivanshsinghchauhan048@gmail.com", "user_name": "Shivansh Singh Chauhan"},
    {"user_email": "deepanshupathak36@gmail.com", "user_name": "Deepanshu Pathak"},
    {"user_email": "sauravmehta631@gmail.com", "user_name": "Saurav Singh Mehta"},
]

# 5. Define event metadata
event_name = "Codecraft, WeCode 2025"
event_date = "21 April 2025"
event_location = "Graphic Era Hill University, Bhimtal Campus"
event_url = "https://docs.google.com/document/d/1eomKgz2bjMuiXGcYEnRTu_eYzz-d89PwO2O2Wn9Eizw/edit?usp=sharing"
instagram_url = "https://www.instagram.com/wecode_gehu?igsh=aGU1cWpzeGZqMGVt"
whatsapp_url = "https://chat.whatsapp.com/CHVTHR9uD1BHlJBl1gxoRw"


# 6. Send emails
for user in users:
    send_thank_you_email(
        user_email=user["user_email"],
        user_name=user["user_name"],
        event_name=event_name,
        event_date=event_date,
        event_location=event_location,
        event_url=event_url,
        instagram_url=instagram_url,
        whatsapp_url=whatsapp_url,
        calendar_url=(
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=WeCode Hackathon"
            "&dates=20250421T090000/20250423T180000"
            "&details=Join us at Bhimtal Campus for a thrilling 3-day coding showdown!"
            "&location=Bhimtal Campus"
        )
    )