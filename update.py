import csv
class Update:
    def __init__(self):
        self.database = []

    def open_database(self):
        with open('jobs.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            reader = list(reader)
            for row in reader[1:]:
                self.database.append(row)

    def get_new_jobs(self, listings):
        new_jobs = []
        flag = False
        for i in range(len(listings)):
            for j in range(len(self.database)):
                if listings[i]['id'] == self.database[j][0] and listings[i]['company'] == self.database[j][2]: # and company is not same
                    flag = True
                    break
                else:
                    flag = False
            if flag == False:
                new_jobs.append(listings[i])
        return new_jobs

    def save_new_jobs(self, new_jobs):
        new_jobs = self.get_new_jobs(new_jobs)
        if not new_jobs:
            print("No new jobs")
        else:
            print(f"number of new jobs: {len(new_jobs)}")
            for job in new_jobs:
                print(job)
            with open("jobs.csv", "a", newline="\n", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["id", "title", "company"])
                for job in new_jobs:
                    writer.writerow({"id": job["id"], "title": job["title"], "company": job["company"]})

    def run(self, job_information):
        self.open_database()
        new_jobs = self.get_new_jobs(job_information)
        self.save_new_jobs(new_jobs)