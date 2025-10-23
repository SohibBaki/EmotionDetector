# Duygu Tanıma Projesi (Emotion Recognition Project)

**Geliştirici:** Soheyb Boutadjine - 212802095

## 📋 Proje Hakkında

Bu proje, derin öğrenme teknikleri kullanarak yüz ifadelerinden duyguları tanıyan bir sistemdir. Proje, 7 farklı duygu sınıfını (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise) tespit edebilen bir CNN (Convolutional Neural Network) modeli içerir.

## 🚀 Özellikler

- **Gerçek Zamanlı Duygu Tanıma**: Kameradan canlı video akışı ile duygu analizi
- **Fotoğraf Analizi**: Yüklenen fotoğraflardan duygu tespiti
- **Web Arayüzü**: Streamlit ile kullanıcı dostu arayüz
- **Yüksek Doğruluk**: Eğitilmiş CNN modeli ile yüksek başarı oranı
- **Çoklu Yüz Tespiti**: Tek seferde birden fazla yüzü analiz edebilme

## 🛠️ Teknolojiler

- **Python 3.x**
- **TensorFlow/Keras**: Derin öğrenme modeli
- **OpenCV**: Yüz tespiti ve görüntü işleme
- **Streamlit**: Web arayüzü
- **NumPy**: Sayısal hesaplamalar

## 📁 Proje Yapısı

```
ProjeKodlari/
├── app.py                          # Streamlit web uygulaması
├── train.py                        # Model eğitim kodu
├── Test.py                         # Test kodu (OpenCV ile)
├── Emotion_little_vgg.h5           # Eğitilmiş model
├── haarcascade_frontalface_default.xml  # Yüz tespiti için Haar Cascade
├── Algoritma_Jupyter.ipynb        # Jupyter notebook
├── train/                          # Eğitim verileri
│   ├── angry/                      # Kızgın yüz ifadeleri
│   ├── disgust/                    # İğrenme yüz ifadeleri
│   ├── fear/                       # Korku yüz ifadeleri
│   ├── happy/                      # Mutlu yüz ifadeleri
│   ├── neutral/                    # Nötr yüz ifadeleri
│   ├── sad/                        # Üzgün yüz ifadeleri
│   └── surprise/                   # Şaşkın yüz ifadeleri
└── validation/                     # Doğrulama verileri
    ├── angry/
    ├── disgust/
    ├── fear/
    ├── happy/
    ├── neutral/
    ├── sad/
    └── surprise/
```

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

```bash
pip install tensorflow
pip install opencv-python
pip install streamlit
pip install numpy
```

### Web Uygulamasını Çalıştırma

```bash
streamlit run app.py
```

### Test Uygulamasını Çalıştırma

```bash
python Test.py
```

## 🎯 Kullanım

### Web Arayüzü (app.py)
1. Uygulamayı başlatın: `streamlit run app.py`
2. Tarayıcınızda açılan sayfada analiz yöntemini seçin:
   - **Kamera**: Gerçek zamanlı kamera analizi
   - **Fotoğraf Yükle**: Dosyadan fotoğraf yükleme

### Test Uygulaması (Test.py)
- OpenCV ile gerçek zamanlı kamera analizi
- 'q' tuşuna basarak çıkış yapabilirsiniz

## 🧠 Model Mimarisi

Proje, özel olarak tasarlanmış bir CNN modeli kullanır:

- **5 Konvolüsyon Bloğu**: Her blok 2 konvolüsyon katmanı içerir
- **Batch Normalization**: Eğitim stabilitesi için
- **Dropout**: Aşırı öğrenmeyi önlemek için
- **ELU Aktivasyon**: Daha iyi performans için
- **7 Sınıf Çıkışı**: 7 farklı duygu sınıfı

## 📊 Veri Seti

- **Toplam Veri**: ~30,000+ görüntü
- **Eğitim Verisi**: ~25,000+ görüntü
- **Doğrulama Verisi**: ~5,000+ görüntü
- **Görüntü Boyutu**: 48x48 piksel (gri tonlama)
- **Duygu Sınıfları**: 7 sınıf (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise)

## 🔧 Model Eğitimi

Modeli yeniden eğitmek için:

```bash
python train.py
```

Eğitim parametreleri:
- **Epochs**: 25
- **Batch Size**: 32
- **Optimizer**: Adam (lr=0.001)
- **Data Augmentation**: Döndürme, kaydırma, yakınlaştırma

## 📈 Performans

- **Eğitim Doğruluğu**: %85+ 
- **Doğrulama Doğruluğu**: %80+
- **Gerçek Zamanlı İşleme**: 30+ FPS

## 🎨 Arayüz Özellikleri

- **Modern Tasarım**: Koyu tema ile şık görünüm
- **Responsive**: Farklı ekran boyutlarına uyum
- **Kullanıcı Dostu**: Basit ve anlaşılır arayüz
- **Gerçek Zamanlı Sonuçlar**: Anlık duygu tespiti

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

## 📞 İletişim

**Soheyb Boutadjine** - 212802095

---

*Bu proje, derin öğrenme ve bilgisayarlı görü teknikleri kullanılarak geliştirilmiştir.*