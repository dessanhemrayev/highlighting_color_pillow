from PIL import Image, ImageDraw, ImageFont


def text_highlighting_colors(
    image_src,
    font_src,
    size_font,
    position_text,
    text_origin,
    text_align,
    text_color,
    highlighting_color,
):
    """Highlight text in image.

    Args:
        image_src (str): Path to image.
        font_src (str): Path to font.
        size_font (int): Size of font.
        position_text (tuple): Position of text.
        text_origin (str): Text to highlight.
        text_align (str): Text alignment.
        text_color (tuple): Color of text.
        highlighting_color (tuple): Color of highlighting.

    """
    try:
        image = Image.open(image_src)
    except FileNotFoundError:
        print(f"Image file '{image_src}' not found.")
        return
    
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(font_src, size_font)
    except IOError:
        print(f"Font file '{font_src}' not found.")
        return
    y = 0 
    bbox = draw.textbbox(position_text, text_origin, font=font,align=text_align)
    xx,yy,x1 = bbox[0:3]
    text2 = text_origin.split('\n')
    for item in text2:
        font_width, _ = font.getsize(item)

        if text_align == 'right':
            left, top, right, bottom = draw.textbbox((x1-font_width,yy+y), item, font=font)
            draw.rectangle((left-5, top-5, right+5, bottom+5), fill=highlighting_color)
            draw.text((x1-font_width,yy+y), item, font=font, fill=text_color)
        elif text_align == 'center':
            left, top, right, bottom = draw.textbbox((xx/2-font_width/2+x1/2,yy+y), item, font=font)
            draw.rectangle((left-5, top-5, right+5, bottom+5), fill=highlighting_color)
            draw.text((xx/2-font_width/2+x1/2,yy+y), item, font=font, fill=text_color)
        else:
            left, top, right, bottom = draw.textbbox((xx,yy+y), item, font=font)
            draw.rectangle((left-5, top-5, right+5, bottom+5), fill=highlighting_color)
            draw.text((xx,yy+y), item, font=font, fill=text_color)
        y += size_font
    image.save("image_highlighting_colors.png")


if __name__ == "__main__":
    size = 100
    image = "tnc_48980557.jpg"
    font = "Lobster-Regular.ttf"
    position = (1000, 1000)
    text = "Hello\nworld\nPillow Python"
    align = "center"
    text_color = "#FF1827"
    highlighting_color = "#18D8FF"
    text_highlighting_colors(
        image, font, size, position, text, align, text_color, highlighting_color
    )
