from pillow_extension import text_highlighting_colors
import gradio as gr
from gradio.components import Textbox, Image, UploadButton, ColorPicker



app = gr.Interface(
    fn=text_highlighting_colors,
    title="Hello",
    inputs=[
        Textbox(label="Size"),
        Image(label="Image", format="jpg", sources=["upload", "webcam", "clipboard"]),
        UploadButton(label="Font"),
        Textbox(label="Position"),
        Textbox(label="Text"),
        Textbox(label="Align"),
        ColorPicker(label="Text Color"),
        ColorPicker(label="Highlighting Color"),
    ],
    outputs=["image"],
)



if __name__ == "__main__":
    size = 100
    image = "tnc_48980557.jpg"
    font = "Lobster-Regular.ttf"
    position = (1000, 1000)
    text = "Hello\nworld\nPillow Python"
    align = "center"
    text_color = "#FF1827"
    highlighting_color = "#18D8FF"
    

    app.launch()
