from requests import Response, post
import os
from typing import List


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message

class Mailgun:
    FROM_TITLE = "Pricing service"
    FROM_EMAIL = "do-not-reply@sandboxb8c013023c024ac7aaab16b8dfbfb35d.mailgun.org"
    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        # TODO load api_key and domain from os.environ can get tricky
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)
        if api_key is None:
            raise MailgunException("Failed to load Mailgun API key.")
        if domain is None:
            raise MailgunException("Failed to load Mailgun domain.")
        response = post(
            f"{domain}/messages",
            auth=("api", api_key),
            data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                  "to": email,
                  "subject": subject,
                  "text": text,
                  "html": html})
        if response.status_code != 200:
            # TODO remove this later
            print(response.json())
            raise MailgunException('An error occurred while sending e-mail')
        return response



