import cv2
import mediapipe as mp
import numpy as np
import os
import pickle
from math import atan2, degrees

# Inicializar o Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Função para calcular o ângulo entre dois vetores
def calculate_angle(p1, p2, p3):
    v1 = np.array(p1) - np.array(p2)
    v2 = np.array(p3) - np.array(p2)
    angle = atan2(v2[1], v2[0]) - atan2(v1[1], v1[0])
    return abs(degrees(angle))

# Função para processar uma imagem e obter os ângulos
def process_image(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
        
        # Definir o índice dos pontos das articulações
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        wrist = landmarks[0]
        
        # Calcular ângulos dos dedos em relação ao pulso
        angles = {
            "thumb_angle": calculate_angle(wrist, landmarks[1], thumb_tip),
            "index_angle": calculate_angle(wrist, landmarks[5], index_tip),
            "middle_angle": calculate_angle(wrist, landmarks[9], middle_tip),
            "ring_angle": calculate_angle(wrist, landmarks[13], ring_tip),
            "pinky_angle": calculate_angle(wrist, landmarks[17], pinky_tip)
        }
        
        return angles
    else:
        return None

# Caminho para a pasta contendo as imagens
image_folder = 'train2'
dataset = []

# Processar todas as imagens na pasta
for subfolder in os.listdir(image_folder):
    subfolder_path = os.path.join(image_folder, subfolder)
    for image_name in os.listdir(subfolder_path):
        image_path = os.path.join(subfolder_path, image_name)
        angles = process_image(image_path)
        if angles:
            dataset.append({"gesture": subfolder, "angles": angles})

# Salvar o dataset em um arquivo pickle
with open('gesture_angles3.pkl', 'wb') as f:
    pickle.dump(dataset, f)

print("Dataset criado com sucesso!")
