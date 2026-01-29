# AI Debate System

An AI debate system built using **Crew AI** and multiple LLMs. Users input a topic, and the system generates structured arguments and counter-arguments using AI agents.

---

## Features

- Multi-agent debate simulation
- Supports multiple LLMs
- Easy local setup and execution
- Optional API and live demo via ngrok

---

## Project Structure

```
crewai/
├── debate/
│   ├── src/
│   └── main.py        # Entry point for Crew AI debate
├── requirements.txt
└── README.md
```
> **Note:** `.venv` is created locally and ignored in the repo.

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Divya-256/AI_Debate_System.git
   cd AI_Debate_System
   ```

2. **Create a Python virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Linux / Mac
   # OR
   .venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file and add:
   ```ini
   OPENAI_API_KEY=<your_openai_key>
   MODEL=<your openai model name>
   ```
   Replace with your actual keys.

---

## Running the Debate System Locally

Run the main Crew AI script:
```bash
python debate/src/debate/main.py
```
Provide a debate topic when prompted. The AI agents will generate arguments.

---

## Optional: Run as API with FastAPI

You can wrap the system in an API for integration or live demo:

```python
# app.py
from fastapi import FastAPI
from debate.src.debate.main import run

app = FastAPI()

@app.get("/debate")
def debate(topic: str = "AI ethics"):
    inputs = {"topic": topic}
    result = run(inputs)
    return result
```

Run the server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## Testing the API

### Local Testing

1. **Start the FastAPI server**
   ```bash
   cd /path/to/your/project
   python3 -m uvicorn app:app --host 0.0.0.0 --port 8000
   ```

2. **Test with curl**
   ```bash
   curl "http://localhost:8000/debate?topic=Should%20AI%20replace%20human%20teachers"
   ```

3. **Test with browser**
   Open: `http://localhost:8000/debate?topic=AI%20ethics`

4. **Interactive API docs**
   Visit: `http://localhost:8000/docs` for Swagger UI

5. **Test with Postman**
   - Method: GET
   - URL: `http://localhost:8000/debate`
   - Add query parameter: `topic` = `Should AI replace human teachers`

### Public Testing with ngrok

1. **Sign up for ngrok** (one-time setup)
   - Go to: https://dashboard.ngrok.com/signup
   - Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken

2. **Configure ngrok**
   ```bash
   ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
   ```

3. **Start your FastAPI server** (keep running)
   ```bash
   python3 -m uvicorn app:app --host 0.0.0.0 --port 8000
   ```

4. **In a new terminal, start ngrok**
   ```bash
   ngrok http 8000
   ```

5. **Copy the public URL** from ngrok output
   Look for the "Forwarding" line:
   ```
   Forwarding    https://abc123-def456.ngrok-free.app -> http://localhost:8000
   ```

6. **Test with the public URL**
   ```bash
   curl "https://abc123-def456.ngrok-free.app/debate?topic=Should%20AI%20replace%20human%20teachers"
   ```

   Or in Postman:
   - URL: `https://abc123-def456.ngrok-free.app/debate?topic=AI%20ethics`

**Note:** Replace `abc123-def456.ngrok-free.app` with your actual ngrok URL.

---

## Sample Usage

Run locally:
```bash
python debate/src/debate/main.py
```
Example input:
```
Topic: Should AI replace human teachers?
```
Example output:
```
Pro Argument: AI can personalize learning experiences for each student...
Con Argument: Human teachers provide empathy and understanding that AI cannot replicate...
```

Or via API:
```bash
curl "https://<your-ngrok-id>.ngrok.io/debate?topic=AI+ethics"
```

---

## Support & Resources

- [crewAI Documentation](https://docs.crewai.com)
- [GitHub Issues](https://github.com/joaomdmoura/crewai/issues)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [Interactive Docs Chat](https://chatg.pt/DWjSBZn)
