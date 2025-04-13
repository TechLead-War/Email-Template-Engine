import os
import django


# 1. Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_engine.settings")
django.setup()


# 2. Import send function (you need to create this if it's separate)
from email_engine.views import send_codecraft_invite_email


# 3. User list
users = [
    {'user_email': 'ayushkapri.richard@gmail.com', 'user_name': 'Ayush'},
]

# 4. Send loop
for user in users:
    send_codecraft_invite_email(
        user_email=user["user_email"],
        user_name=user["user_name"]
    )