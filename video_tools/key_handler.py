import cv2


def handle_key_press(key, pause, show_keypoints, show_emotions, show_help):
    """
    Manipula a tecla pressionada pelo usuário para definir ações no visualizador de vídeo.

    Parâmetros:
    - key (int): O código ASCII da tecla pressionada.
    - pause (bool): Indica se o vídeo está pausado.
    - show_keypoints (bool): Indica se os pontos faciais estão sendo mostrados.
    - show_emotions (bool): Indica se as emoções estão sendo mostradas.
    - show_help (bool): Indica se o menu de ajuda está sendo exibido.

    Retorna:
    - tuple: Uma tupla contendo a ação a ser tomada e os estados atualizados para pause, show_keypoints, show_emotions e show_help.
    """
    
    actions = {
        ord('q'): ('break', pause, show_keypoints, show_emotions, show_help),
        ord('p'): (None, not pause, show_keypoints, show_emotions, show_help),
        ord('k'): (None, pause, not show_keypoints, show_emotions, show_help),
        ord('e'): (None, pause, show_keypoints, not show_emotions, show_help),
        ord('h'): (None, pause, show_keypoints, show_emotions, not show_help),
    }

    return actions.get(key, (None, pause, show_keypoints, show_emotions, show_help))


def add_messages_to_frame(frame, messages, display_width, show_help=True):
    """
    Adiciona mensagens (ou um menu de ajuda) a um quadro do vídeo.

    Parâmetros:
    - frame (ndarray): O quadro atual do vídeo.
    - messages (dict): Um dicionário com mensagens a serem exibidas.
    - display_width (int): A largura do display de visualização.
    - show_help (bool, opcional): Se True, exibe o menu de ajuda. Caso contrário, mostra a mensagem para pressionar [H]. Padrão é True.

    Retorna:
    - ndarray: O quadro com as mensagens adicionadas.
    """
    
    frame_copy = frame.copy()

    if show_help:
        cv2.rectangle(frame_copy, (display_width - 270, 0), (display_width - 0, 30 + 30 * len(messages)), (0, 0, 0), -1)

        alpha = 0.5
        cv2.addWeighted(frame_copy, alpha, frame, 1 - alpha, 0, frame)

        for idx, (key, message) in enumerate(messages.items()):
            cv2.putText(frame, message, (display_width - 250, 30 + 30 * idx), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    else:
        cv2.rectangle(frame_copy, (5, -10), (300, 25), (0, 0, 0), -1)

        alpha = 0.5
        cv2.addWeighted(frame_copy, alpha, frame, 1 - alpha, 0, frame)
        cv2.putText(frame, "Pressione [H] para exibir o menu", (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    return frame
