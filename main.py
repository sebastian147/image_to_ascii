from PIL import Image

def separar_letras(string, izquierda, derecha):
    letras_separadas = [izquierda + letra + derecha if letra != '\n' else letra for letra in string]
    return ''.join(letras_separadas)
def sensor_image(string):
        string = separar_letras(string, "||", "||")
        return string

def dividir_cadena(cadena, longitud_maxima=1000):
    subcadenas = []
    while len(cadena) > longitud_maxima:
        subcadena = cadena[:longitud_maxima]
        subcadenas.append(subcadena)
        cadena = cadena[longitud_maxima:]
    subcadenas.append(cadena + "\n")
    return subcadenas

def convertir_a_ascii(imagen, caracteres, anchura=30):
    # calcular las dimensiones de la imagen de salida
    (ancho_original, alto_original) = imagen.size
    proporcion = alto_original / ancho_original
    alto = int(proporcion * anchura)
    # redimensionar la imagen
    imagen_redimensionada = imagen.resize((anchura, alto))
    # convertir la imagen a escala de grises
    imagen_escala_grises = imagen_redimensionada.convert('L')
    # convertir la imagen a caracteres ASCII
    pixels = imagen_escala_grises.getdata()
    caracteres_ascii = ''.join([caracteres[int(pixel / 255 * (len(caracteres) - 1))] for pixel in pixels])
    # dividir la cadena en líneas de ancho fijo
    lineas = [caracteres_ascii[index:index+anchura] for index in range(0, len(caracteres_ascii), anchura)]
    # unir las líneas con saltos de línea
    return '\n'.join(lineas)

img = Image.open("CYitTOnUQAAAeEu.png")
ascii_chars1 = ['⢀', '░', '▒', '▓', '█']
ascii_chars2 = [' ', '⢀', '⢠', '⢤', '⢴', '⢶', '⣄', '⣆', '⣤', '⣦', '⣴', '⣶', '⣷', '⣿']
ascii_chars3 = ['⠀', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '⠇', '⠈', '⠉', '⠊', '⠋', '⠌', '⠍', '⠎', '⠏', '⠐', '⠑', '⠒', '⠓', '⠔', '⠕', '⠖', '⠗', '⠘', '⠙', '⠚', '⠛', '⠜', '⠝', '⠞', '⠟', '⠠', '⠡', '⠢', '⠣', '⠤', '⠥', '⠦', '⠧', '⠨', '⠩', '⠪', '⠫', '⠬', '⠭', '⠮', '⠯', '⠰', '⠱', '⠲', '⠳', '⠴', '⠵', '⠶', '⠷', '⠸', '⠹', '⠺', '⠻', '⠼', '⠽', '⠾', '⠿']
ascii_chars4 = ['←', '↑', '→', '↓']
ascii_chars5 = ['@', '#', '%', '*', '+', '-', '.', ':', ';', '=', '?', '^', '~']

# convertir la imagen a ASCII
text = convertir_a_ascii(img, ascii_chars2)
#text = sensor_image(text)
texto_dividido = dividir_cadena(text)

for subcadena in texto_dividido:
    print(subcadena)