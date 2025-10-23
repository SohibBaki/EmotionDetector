# Duygu Tanıma Projesi / Emotion Recognition Project

**Geliştirici / Developer:** Soheyb Boutadjine - 212802095

---

##  Proje Hakkında / About the Project

** Türkçe:**
Bu proje, derin öğrenme teknikleri kullanarak yüz ifadelerinden duyguları tanıyan bir sistemdir. Proje, 7 farklı duygu sınıfını (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise) tespit edebilen bir CNN (Convolutional Neural Network) modeli içerir.

**🇺🇸 English:**
This project is a system that recognizes emotions from facial expressions using deep learning techniques. The project includes a CNN (Convolutional Neural Network) model that can detect 7 different emotion classes (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise).

---

##  Özellikler / Features

** Türkçe:**
- **Gerçek Zamanlı Duygu Tanıma**: Kameradan canlı video akışı ile duygu analizi
- **Fotoğraf Analizi**: Yüklenen fotoğraflardan duygu tespiti
- **Web Arayüzü**: Streamlit ile kullanıcı dostu arayüz
- **Yüksek Doğruluk**: Eğitilmiş CNN modeli ile yüksek başarı oranı
- **Çoklu Yüz Tespiti**: Tek seferde birden fazla yüzü analiz edebilme

** English:**
- **Real-time Emotion Recognition**: Live emotion analysis from camera video stream
- **Photo Analysis**: Emotion detection from uploaded photos
- **Web Interface**: User-friendly interface with Streamlit
- **High Accuracy**: High success rate with trained CNN model
- **Multi-face Detection**: Ability to analyze multiple faces at once

---

##  Teknolojiler / Technologies

- **Python 3.x**
- **TensorFlow/Keras**: Deep learning model / Derin öğrenme modeli
- **OpenCV**: Face detection and image processing / Yüz tespiti ve görüntü işleme
- **Streamlit**: Web interface / Web arayüzü
- **NumPy**: Numerical computations / Sayısal hesaplamalar

---

##  Proje Yapısı / Project Structure

```
ProjeKodlari/
├── app.py                          # Streamlit web uygulaması / Streamlit web app
├── train.py                        # Model eğitim kodu / Model training code
├── Test.py                         # Test kodu (OpenCV ile) / Test code (with OpenCV)
├── Emotion_little_vgg.h5           # Eğitilmiş model / Trained model
├── haarcascade_frontalface_default.xml  # Yüz tespiti için Haar Cascade / Haar Cascade for face detection
├── Algoritma_Jupyter.ipynb        # Jupyter notebook
├── train/                          # Eğitim verileri / Training data
│   ├── angry/                      # Kızgın yüz ifadeleri / Angry facial expressions
│   ├── disgust/                    # İğrenme yüz ifadeleri / Disgust facial expressions
│   ├── fear/                       # Korku yüz ifadeleri / Fear facial expressions
│   ├── happy/                      # Mutlu yüz ifadeleri / Happy facial expressions
│   ├── neutral/                    # Nötr yüz ifadeleri / Neutral facial expressions
│   ├── sad/                        # Üzgün yüz ifadeleri / Sad facial expressions
│   └── surprise/                   # Şaşkın yüz ifadeleri / Surprise facial expressions
└── validation/                     # Doğrulama verileri / Validation data
    ├── angry/
    ├── disgust/
    ├── fear/
    ├── happy/
    ├── neutral/
    ├── sad/
    └── surprise/
```

---

##  Kurulum ve Çalıştırma / Installation and Running

### Gereksinimler / Requirements

```bash
pip install tensorflow
pip install opencv-python
pip install streamlit
pip install numpy
```

### Web Uygulamasını Çalıştırma / Running Web Application

```bash
streamlit run app.py
```

### Test Uygulamasını Çalıştırma / Running Test Application

```bash
python Test.py
```

---

##  Kullanım / Usage

### Web Arayüzü (app.py) / Web Interface (app.py)

** Türkçe:**
1. Uygulamayı başlatın: `streamlit run app.py`
2. Tarayıcınızda açılan sayfada analiz yöntemini seçin:
   - **Kamera**: Gerçek zamanlı kamera analizi
   - **Fotoğraf Yükle**: Dosyadan fotoğraf yükleme

** English:**
1. Start the application: `streamlit run app.py`
2. Select the analysis method on the page that opens in your browser:
   - **Camera**: Real-time camera analysis
   - **Upload Photo**: Upload photo from file

### Test Uygulaması (Test.py) / Test Application (Test.py)

** Türkçe:**
- OpenCV ile gerçek zamanlı kamera analizi
- 'q' tuşuna basarak çıkış yapabilirsiniz

** English:**
- Real-time camera analysis with OpenCV
- Press 'q' key to exit

---

##  Model Mimarisi / Model Architecture

** Türkçe:**
Proje, özel olarak tasarlanmış bir CNN modeli kullanır:

- **5 Konvolüsyon Bloğu**: Her blok 2 konvolüsyon katmanı içerir
- **Batch Normalization**: Eğitim stabilitesi için
- **Dropout**: Aşırı öğrenmeyi önlemek için
- **ELU Aktivasyon**: Daha iyi performans için
- **7 Sınıf Çıkışı**: 7 farklı duygu sınıfı

** English:**
The project uses a specially designed CNN model:

- **5 Convolution Blocks**: Each block contains 2 convolution layers
- **Batch Normalization**: For training stability
- **Dropout**: To prevent overfitting
- **ELU Activation**: For better performance
- **7 Class Output**: 7 different emotion classes

---

##  Veri Seti / Dataset

- **Toplam Veri / Total Data**: ~30,000+ görüntü / images
- **Eğitim Verisi / Training Data**: ~25,000+ görüntü / images
- **Doğrulama Verisi / Validation Data**: ~5,000+ görüntü / images
- **Görüntü Boyutu / Image Size**: 48x48 piksel (gri tonlama) / pixels (grayscale)
- **Duygu Sınıfları / Emotion Classes**: 7 sınıf / classes (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise)

---

##  Model Eğitimi / Model Training

** Türkçe:**
Modeli yeniden eğitmek için:

```bash
python train.py
```

Eğitim parametreleri:
- **Epochs**: 25
- **Batch Size**: 32
- **Optimizer**: Adam (lr=0.001)
- **Data Augmentation**: Döndürme, kaydırma, yakınlaştırma

** English:**
To retrain the model:

```bash
python train.py
```

Training parameters:
- **Epochs**: 25
- **Batch Size**: 32
- **Optimizer**: Adam (lr=0.001)
- **Data Augmentation**: Rotation, shifting, zooming

---

##  Performans / Performance

- **Eğitim Doğruluğu / Training Accuracy**: %85+ 
- **Doğrulama Doğruluğu / Validation Accuracy**: %80+
- **Gerçek Zamanlı İşleme / Real-time Processing**: 30+ FPS

---

##  Arayüz Özellikleri / Interface Features

** Türkçe:**
- **Modern Tasarım**: Koyu tema ile şık görünüm
- **Responsive**: Farklı ekran boyutlarına uyum
- **Kullanıcı Dostu**: Basit ve anlaşılır arayüz
- **Gerçek Zamanlı Sonuçlar**: Anlık duygu tespiti

** English:**
- **Modern Design**: Elegant appearance with dark theme
- **Responsive**: Adapts to different screen sizes
- **User-friendly**: Simple and understandable interface
- **Real-time Results**: Instant emotion detection

---

##  Katkıda Bulunma / Contributing

** Türkçe:**
1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

** English:**
1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push your branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

---

##  Lisans / License

** Türkçe:** Bu proje eğitim amaçlı geliştirilmiştir.

** English:** This project is developed for educational purposes.

---

##  İletişim / Contact

**Soheyb Boutadjine** : Sohibboutadjine@gmail.com

---

*Bu proje, derin öğrenme ve bilgisayarlı görü teknikleri kullanılarak geliştirilmiştir. / This project is developed using deep learning and computer vision techniques.*
