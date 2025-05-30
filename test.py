import datetime

from google import genai
from pydantic import BaseModel,ValidationError
from dotenv import load_dotenv
import os
import streamlit as st
import enum
import json



load_dotenv()
api_key = os.getenv('API_KEY')

current_date = datetime.datetime.now().strftime("%Y-%m-%d")


class Priority(enum.Enum):
  P1 = "P1"
  P2 = "P2"
  P3 = "P3"

  class Config:
      use_enum_values = True

class Recipe(BaseModel):
    task: str
    assigned_to: str
    due_date_time: datetime.datetime
    priority: Priority

client = genai.Client(api_key=api_key)

user_input = input("Enter task description prompt: ")

enhanced_prompt = f"""
Today is {current_date}.

You are a task planner. Extract tasks from the following input.

For each task, provide:
- task: description of the task
- assigned_to: person's name responsible
- due_date_time: convert natural deadline into ISO 8601 format (assume current year if not mentioned)
- priority: P1 (high urgency), P2 (medium), P3 (low/default). If no urgency is mentioned, use P3.

Input: {user_input}
Return output in JSON array format.
"""
response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=enhanced_prompt,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': list[Recipe],
                },
            )

print(response.text)