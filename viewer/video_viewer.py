# video_viewer.py
import cv2
from core import video_processing


def run_video_viewer(video_path, messages, display_width, display_height):
    """
    Executa o visualizador de vídeo, processando e exibindo o vídeo frame a frame.

    Parâmetros:
    - video_path (str): Caminho do arquivo de vídeo que será processado.
    - messages (dict): Dicionário contendo mensagens para exibir na interface.
    - display_width (int): Largura da janela de exibição do vídeo.
    - display_height (int): Altura da janela de exibição do vídeo.

    Durante a execução, o vídeo é processado frame a frame para detectar faces, pontos faciais e emoções. 
    O usuário pode pausar, reproduzir e alterar configurações em tempo real através de atalhos no teclado.
    """
    
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print('fps:', fps)

    pause = False
    show_keypoints = False
    show_emotions = False
    show_help = False

    while cap.isOpened():
        if not pause:
            ret, frame = cap.read()

            if not ret:
                break

            face_data_list, display_frame = video_processing.process_frame(frame, display_width, display_height, show_keypoints, show_emotions)
            video_processing.update_display(display_frame, messages, display_width, show_help)

        action, pause, show_keypoints, show_emotions, show_help = video_processing.handle_user_input(pause, show_keypoints, show_emotions, show_help)

        if action == 'break':
            break

    cap.release()
    cv2.destroyAllWindows()
