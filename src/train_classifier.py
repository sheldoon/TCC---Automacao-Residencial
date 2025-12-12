import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import svm
# Carregar o dataset
with open('gesture_angles.pkl', 'rb') as f:
    dataset = pickle.load(f)

# Preparar os dados
X = []
y = []

for data in dataset:
    angles = data['angles']
    gesture = data['gesture']
    # Converter os ângulos em uma lista
    feature_vector = [
        angles['thumb_angle'],
        angles['index_angle'],
        angles['middle_angle'],
        angles['ring_angle'],
        angles['pinky_angle']
    ]
    X.append(feature_vector)
    y.append(gesture)

X = np.array(X)
y = np.array(y)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo SVM
model = svm.SVC(probability=True, random_state=np.random.randint(13), C= 0.1, gamma= 'auto', kernel= 'poly')


# 6. Treinar o modelo
model.fit(X_train, y_train)

# Salvar o modelo treinado
with open('svm_gesture_classifier.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo SVM treinado e salvo com sucesso!")

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)