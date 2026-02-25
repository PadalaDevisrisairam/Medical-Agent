severity_scores={
    "fever" : 2,
    "cough" : 2,
    "headache" : 2,
    "back pain" : 3,
    "vomiting" : 3,
    "diarrhea" : 4,
    "motions" : 4
}

def severity_score(symptoms_text):
    score=0
    for symptom,score in severity_scores.items():
        if symptom in symptoms_text.lower():
            score+=score
    return score
def classify_severity(score):
    if(score > 10):
        return "High"
    elif(score>5):
        return "Moderate"
    else:
        return "Low"
   