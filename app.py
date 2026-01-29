import gradio as gr

def debate(topic):
    return f"Debate on: {topic}"

demo = gr.Interface(
    fn=debate,
    inputs=gr.Textbox(label="Debate Topic"),
    outputs=gr.Textbox(label="AI Debate Output"),
    title="AI Debate System"
)

if __name__ == "__main__":
    demo.launch()
