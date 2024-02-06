from sqlalchemy import select, update
from models import Session, Job

from emails import EmailSender
from platsbanken import JobSearcher

#search new jerbs and persist to datebase
jerbs = JobSearcher('https://platsbanken-api.arbetsformedlingen.se/jobs/v1/search')
jerbs.persist_jerbs_to_db()
jerbs.get_unhandled_jerbs_from_db()

if jerbs.new_jerbs_count > 0:
    subject = f"{jerbs.new_jerbs_count}st nya Jobb!"
    print(subject)
    sender = EmailSender(subject, jerbs.html_ad_links).send_email()
    print(f"setting jobs as done in DB")
    jerbs.set_done_to_true_in_db()
else:
    print(f"{jerbs.new_jerbs_count} new jobs. No emails was sent.")
