from PIL import Image
from unidecode import unidecode

input_text = open('text.txt', encoding="utf-8").read()
# Create a white canvas
background = Image.new('RGB', (3000, 1000), (255, 255, 255))

x, y = 0, 0
multiplier = 1.0
imgHeight = Image.open('hand_fonts/32.jpg').height
lineSpacing = multiplier * imgHeight

for text in input_text:
    # If Enter is pressed, skip to the next line
    # print(text, ord(text))  --> prints the utf-8 ascii value of each character
    if ord(text) == 10:
        x = 0
        y += int(lineSpacing)
        continue

    # Converts ASCII value into a string
    ascii_current = str(ord(text))
    try:
        font = Image.open(f'hand_fonts/{ascii_current}.jpg')
    except:
        print(f"LOG - O arquivo hand_fonts/{ascii_current}.jpg não foi encontrado!")
        ascii_current = str(ord(unidecode(text)))
        print(f"LOG - Tentando substituir por hand_fonts/{ascii_current}.jpg ({chr(int(ascii_current))})")
        try:
            font = Image.open(f'hand_fonts/{ascii_current}.jpg')
        except:
            print(f"LOG - O arquivo hand_fonts/{ascii_current}.jpg tambem não foi encontrado!")
            continue
    
    # Paste the images correspondent to the letters
    background.paste(font, (x, y))
    
    x += font.width

    # If the text exceeds the canvas size, it skips to the next line
    if background.width < x or 115 > (background.width - x):
        x = 0
        y += int(lineSpacing)

print(f"LOG - Finalizando!")
background.show()
