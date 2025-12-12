#Importa as Biblioteecas
import os
import cv2


DATA_DIR = './train2/rocknroll'  #Escolhe a pasta pra salvar as imagens
if not os.path.exists(DATA_DIR):    #cria a pasta se ela nao existir
    os.makedirs(DATA_DIR)

number_of_classes = 1
dataset_size = 300 #quantidade de img que vai tirar

cap = cv2.VideoCapture(1)  #inicia a camera
for j in range(number_of_classes):
    while True: #Quando apertar Q vai começar a tirar foto e salvar na pasta
        ret, frame = cap.read()
        cv2.putText(frame, 'Aperte Q para começar', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size: #enquanto o contador tiver menor que a quantidade de imgs do começo, fica salvando as imgs
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, '{}.jpg'.format(counter)), frame) # salva as imgs

        counter += 1


cap.release()
cv2.destroyAllWindows()
