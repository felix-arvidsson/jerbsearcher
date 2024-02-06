from datetime import datetime
import json
import requests

from models import Session, Job
from sqlalchemy import select, update

import config


class JobSearcher:
    def __init__(self, url):
        self.url = url
        self.new_jerbs_count = 0
        self.html_ad_links = ""

    def search_jerb(self):
        #create datetime string with this format "2024-02-06T12:46:05.060Z".
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'INT_SYS': 'platsbanken_web_beta',
            'Content-Type': 'application/json',
            'Origin': 'https://arbetsformedlingen.se',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://arbetsformedlingen.se/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        data = {
            "filters": [
                {"type": "occupationField", "value": config.occupation_field},
                {"type": "municipality", "value": config.kommun}
            ],
            "fromDate": None,
            "order": "relevance",
            "maxRecords":  100,
            "startIndex":  0,
            "toDate": current_time,
            "source": "pb"
        }
        response = requests.post(self.url, headers=headers, data=json.dumps(data))
        return response.json()["ads"]    

    def persist_jerbs_to_db(self):
        session = Session()
        for job in self.search_jerb():
            try:
                new_job = Job(id=job["id"], title=job["title"], publishedDate=job['publishedDate'], email_sent=False)
                session.add(new_job)
                session.commit()
            except Exception as e:
                pass
        session.close()

    def get_unhandled_jerbs_from_db(self):
        session = Session()
        query = select(Job).where(Job.email_sent == False)
        
        ad_links = ""
        for row in session.execute(query):
            ad_links += f"<a href='https://arbetsformedlingen.se/platsbanken/annonser/{row[0].id}'>{row[0].title}</a><br />"
            self.new_jerbs_count += 1

        self.html_ad_links = f"""
            <html>
              <body>
                {ad_links}
              </body>
            </html>
        """
        session.close()

    def set_done_to_true_in_db(self):
        session = Session()
        try:
            print("marking stuff as done in DB..")
            stmt = update(Job).where(Job.email_sent == False).values(email_sent=True)
            session.execute(stmt)
            session.commit()
        except Exception as e:
            print(e)
        finally:
            session.close()
