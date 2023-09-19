import cv2


def resize_frame(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Redimensiona uma imagem para as dimensões especificadas, mantendo sua proporção.

    Parâmetros:
    - image (ndarray): A imagem a ser redimensionada.
    - width (int, opcional): A largura desejada da imagem redimensionada. Se None, será calculada com base na altura fornecida.
    - height (int, opcional): A altura desejada da imagem redimensionada. Se None, será calculada com base na largura fornecida.
    - inter (int, opcional): Método de interpolação a ser usado. Padrão é cv2.INTER_AREA.

    Retorna:
    - ndarray: Imagem redimensionada.
    """
    
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def draw_rectangle(frame, text, position, margin=5):
    """
    Desenha um retângulo com texto dentro em uma imagem dada.

    Parâmetros:
    - frame (ndarray): A imagem onde o retângulo com texto será desenhado.
    - text (str): O texto a ser desenhado dentro do retângulo.
    - position (tuple): A posição (x, y) onde o canto inferior esquerdo do texto será colocado.
    - margin (int, opcional): A margem em torno do texto dentro do retângulo. Padrão é 5.

    Retorna:
    - ndarray: Imagem com o retângulo e texto desenhados.
    """
    
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    text_width = text_size[0] + 2 * margin
    text_height = text_size[1] + 2 * margin

    text_x, text_y = position
    bg_rect = (text_x, text_y - text_height, text_width, text_height)
    cv2.rectangle(frame, bg_rect, (0, 0, 0), -1)
    cv2.putText(frame, text, (text_x + margin, text_y - margin), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return frame
