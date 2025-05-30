from datetime import timedelta,datetime

from google import genai
from pydantic import BaseModel,ValidationError
from dotenv import load_dotenv
import os
import streamlit as st
import enum
import json



load_dotenv()
api_key = os.getenv('API_KEY')

current_date = datetime.now().strftime("%Y-%m-%d")



class Priority(enum.Enum):
  P1 = "P1"
  P2 = "P2"
  P3 = "P3"

  class Config:
      use_enum_values = True

class Recipe(BaseModel):
    task: str
    assigned_to: str
    due_date_time: datetime
    priority: Priority

client = genai.Client(api_key=api_key)

# Use the response as a JSON string.
# print(response.text)

# Use instantiated objects.


st.title("🧠 AI Task Generator with Gemini")

st.markdown("""
    <style>
    div.stButton > button {
        padding: 0.25rem 0.75rem;
        font-size: 0.85rem;
        height: 2.2rem;
        line-height: 1;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)
col1, col2 = st.columns([5, 1])  # Wider input, narrower button

with col1:
    user_input = st.text_area("Enter task description prompt", "", height=73)

with col2:
    st.write("")  # Add spacing
    st.write("")# More spacing
    st.write("")# More spacing

    generate_clicked = st.button("Generate Tasks.")



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

view_mode = st.radio("Select View Mode", ["Card View", "Table View"], horizontal=True)


def format_due_date(dt: datetime) -> str:
    now = datetime.now()
    date_only = dt.date()
    now_date = now.date()

    # Identify relative day
    if date_only == now_date:
        day_label = "Today"
    elif date_only == now_date + timedelta(days=1):
        day_label = "Tomorrow"
    else:
        day_label = dt.strftime("%A")  # e.g., Wednesday

    time_str = dt.strftime("%I:%M %p")  # e.g., 09:00 AM
    date_str = dt.strftime("%B %d, %Y")  # e.g., June 04, 2025

    return f"{time_str}, {day_label}, {date_str}"

def get_priority_badge(priority: str) -> str:
    colors = {"P1": "#FF4B4B", "P2": "#FFA500", "P3": "#21BA45"}
    return f"<span style='background-color:{colors.get(priority, '#AAA')}; color:white; padding:4px 8px; border-radius:8px;'>{priority}</span>"


if generate_clicked:
    if not user_input.strip():
        st.warning("Please enter a task prompt.")
    else:
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=enhanced_prompt,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': list[Recipe],
                },
            )

            raw_tasks = json.loads(response.text)
            task_list = []

            for i, task_json in enumerate(raw_tasks, start=1):
                try:
                    # Fallback to default priority if not provided
                    if 'priority' not in task_json:
                        task_json['priority'] = 'P3'
                    recipe = Recipe(**task_json)

                    task_list.append({
                        "Task": recipe.task,
                        "Assigned To": recipe.assigned_to,
                        "Due Date": format_due_date(recipe.due_date_time),
                        "Priority": recipe.priority.value
                    })
                except ValidationError as e:
                    st.error(f"Validation error in task {i}: {e}")

            # Store the data in session state
            st.session_state["task_data"] = task_list

        except Exception as e:
            st.error(f"Error: {e}")

# Render tasks from session state if available
if "task_data" in st.session_state:
    task_data = st.session_state["task_data"]

    if view_mode == "Table View":
        st.dataframe(task_data, use_container_width=True)
    else:
        for task in task_data:
            st.markdown(f"""
                <div style="background-color:#1E1E1E; padding:15px; border-radius:12px; margin-bottom:10px; box-shadow:0 2px 6px rgba(0,0,0,0.2);">
                    <h4 style="margin-bottom:5px;">📝 {task['Task']}</h4>
                    <p><strong>Assigned To:</strong> {task['Assigned To']}</p>
                    <p><strong>Due Date:</strong> {task['Due Date']}</p>
                    <p><strong>Priority:</strong> {get_priority_badge(task['Priority'])}</p>
                </div>
            """, unsafe_allow_html=True)


