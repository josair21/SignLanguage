import cv2
import mediapipe as mp


entrada = "video.mp4"
alto = 960
ancho = 960

def main():
    video = cv2.VideoCapture(entrada)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, ancho)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, alto)
    #Preparacion del clasificador
    procesador_mano = mp.solutions.hands.Hands()
    dibujado_mano = mp.solutions.drawing_utils

    while True:
        frame, imagen = video.read()

        if not frame:
            print("Error al leer la imagen")
            break

        resultado = procesador_mano.process(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
        

        if resultado.multi_hand_landmarks:
            for hand_landmark in resultado.multi_hand_landmarks:
                dibujado_mano.draw_landmarks(imagen, hand_landmark, mp.solutions.hands.HAND_CONNECTIONS)

        print(resultado.multi_hand_landmarks)
        cv2.imshow("Salida", imagen)
        if cv2.waitKey(1) == 113:
            print("Terminado")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()