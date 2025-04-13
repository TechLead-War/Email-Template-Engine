import os
import django

# 1. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_engine.settings")

# 2. Setup Django
django.setup()

# 3. Import your sample email sender
from email_engine.views import send_sample_problem_email


# 4. Define recipient list

users = [
    {
        'user_email': 'ayushkapri.richard@gmail.com'
    },
]


# 5. Send sample problem emails
for user in users:
    send_sample_problem_email(
        user_email=user["user_email"],
    )
