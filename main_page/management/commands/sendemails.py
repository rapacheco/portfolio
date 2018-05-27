from django.core.management.base import BaseCommand, CommandError
from django.core.mail import mail_admins

from smtplib import SMTPException

from main_page.models import Message

class Command(BaseCommand):
    help = 'Sends a report with all the msgs sent in the contact.html form'

    def handle(self, *args, **options):
        msgs = Message.objects.filter(sent=False)
        mail = ""

        if len(msgs) == 0:
            mail += "No messages received today"
        else:
            for msg in msgs:
                #self.stdout.write(msg.msg)
                mail += msg.name + '\n' + msg.email + '\n' + msg.msg + '\n' + str(msg.date) + '\n\n'

        try:
            # mail_admins(
            #     'Emails received today',
            #     mail,
            #     fail_silently=False,
            # )
            self.stdout.write(mail)
        except SMTPException:
            raise CommandError("Unable to send email")
        else:
            for msg in msgs:
                msg.sent = True
                msg.save()
