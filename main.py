from flask import Flask, render_template

import config
from emails import EmailSender
from models import Job, Session
from platsbanken import JobTracker

app = Flask(__name__)


def searchJerbs():
    # search new jerbs and persist to datebase
    jerbs = JobTracker(config.occupation_fields, config.kommuner)

    if jerbs.new_jerbs_count > 0:
        # subject = f"{jerbs.new_jerbs_count}st nya Jobb!"
        # EmailSender(subject, jerbs.html_ad_links).send_email()
        print(f"setting jobs as done in DB")
        jerbs.set_done_to_true_in_db()
    else:
        print(f"{jerbs.new_jerbs_count} new jobs. No emails was sent.")


@app.route("/")
def hello():
    jerbs = JobTracker(config.occupation_fields, config.kommuner)
    results = jerbs.get_all_jerbs_from_db()
    job_list = [{"title": res.title, "id": res.id} for res in results]

    # Rendera mallen med jobbdata
    return render_template("index.html", jobs=job_list)


if __name__ == "__main__":
    searchJerbs()
    app.run(debug=True)
