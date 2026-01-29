import sys
import os
from fastapi import FastAPI, Query
from dotenv import load_dotenv

# Load environment variables from debate/.env
load_dotenv(os.path.join(os.path.dirname(__file__), "debate", ".env"))

# Fix sys.path so that "debate" is importable as a package
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBATE_SRC = os.path.join(BASE_DIR, "debate", "src")
if DEBATE_SRC not in sys.path:
    sys.path.insert(0, DEBATE_SRC)

from debate.crew import Debate

app = FastAPI()

@app.get("/debate")
def debate(topic: str = Query("AI ethics", description="Debate topic")):
    try:
        inputs = {"motion": topic}
        result = Debate().crew().kickoff(inputs=inputs)
        return {"topic": topic, "result": result.raw}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}", "topic": topic}

# To test your FastAPI app:
#
# 1. **Start the server**
#    In your project root, run:
#    ```bash
#    uvicorn app:app --host 0.0.0.0 --port 8000
#    ```
#
# 2. **Open your browser**
#    Go to:
#    [http://localhost:8000/debate?topic=AI%20ethics](http://localhost:8000/debate?topic=AI%20ethics)
#    You should see a JSON response with the debate result.
#
# 3. **Try with curl**
#    ```bash
#    curl "http://localhost:8000/debate?topic=Should%20AI%20replace%20human%20teachers"
#    ```
#
# 4. **Interactive docs**
#    Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI and test the endpoint interactively.
#
# If you want to demo it publicly, use ngrok:
# ```bash
# ngrok http 8000
# ```
# and use the public URL provided by ngrok.
