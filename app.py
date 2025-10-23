import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Streamlit sayfa ayarları
st.set_page_config(page_title="Duygu Tanıma", page_icon=":smiley:", layout="centered")

# Stil ekle
st.markdown("""
    <style>
    .main {background-color: #222831;}
    .stApp {background-color: #222831;}
    .stButton>button {background-color: #00adb5; color: white;}
    .stRadio>div {color: #00adb5;}
    .stFileUploader {background-color: #393e46;}
    .stImage {border-radius: 10px; box-shadow: 0 4px 16px rgba(0,0,0,0.3);}
    </style>
""", unsafe_allow_html=True)

# Model ve haarcascade yükle
model = load_model('Emotion_little_vgg.h5', compile=False)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

st.markdown("<h1 style='text-align: center; color: #00adb5;'>Duygu Tanıma Uygulaması</h1>", unsafe_allow_html=True)
st.markdown(
    "<div style='background-color: #393e46; padding: 15px; border-radius: 10px; color: #eeeeee; text-align: center;'>"
    "Kameradan veya yüklediğiniz fotoğraftan yüz ifadesi analizi yapar."
    "</div>", unsafe_allow_html=True
)

st.write("")
secenek = st.radio('Analiz yöntemi seçin:', ('Kamera', 'Fotoğraf Yükle'))

if secenek == 'Kamera':
    run = st.checkbox('Kamerayı Başlat')
    FRAME_WINDOW = st.image([])
    if run:
        cap = cv2.VideoCapture(0)
        while run:
            ret, frame = cap.read()
            if not ret:
                st.warning("Kamera görüntüsü alınamıyor.")
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
                if np.sum([roi_gray]) != 0:
                    roi = roi_gray.astype('float') / 255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)
                    preds = model.predict(roi)[0]
                    label = class_labels[preds.argmax()]
                    label_position = (x, y-10)
                    cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 173, 181), 2)
            FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        cap.release()
    else:
        st.info("Kamerayı başlatmak için kutucuğu işaretleyin.")

elif secenek == 'Fotoğraf Yükle':
    uploaded_file = st.file_uploader("Bir fotoğraf yükleyin", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        labels = []
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                preds = model.predict(roi)[0]
                label = class_labels[preds.argmax()]
                labels.append(label)
                label_position = (x, y-10)
                cv2.putText(image, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 173, 181), 2)
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Analiz Sonucu', use_container_width=True)
        if len(faces) == 0:
            st.warning("Yüz tespit edilemedi.")
        else:
            st.success("Analiz Sonucu:")
            for i, label in enumerate(labels):
                st.write(f"Yüz {i+1}: :smiley: **{label}**") 