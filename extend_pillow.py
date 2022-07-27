from PIL import Image, ImageDraw, ImageFont

def text_highlighting_colors(image_src,font_src,size_font,position_text,text_origin,text_align,text_color,highlighting_color):
    
    image = Image.open(image_src)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_src, size_font)
    position = position_text
    align = text_align
    y = 0 
    text = text_origin
    bbox = draw.textbbox(position, text, font=font,align=text_align)
    xx,yy,x1 = bbox[0:3]
    text2 = text.split('\n')
    for item in text2:
        font = ImageFont.truetype("Lobster-Regular.ttf", size_font)
        font_width, font_height = font.getsize(item)

        if align == 'right':
            left, top, right, bottom = draw.textbbox((x1-font_width,yy+y), item, font=font)
            draw.rectangle((left-5, top-5, right+5, bottom+5), fill=highlighting_color)
            draw.text((x1-font_width,yy+y), item, font=font, fill=text_color)
        elif align == 'center':
            left, top, right, bottom = draw.textbbox((xx/2-font_width/2+x1/2,yy+y), item, font=font)
            draw.rectangle((left-5, top-5, right+5, bottom+5), fill=highlighting_color)
            draw.text((xx/2-font_width/2+x1/2,yy+y), item, font=font, fill=text_color)
        else:
            left, top, right, bottom = draw.textbbox((xx,yy+y), item, font=font)
            print(left, top, right, bottom)
            draw.rectangle((left-5, top-5, right+5, bottom+5), fill=highlighting_color)
            draw.text((xx,yy+y), item, font=font, fill=text_color)
        y += size_font

    image.show()

size = 100
image = 'tnc_48980557.jpg'
font = "Lobster-Regular.ttf"
position = (1000, 1000)
text = "Hello\nworld\nPillow Python"
align = 'center'
text_color = "#FF1827"
highlighting_color = "#18D8FF"
text_highlighting_colors(image,font,size,position,text,align,text_color,highlighting_color)