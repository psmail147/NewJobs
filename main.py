from jobinfo import JobInfo
from strings import get_strings
from update import Update

URL, profile_path, profile_name, driver_path, base_url, indeed_jobcards_parent, indeed_jobcards = get_strings()
test = JobInfo(indeed_jobcards_parent, indeed_jobcards, profile_path, profile_name, driver_path, base_url)

job_information = test.run_it(URL)

test = Update()
test.run(job_information)