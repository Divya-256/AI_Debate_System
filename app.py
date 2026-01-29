import gradio as gr
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fix sys.path for debate package
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBATE_SRC = os.path.join(BASE_DIR, "debate", "src")
if DEBATE_SRC not in sys.path:
    sys.path.insert(0, DEBATE_SRC)

from debate.crew import Debate

def run_debate(topic):
    if not topic.strip():
        return "Please enter a debate topic."
    
    try:
        inputs = {"motion": topic}
        result = Debate().crew().kickoff(inputs=inputs)
        return result.raw
    except Exception as e:
        return f"Error: {str(e)}"

# Create interface
with gr.Blocks(title="AI Debate System", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🤖 AI Debate System
    
    **Multi-agent AI system using CrewAI that generates structured debates on any topic.**
    
    Enter a debate topic and watch AI agents present arguments from both sides!
    """)
    
    topic_input = gr.Textbox(
        label="Debate Topic",
        placeholder="Enter your debate topic here...",
        value="Should AI replace human teachers?",
        lines=2
    )
    
    submit_btn = gr.Button("🎯 Start Debate", variant="primary")
    
    output = gr.Textbox(
        label="Debate Results",
        lines=12,
        show_copy_button=True,
        placeholder="Debate results will appear here..."
    )
    
    submit_btn.click(
        fn=run_debate,
        inputs=topic_input,
        outputs=output,
        show_progress=True
    )
    
    gr.Examples(
        examples=[
            ["Should AI replace human teachers?"],
            ["Is remote work better than office work?"],
            ["Should social media be regulated?"],
            ["Is nuclear energy the future?"]
        ],
        inputs=topic_input,
        outputs=output,
        fn=run_debate
    )
    
    gr.Markdown("""
    ---
    ### 🔧 Tech Stack: Python • CrewAI • Gradio • LLMs • Multi-Agent Systems
    
    [View Source Code](https://github.com/Divya-256/AI_Debate_System)
    """)

if __name__ == "__main__":
    demo.launch()
