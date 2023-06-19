# Polecenia do zadań
Zadania trzeba robić po kolei, tzn. jak nie zrobicie pierwszego, nie zrobić kolejnych. 

## Zadanie 1.
Napisz funkcję, która przygotuje obrazek, aby można było go podać modelowi. Model oczekuje 4 wymiarowej listy (Ilość zdjęć, szerokość=30  wysokość=30, kanały=3). W naszym przypadku chcemy zrobić tylko dla jednego obrazka dlatego ilość zdjęć będzie wynosić 1.
Funkcja będzie brała jako argument ścieżkę jako string do obrazka i zwracała numpy array jako ten obrazek

Przydatna będzie biblioteka OpenCV. (import cv2)

    cv2.imread(img_path, cv2.IMREAD_COLOR) załadowanie obrazka, ważny jest tutaj argument cv2.IMREAD_COLOR precyzujemy w ten sposób, aby obrazek został wczytany z kolorami a dokładniej w formacie BGR.
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB) trzeba będzie przekonwertować załadowany obrazek z BGR na RGB.
    cv2.resize(img_rgb, (image_width, image_height)) musimy przeskalować nasz obraz, aby liczba neuronów które będa ładowane przez model była taka sama na jakiej był uczony. W naszym przypadku to będzie 30x30.

Przyda nam sie też biblioteka numpy (import numpy as np)

    np.expand_dims(resized_img, axis=0) Spowoduje to stworzenie nowego wymiaru. Kształt naszej listy będzie wyglądał (1, 30, 30, 3) zamiast (30, 30, 3).

Przetestuj działanie funkcji na jakimś wybranym przez ciebie obrazku i wykonaj

    print(returned_img.shape) jeśli otrzymasz (1, 30, 30, 3) znaczy ze jest git.

Wyślij kod i zwrócenie printa.

## Zadanie 2.
W tym zadaniu trzeba będzie spytać nasz model o to jakiej klasy jest wybrane przez nas zdjęcie znaku.
Trzeba będzie użyć wcześniej napisanej funkji i wytrenowanego przez nas modelu. Należy go pobrać z dysku google (66MB):
https://drive.google.com/file/d/1a5bylNuhRNaruQoUytkCRT60vWuAsBlo/view?usp=drive_link

Po pobraniu, należy załadować model w naszym pliku pythona. 
Potrzebna będzie do tego biblioteka tensorflow (import tensorflow as tf)

    model = tf.keras.models.load_model(path_to_model)

Po załadowaniu należy użyć metody model.predict() jako argument podać obrazek zwrócony przez funkcje z poprzedniego zadania
Wyprintuj zwróconą wartość przez tą metode. Jest to lista z predykcją klasy znaku dla podanej listy zdjęć, daliśmy mu tylko jedno zdjęcie więc będzie to lista w liście po prostu. Będzie występować tylko jedna "1" którą model postawił dla klasy która przewidział.
Aby zobaczyć jaki to nr klasy wystarczy zrobić np.argmax(pred, axis=1) zwróci nam to jedno elementową liste która zawiera index występowania 1 

Jednak same numery nam nic nie mówią dlatego zamienimy je na nazwy znaków. Przekopiuj poniższy python dictionary o nazwe classes do swojego kodu, a następnie odkoduj String nazwy znaku. 

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)', 
            2:'Speed limit (50km/h)', 
            3:'Speed limit (60km/h)', 
            4:'Speed limit (70km/h)', 
            5:'Speed limit (80km/h)', 
            6:'End of speed limit (80km/h)', 
            7:'Speed limit (100km/h)', 
            8:'Speed limit (120km/h)', 
            9:'No passing', 
            10:'No passing veh over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Veh > 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons' }

Wyprintuj otrzymaną nazwe, zrób ss kodu i otrzymanej nazwy

## Zadanie 3.
Zaprojektuj proste GUI, które będzie składało się z dwóch elementów: guzika, pozwalającego na wybranie pliku i labela, na którym będzie wyświetlana ścieżka wybranego pliku - elementy te powinny znajdować się obok siebie. Okno powinno mieć wymiary 600x300 i wymiar ten powinien być niemożliwy do zmiany, tytułem okna powinien być Twój numer indeksu.
W celu wykonania zadania wykorzystaj poniższe importy:

    import tkinter as tk
    from tkinter import filedialog as fd
    import os

Funkcje guzika zaprojektuj w funkcji select_path(), a wyświetlanie ścieżki w funkcji update_file_path_label. 

Do wykonania tego zadania przydadzą Ci się metody:
- askopenfilename
- abspath
- columnconfigure / rowconfigure

W rozwiązaniu zadania umieść ss kodu i swojego GUI.

## Zadanie 4.
Korzystając z rozwiązań do poprzednich zadań, stwórz okno, które będzie wypisywało zdjęcie i wynik działania modelu z zadań 1 i 2. Przyda Ci się do tego biblioteka PILLOW. Okno stwórz analogicznie jak w poprzednim zadaniu. To tyle wskazówek, powodzenia. Nie zapomnij o zrobieniu ss swojego kodu i okienka. 
