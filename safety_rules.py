RED_FLAG_SYMPTOMS = [
    "chest pain",
    "difficulty breathing",
    "severe bleeding",
    "loss of consciousness",
    "stroke symptoms",
    "seizure",
    "suicidal thoughts"
]

def check_red_flags(user_input):
    for symptom in RED_FLAG_SYMPTOMS:
        if symptom in user_input.lower():
            return True, symptom
    return False, None