import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_engine.settings")
django.setup()


from email_engine.views import send_codecraft_hackathon_invite_email

users = [
    {
        'user_email': 'ayushkapri.richard@gmail.com',
        'user_name': 'Ayush',
        'team_name': 'JARVIS',
        'room_number': 'PixelPod'
    },
    {
        'user_email': 'rajaarav272@gmail.com',
        'user_name': 'Aarav Raj',
        'team_name': 'Oxellus',
        'room_number': 'PixelPod'
    },
    {
        'user_email': 'dhruv16carter@gmail.com',
        'user_name': 'Dhruv Sharma',
        'team_name': 'Byte Bros',
        'room_number': 'PixelPod'
    },
    {
        'user_email': 'shivanibansal9928031918@gmail.com',
        'user_name': 'Shivani bansal',
        'team_name': 'TechWizards',
        'room_number': 'PixelPod'
    }
]

for user in users:
    send_codecraft_hackathon_invite_email(
        user_email=user["user_email"],
        user_name=user["user_name"],
        team_name=user["team_name"],
        room_number=user["room_number"]
    )
