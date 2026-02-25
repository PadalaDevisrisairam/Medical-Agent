
def classify_severity(symptoms_text):
    text=symptoms_text.lower()
    if "severe" in text or "very painful" in text :
        return "High"
    elif "Moderate" in text:
        return "Moderate"
    elif "mild" in text or "slight" in text:
        return "Low"
    else:
        return "Unknown"