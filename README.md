# Enterprise-Grade-To-Sure! Here's a polished and clear README.md file for your AI-powered transcript parser web app project:


# AI-Powered Transcript Task Parser

An AI-powered web application that extracts actionable tasks from meeting transcripts. Users can paste entire meeting conversations, and the app automatically extracts tasks with assignees, deadlines, and priorities, displaying them in an intuitive, visually appealing task board.

---

## Features

- **Automatic Task Extraction**  
  Parses meeting transcripts to identify task descriptions, assigned persons, deadlines, and priority levels.

- **Smart Deadline Parsing**  
  Converts natural language deadlines (e.g., "tonight", "Wednesday", "10pm tomorrow") into standardized date-time formats.

- **Default Priority & Priority Badges**  
  Assigns default priority P3 unless specified otherwise, with color-coded badges (P1-red, P2-orange, P3-green).

- **Multiple View Modes**  
  Toggle between clean card view and table view for tasks.

- **Responsive UI**  
  Works seamlessly on both desktop and mobile devices.

- **Easy-to-use Interface**  
  Simple input box to paste transcripts and generate tasks with one click.

---

## Demo Screenshot

![Screenshot](docs/screenshot.png)  
*Example of task cards generated from a meeting transcript.*

---

## Getting Started

### Prerequisites

- [Streamlit](https://anjani1598-enterprise-grade-to-do-list-main-o4ysgc.streamlit.app/)
- Google Gemini API key (for AI model access)
- `pip` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-transcript-task-parser.git
   cd ai-transcript-task-parser
````

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API key:

   ```
   API_KEY=your_google_gemini_api_key_here
   ```

---

## Running the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## Usage

1. Paste a meeting transcript into the input box, e.g.:

   ```
   Aman you take the landing page by 10pm tomorrow. Rajeev you take care of client follow-up by Wednesday. Shreya please review the marketing deck tonight.
   ```

2. Click **Generate Tasks**.

3. View extracted tasks with assignee, due date/time, and priority.

4. Switch between **Card View** and **Table View** using the radio buttons.

---

## Code Structure

* `app.py` - Main Streamlit application file.
* `requirements.txt` - Python dependencies.
* `docs/` - Project documentation and screenshots.
* `.env` - Environment variables (API keys).

---

