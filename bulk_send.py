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
    {'user_email': 'barkharawat621@gmail.com', 'user_name': 'Shreya Rawat'},
    {'user_email': 'bhaveshkandpal88@gmail.com', 'user_name': 'Bhavesh Kandpal'},
    {'user_email': 'specious0027@gmail.com', 'user_name': 'Sourabh Singh'},
    {'user_email': 'dineshdumka874@gmail.com', 'user_name': 'Dinesh Dumka'},
    {'user_email': 'Deewasjalal@gmail.com', 'user_name': 'Deewas Singh'},
    {'user_email': 'harshhhverma01@gmail.com', 'user_name': 'Harsh Verma'},
    {'user_email': 'manralkartik09@gmail.com', 'user_name': 'KARTIK MANRAL'},
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