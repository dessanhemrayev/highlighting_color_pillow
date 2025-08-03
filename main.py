from pillow_extension import text_highlighting_colors
import gradio as gr

from gradio.components import Textbox, Image, UploadButton, CheckboxGroup


def process_image_highlighting(
    size, image, font_file, position_str, text, align, text_color, highlighting_color
):
    """Wrapper function to handle Gradio inputs and call text_highlighting_colors."""
    try:
        # Validate inputs
        if not position_str or "," not in position_str:
            raise ValueError("Position must be in format 'x,y'")
        if not image:
            raise ValueError("Image is required")
        if not font_file:
            raise ValueError("Font file is required")

        # Convert position string to tuple
        x, y = map(int, position_str.split(","))
        position = (x, y)

        # Handle uploaded image and font files
        image_path = image if isinstance(image, str) else image.name
        font_path = font_file if isinstance(font_file, str) else font_file.name
        result_path = text_highlighting_colors(
            image_path,
            font_path,
            int(size),
            position,
            text,
            align[0] if align else "left",
            text_color,
            highlighting_color,
        )
        return result_path
    except Exception as e:
        raise gr.Error(f"Processing failed: {str(e)}")


app = gr.Interface(
    fn=process_image_highlighting,
    title="Extension for the Pillow library",
    inputs=[
        gr.Number(label="Font Size", value=100),
        Image(
            label="Image",
            format="jpg",
            type="filepath",
            sources=["upload", "webcam", "clipboard"],
        ),
        UploadButton(label="Font"),
        Textbox(
            label="Position (x,y)", value="1000,1000", placeholder="x,y coordinates"
        ),
        Textbox(label="Text", value="Hello\nworld\nPillow Python"),
        CheckboxGroup(
            label="Align", choices=["left", "center", "right"], value="center"
        ),
        gr.ColorPicker(label="Text Color", value="#FF1827"),
        gr.ColorPicker(label="Highlighting Color", value="#18D8FF"),
    ],
    outputs=["image"],
)


if __name__ == "__main__":
    app.launch()
