# video_processing.py
import cv2
from video_tools import is_human_face, draw_rectangle, resize_frame, add_messages_to_frame, handle_key_press


def process_face_data(frame, show_keypoints, show_emotions):
    """
    Processa os dados da face para identificar keypoints e emoções.
    
    Args:
    - frame: O quadro/frame a ser processado.
    - show_keypoints: Se verdadeiro, mostra keypoints no frame.
    - show_emotions: Se verdadeiro, mostra emoções no frame.

    Retorna:
    - Lista de dados das faces e frame anotado.
    """

    face_data_list = is_human_face(frame, show_keypoints, show_emotions)
    annotated_frame = frame

    for face_data in face_data_list:
        x_min, y_min, x_max, y_max = face_data["bounding_box"]
        dominant_emotion = face_data["dominant_emotion"]

        if show_emotions and dominant_emotion:
            emotion_position = (x_min, y_min - 10)
            annotated_frame = draw_rectangle(annotated_frame, dominant_emotion, emotion_position)

    return face_data_list, annotated_frame

def process_frame(frame, display_width, display_height, show_keypoints, show_emotions):
    """
    Processa o frame completo, redimensionando e processando dados faciais.
    
    Args:
    - frame: O quadro/frame a ser processado.
    - display_width: Largura desejada para exibição.
    - display_height: Altura desejada para exibição.
    - show_keypoints: Se verdadeiro, mostra keypoints no frame.
    - show_emotions: Se verdadeiro, mostra emoções no frame.

    Retorna:
    - Lista de dados das faces e frame de exibição.
    """
    
    resized_frame = resize_frame(frame, width=display_width, height=display_height)
    face_data_list, display_frame = process_face_data(resized_frame, show_keypoints, show_emotions)
    return face_data_list, display_frame

def update_display(frame, messages, display_width, show_help):
    """
    Atualiza a exibição da janela com o frame processado e mensagens.
    
    Args:
    - frame: O quadro/frame a ser exibido.
    - messages: Mensagens a serem adicionadas ao frame.
    - display_width: Largura desejada para exibição.
    - show_help: Se verdadeiro, exibe mensagens de ajuda.

    Retorna:
    - None
    """
    
    frame_with_messages = add_messages_to_frame(frame, messages, display_width, show_help)
    cv2.imshow('Player', frame_with_messages)

def handle_user_input(pause, show_keypoints, show_emotions, show_help):
    """
    Manipula a entrada do usuário por meio de teclas pressionadas.
    
    Args:
    - pause: Se o vídeo está pausado ou não.
    - show_keypoints: Se verdadeiro, mostra keypoints no frame.
    - show_emotions: Se verdadeiro, mostra emoções no frame.
    - show_help: Se verdadeiro, exibe mensagens de ajuda.

    Retorna:
    - Ação a ser tomada com base na tecla pressionada e estados de exibição.
    """
    
    key = cv2.waitKey(1) & 0xFF
    return handle_key_press(key, pause, show_keypoints, show_emotions, show_help)
