from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
import os
from django.conf import settings

def send_thank_you_email(user_email, user_name, event_name, event_date, event_location, event_url, instagram_url, whatsapp_url, calendar_url):
    subject = f"Thank You for Registering for {event_name}"
    context = {
        "user_name": user_name,
        "event_name": event_name,
        "event_date": event_date,
        "event_location": event_location,
        "event_url": event_url,
        "instagram_url": instagram_url,
        "whatsapp_url": whatsapp_url,
        "calendar_url": calendar_url,
    }
    html_content = render_to_string("thank_you_email.html", context)
    text_content = f"Thank you {user_name} for registering for {event_name}."

    email = EmailMultiAlternatives(subject, text_content, None, [user_email])
    email.attach_alternative(html_content, "text/html")

    image_path = os.path.join("email_app", "templates", "invite.jpg")
    with open(image_path, 'rb') as img:
        image = MIMEImage(img.read())
        image.add_header('Content-ID', '<invite_image>')
        image.add_header('Content-Disposition', 'inline', filename="invite.jpeg")
        email.attach(image)

    email.send()
    print(f"[✓] Email sent to {user_name} <{user_email}>")


def send_codecraft_invite_email(user_email, user_name):
    subject = "🚨 CodeCraft – Kitna Reels Dekhoge?"
    text_content = f"Hey {user_name}, don't miss CodeCraft at GEHU Bhimtal!"

    context = {
        "user_name": user_name
    }

    html_content = render_to_string("codecraft_invite.html", context)

    email = EmailMultiAlternatives(subject, text_content, None, [user_email])
    email.attach_alternative(html_content, "text/html")

    image_path = os.path.join("email_app", "templates", "invite.jpg")  # use same image if applicable
    if os.path.exists(image_path):
        with open(image_path, "rb") as img:
            image = MIMEImage(img.read())
            image.add_header("Content-ID", "<invite_image>")
            image.add_header("Content-Disposition", "inline", filename="invite.jpg")
            email.attach(image)

    email.send()
    print(f"[✓] Invite sent to {user_name} <{user_email}>")
