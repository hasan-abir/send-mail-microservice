from celery import shared_task
from django.core.mail import send_mail

@shared_task
def sendmail_task(email_data):
    recipient = email_data['recipient']
    subject = email_data['subject']
    msg_content = email_data['msg_content']

    return send_mail(
        subject,
        msg_content,
        "hasan@test.com",
        [recipient],
        fail_silently=False,
    )

