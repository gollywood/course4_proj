from django.core.mail import mail_admins

@shared_task
def notify_of_new_search_term(search_term):
    mail_admins("New Search Term", f"A new search term was used: '{search_term}'")