import os
import django

# 1. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_engine.settings")

# 2. Setup Django
django.setup()

# 3. Import your sample email sender
from email_engine.views import round_one_mail

# 4. Define recipient list

users = [
    {
        'user_email': 'ayushkapri.richard@gmail.com'
    },
    {
        'user_email': 'rajaarav272@gmail.com'
    },
    {
        'user_email': 'dhruv16carter@gmail.com'
    },
    {
        'user_email': 'shivanibansal9928031918@gmail.com'
    }
]

# 5. Send sample problem emails
for user in users:
    round_one_mail(
        user_email=user["user_email"],
    )
