from fastapi import FastAPI 
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os 
from openai import OpenAI
from safety_rules import check_red_flags
from triage import classify_severity,severity_score
load_dotenv()

client = genai.configure(api_key=os.getenv("OPENAI_AI_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash") 

while True :
    userinput=input("you : ")
    if userinput.lower() == "exit":
        break 
    if len(userinput.split())<3:
        print("please give the detailed explanation")
        continue 
    is_emergency,symptom = check_red_flags(userinput)
    if(is_emergency):
        print(
            """severity:Emergency,\n
            response:Emergency! Go to hospical immediately,\n
            disclaimer:This AI cannot give medical advice for emergency cases\n
            """
        )
        continue 
    score=severity_score(userinput)
    severity=classify_severity(score)
    prompt=f"""  You are a medical triage assistant.
    Provide general health guidance only.
    Do not diagnose.
    Do not prescribe medicine.
    Always suggest consulting a doctor.
    patient message : {userinput}
    """
    response=model.generate_content(prompt)
    print(f"""
        severity:{severity} with score {score},\n
        response:{response.text},\n
        disclaimer:This AI provides general information only and is not a medical professional.\n
        """)

      