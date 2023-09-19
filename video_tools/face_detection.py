import cv2
import mediapipe as mp
from deepface import DeepFace
from utils.helpers import load_json
from config.settings import PATH_EMOTION_TRANSLATION_FILE


def detect_faces(image):
    """
    Detecta faces em uma imagem.

    Parâmetros:
    - image (ndarray): A imagem em que a detecção de face será realizada.

    Retorna:
    - list: Uma lista contendo os pontos de referência da face detectada, se houver alguma.
    """

    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=100, min_detection_confidence=0.2) as face_mesh:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

    return results.multi_face_landmarks if results.multi_face_landmarks else []


def get_face_bounding_box(face_landmarks, image_width, image_height):
    """
    Obtém a caixa delimitadora em torno de uma face com base em seus pontos de referência.

    Parâmetros:
    - face_landmarks (list): Lista de pontos de referência da face.
    - image_width (int): Largura da imagem.
    - image_height (int): Altura da imagem.

    Retorna:
    - tuple: Coordenadas (x_min, y_min, x_max, y_max) da caixa delimitadora.
    """

    x_min, y_min = image_width, image_height
    x_max, y_max = 0, 0

    for landmark in face_landmarks.landmark:
        x, y = int(landmark.x * image_width), int(landmark.y * image_height)
        x_min, y_min = min(x, x_min), min(y, y_min)
        x_max, y_max = max(x, x_max), max(y, y_max)

    return x_min, y_min, x_max, y_max


def analyze_emotions(face_crop_no_points):
    """
    Analisa as emoções de um rosto.

    Parâmetros:
    - face_crop_no_points (ndarray): Imagem da face sem os pontos de referência.

    Retorna:
    - str: A emoção dominante detectada, se houver.
    """

    try:
        emotion_analysis = DeepFace.analyze(face_crop_no_points, actions=['emotion'], enforce_detection=False)
        if isinstance(emotion_analysis, list):
            emotion_analysis = emotion_analysis[0]

        emotion_translation = load_json(PATH_EMOTION_TRANSLATION_FILE)

        dominant_emotion = emotion_analysis['dominant_emotion']
        dominant_emotion_pt = emotion_translation.get(dominant_emotion, 'None')

        return dominant_emotion_pt.capitalize()
    except:
        return 'None'
    

def is_human_face(image, draw_keypoints=True, detect_emotions=True):
    """
    Verifica se há rostos humanos na imagem e, se sim, processa e extrai informações.

    Parâmetros:
    - image (ndarray): A imagem a ser processada.
    - draw_keypoints (bool, opcional): Se True, desenha pontos de referência no rosto. Padrão é True.
    - detect_emotions (bool, opcional): Se True, detecta emoções no rosto. Padrão é True.

    Retorna:
    - list: Uma lista contendo informações de cada rosto detectado, como emoção dominante e imagens cortadas.
    """
    
    mp_drawing = mp.solutions.drawing_utils

    face_data = []
    face_landmarks_list = detect_faces(image)
    height, width, _ = image.shape

    for face_landmarks in face_landmarks_list:
        image_copy = image.copy()

        if draw_keypoints:
            landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
            connection_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
            
            mp_drawing.draw_landmarks(image, face_landmarks, mp.solutions.face_mesh.FACEMESH_TESSELATION,
                                      landmark_drawing_spec=landmark_drawing_spec,
                                      connection_drawing_spec=connection_drawing_spec)

        x_min, y_min, x_max, y_max = get_face_bounding_box(face_landmarks, width, height)

        face_crop_no_points = image_copy[y_min:y_max, x_min:x_max]
        face_crop_with_points = image[y_min:y_max, x_min:x_max]

        if detect_emotions:
            dominant_emotion = analyze_emotions(face_crop_no_points)
        else:
            dominant_emotion = None

        face_data.append({
            "annotated_image": image,
            "face_crop_no_points": face_crop_no_points,
            "face_crop_with_points": face_crop_with_points,
            "dominant_emotion": dominant_emotion,
            "bounding_box": (x_min, y_min, x_max, y_max)
        })

    return face_data
