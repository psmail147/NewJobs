from bs4 import BeautifulSoup
from utils import get_driver
import time
class JobInfo:
        def __init__(self, job_listings_container, job_entry_selector,
                     profile_path, profile_name, driver_path, base_url):

            self.job_listings_container = job_listings_container
            self.job_entry_selector = job_entry_selector
            self.driver = get_driver(profile_path, profile_name, driver_path)
            self.base_url = base_url

        def get_job_information(self,job_listings, base_url):
            job_information = []
            for job in job_listings:
                job_title = job.find("a", class_="jcs-JobTitle css-1baag51 eu4oa1w0")
                company = job.find("span", class_="css-1h7lukg eu4oa1w0")
                short_description = job.find("div", class_="underShelfFooter")
                if job_title is not None and short_description is not None and job.find("a"):
                    job_information.append({"id": job.find("a")["id"], "title": job_title.text.strip(),
                                            "company": company.text.strip(),
                                            "short_description": short_description.text.strip(),
                                            "link": base_url + job.find("a")["href"]})
            return job_information

        def run_it(self, URL):
            self.driver.get(URL)
            time.sleep(5)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find("div", class_=self.job_listings_container)
            job_listings = results.find_all("li", class_=self.job_entry_selector)
            job_information = self.get_job_information(job_listings, self.base_url)
            return job_information

