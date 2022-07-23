from django.core.mail import EmailMessage



class Util:
    @staticmethod

    def send_mail(data):
        email=EmailMessage(
            subject=data['email_subject'],
            to_email=data['to_email'],
            body=data['email_body']
        )

        email.send()