from fastapi import FastAPI 
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os 
from openai import OpenAI
from safety_rules import check_red_flags
from triage import classify_severity
load_dotenv()
app=FastAPI()
client = genai.configure(api_key=os.getenv("OPENAI_AI_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash") 
class RequestBody(BaseModel):
    message:str
@app.post("/triage")
def medical_agent(body:RequestBody):
    is_emergency,symptom = check_red_flags(body.message)
    if(is_emergency):
        return {"response":"Emergency! Go to hospical immediately"}
    severity=classify_severity(body.message)
    prompt=f"""  You are a medical triage assistant.
    Provide general health guidance only.
    Do not diagnose.
    Do not prescribe medicine.
    Always suggest consulting a doctor.
    patient message : {body.message}
    """
    response=model.generate_content(prompt)
    return response.text

      