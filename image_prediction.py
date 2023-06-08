import cv2
import numpy as np
import config

#Funkcja która bierze ścieżke do zdjęcia jako string i model
#zwraca stringa klasy która predictuje i orginalne zdjęcie które zostało wybrane jako np.array (można potem przekonwertować do pila i wyświetlić w gui czy coś idk)

def load_predict_image(img_path, model):
    try:
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resized_img = cv2.resize(img_rgb, (config.image_width, config.image_height))
        resized_img = np.expand_dims(resized_img, axis=0)
        resized_img = np.array(resized_img)
    except:
        print("Error in image: " + img_path)
        
    pred = model.predict(resized_img)
    pred_label = np.argmax(pred, axis=1)
    pred_class = config.classes[pred_label[0]]

    return pred_class, img_rgb

#żeby użyć trzeba załadować model

# import tensorflow as tf
# model = tf.keras.models.load_model(path_to_model)
# load_predict_image(img_path, model)