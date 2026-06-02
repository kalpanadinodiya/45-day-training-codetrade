# Student Profile Card

student = {
    "name": "Kalpana",
    "course": "BTech CSE",
    "city": "Hanumangarh",
    "skill": "Python"
}

def create_profile(profile: dict) -> str:
    return (
        f"Name   : {profile['name']}\n"
        f"Course : {profile['course']}\n"
        f"City   : {profile['city']}\n"
        f"Skill  : {profile['skill']}"
    )

print(create_profile(student))