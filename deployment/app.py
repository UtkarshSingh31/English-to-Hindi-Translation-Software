import gradio as gr
from transformers import MarianMTModel, MarianTokenizer

# Load YOUR fine-tuned model
print("Loading fine-tuned model...")
model_name = "utkarshsingh0013/enghind-translator
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Gradio interface
demo = gr.Interface(
    fn=translate,
    inputs=gr.Textbox(label="English Public Notice", placeholder="Enter English notice text..."),
    outputs=gr.Textbox(label="Hindi Translation"),
    title="Public Notice Translator (English → Hindi)",
    description="Translate formal English public notices to Hindi using fine-tuned MarianMT model",
    examples=[
        ["Notice: The office will remain closed on Republic Day."],
        ["All citizens are requested to submit their applications by January 15th."],
        ["This is to inform that the public hearing will be held on Monday."]
    ]
)

demo.launch()
