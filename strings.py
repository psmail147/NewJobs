
def get_strings():
    names = []
    with open("strings.txt", "r") as file:
        for line in file:
            names.append(line)

    URL = names[0].strip().replace('"', "")
    profile_path = names[1].strip().replace('"', '')
    profile_name = names[2].replace('"', "").strip().replace('"', "")
    driver_path = names[3].replace('"', "").strip().replace('"', "")
    base_url = names[4].replace('"', "").strip().replace('"', "")
    indeed_jobcards_parent = names[5].replace('"', "").strip().replace('"', "")
    indeed_jobcards = names[6].replace('"', "").strip().replace('"', "")
    return URL, profile_path, profile_name, driver_path, base_url, indeed_jobcards_parent, indeed_jobcards

#URL, profile_path, profile_name, driver_path, base_url, indeed_jobcards_parent, indeed_jobcards = get_strings()

