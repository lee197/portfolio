import os
from python_http_client.exceptions import HTTPError

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailException(Exception):
    pass


def send_email(email):
    message = Mail(
        from_email='leebusiness197@gmail.com',
        to_emails='lee5187415@gmail.com',
        subject='Please confirm you email address',
        html_content='test content')
    message.template_id = os.environ.get('EMAIL_TEMPLATE_ID')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        return sg.send(message).status_code
    except HTTPError as e:
        print(e.to_dict)
        raise EmailException("Email can not send out")

    except Exception as e:
        print(e)
        raise EmailException("Email can not send out")
