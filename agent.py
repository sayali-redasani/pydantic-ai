from pydantic import BaseModel
from pydantic_ai import Agent
from langchain_cohere import ChatCohere
from pydantic_ai.models.openai import OpenAIModel
# from pydantic_ai.models.mistral import MistralModel

class Patient(BaseModel):
    # name, gender, age, weight, height, BMI, and chief medical
    name: str
    gender: str
    age:int
    weight:float
    height:float
    BMI:float
    chief_medical_complaint: str

# openai gave accurate result --> tested
model = OpenAIModel('gpt-4o')

system_prompt = """
You are tasked with extracting patient information from the input text. The patient details you need to extract are as follows:
- Name: Full name of the patient.
- Gender: Identify the gender based on the context (pronouns like he/she, or gendered names such as Emily, etc.).
- Age: Patient’s age in years.
- Weight: Patient's weight in pounds or kilograms.
- Height: Patient's height in inches or centimeters.
- BMI: Patient's Body Mass Index (BMI).
- Chief Medical Complaint: A short description of the patient's primary medical concern or symptoms.

If any information is not provided or is unclear in the text, leave the corresponding field blank. Avoid hallucinating details and ensure accuracy. If a patient's gender is not explicitly stated, try to infer it from context or name. In case of ambiguity, leave it blank.

Extract the following values from the input below and return them in a structured format:

"""
     
agent = Agent(model, result_type=Patient, system_prompt=system_prompt)

result = agent.run_sync("""Karen L. Thompson, a 38-year-old female, is 5'4" (64 inches) tall and weighs 162
lbs. She has a history of irritable bowel syndrome (IBS) and recurrent migraines, both of
which have intensified over the past year. Karen also experiences chronic fatigue and joint
pain, leading her physician to investigate possible early-stage rheumatoid arthritis. She
reports frequent episodes of dizziness and occasional heart palpitations, which have been
attributed to mild anemia and elevated stress levels. Karen’s symptoms are exacerbated by
her demanding job as a paralegal, where long hours and poor posture have contributed to
persistent neck and shoulder tension. Recently, she has begun experiencing intermittent
insomnia, further impacting her energy levels and overall well-being.""")

print(f"This is sample 3 -  {result.data}")

# Patient type
print(type(result.data))