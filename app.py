import gradio as gr
from transformers import MarianMTModel, MarianTokenizer

tokenizer = None
model = None
model_name="utkarshsingh0013/enghind-translator"

def load_model():
    global tokenizer, model
    if tokenizer is None or model is None:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        model.eval()

def translate(text):
    load_model()
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Gradio interface
demo = gr.Interface(
    fn=translate,
    inputs=gr.Textbox(label="English Public Notice", placeholder="Enter English notice text..."),
    outputs=gr.Textbox(label="Hindi Translation"),
    title="Public Notice Translator (English → Hindi) [AUTO-DEPLOYED]",
    description="Translate formal English public notices to Hindi using fine-tuned MarianMT model",
    examples=[
        ["Notice: The office will remain closed on Republic Day."],
        ["All citizens are requested to submit their applications by January 15th."],
        ["This is to inform that the public hearing will be held on Monday."]
    ]
)

demo.launch(server_name="0.0.0.0", server_port=7860)
