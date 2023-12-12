from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging

from api.settings import _env_get_required

logger = logging.getLogger(__name__)

# How to use this function:
# add all args to provide clarity on what is needed
# subject, template, send_from, send_to, context={}, bcc_emails=[]
# subject and template are stored in the templates folder
# create a new folder to keep all email templates organized

# Ex:
# send_html_email(
#     subject=login_subject,
#     template="auth/login_email.html",
#     send_from=_env_get_required("REWYRE_SUPPORT_EMAIL"),
#     send_to=[context["email"]],
#     context=context,
# )


def send_html_email(subject, template, send_from, send_to, context={}, bcc_emails=[]):
    """Generic sender to build and send an HTML email with a plain-text fallback.
    Args:
        subject (str): Subject of the email.
        template (str): Path to the HTML template to use for this email. Use the Django
            template loader path.
        send_from (str): The email address of the sender.
        send_to (str or list of str): Email address(es) of recipients.
        context (dict, optional): Dictionary of context variables needed to render
            the HTML template. Defaults to an empty :obj:`dict`.
        bcc_emails (list of str, optional): List of email addresses to BCC
            on the email. Defaults to an empty :obj:`list`.
    Returns: None
    """
    assert isinstance(
        send_to, (list, tuple, str)
    ), "send_to must be an instance of list, tuple, or str"

    if isinstance(send_to, str):
        send_to = [send_to]

    # Email subject *must not* contain newlines
    subject = "".join(subject.splitlines())

    # Render HTML and use premailer transform to force inline CSS
    html_body = render_to_string(template, context)

    plaintext_body = (
        "This is an HTML email. If you can read this, then "
        "your email client does not support HTML emails. "
        "Please contact us at {0} to report the problem.".format(settings.SERVER_EMAIL)
    )

    email = EmailMultiAlternatives(
        subject,
        plaintext_body,
        send_from,
        send_to,
        bcc_emails,
    )

    email.attach_alternative(html_body, "text/html")
    email.send(fail_silently=False)


# send an automated email to the references when a user signs up
# WIP
def send_reference_email(context):
    print(f"context in send_reference_email => {context}")
    subject_context = {
        "environment": settings.ENVIRONMENT.upper(),
        "user_email": context["email"],
        "reference_first_name": context["reference_first_name"],
        "user_first_name": context["user_first_name"],
    }
    reference_subject = render_to_string("auth/reference_subject.txt", subject_context)
    send_html_email(
        subject=reference_subject,
        template="auth/reference_email.html",
        send_from=_env_get_required("REFERENCE_EMAIL"),
        send_to=[context["email"]],
        context=context,
        bcc_emails=[_env_get_required("REFERENCE_EMAIL")],
    )


# WIP
# send intro email from leaderboard cta
# user (company) sends an intro to the
def send_intro_email(context):
    print(f"context in send_intro_email => {context}")
    subject_context = {
        "environment": settings.ENVIRONMENT.upper(),
        "user_first_name": context["user_first_name"],
        "user_last_name": context["user_last_name"],
    }
    intro_subject = render_to_string("intro/intro_subject.txt", subject_context)
    send_html_email(
        subject=intro_subject,
        template="intro/intro_email.html",
        send_from=_env_get_required("INTRO_EMAIL"),
        send_to=[context["email"]],
        context=context,
        bcc_emails=[_env_get_required("INTRO_EMAIL")],
    )


# def send_user_login_email(context):
#     print(f"context in send_user_login_email => {context}")
#     # Send email to Rewyre Admin notyfing that seller is not set up
#     subject_context = {
#         "environment": settings.ENVIRONMENT.upper(),
#         "user_email": context["email"],
#     }
#     login_subject = render_to_string("auth/login_subject.txt", subject_context)
#     send_html_email(
#         subject=login_subject,
#         template="auth/login_email.html",
#         send_from=_env_get_required("SUPPORT_EMAIL"),
#         send_to=[context["email"]],
#         context=context,
#     )
