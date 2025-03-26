# Metro Rota Bulucu

Ankara metrosu için geliştirilmiş bu web tabanlı uygulama, kullanıcıya **en hızlı** ya da **en az aktarmalı** metro rotasını bulma imkânı sunar. Bunun yanı sıra, yolculuk saatine göre **ChatGPT destekli kalabalık tahmini** de yapar. Kullanıcı dostu arayüzü ve detaylı metro ağı modellemesiyle Ankara için bir akıllı ulaşım uygulaması prototipidir.
---
## 🔄 Akış Diyagramı
  ![Screenshot 2025-03-24 at 22 05 36](https://github.com/user-attachments/assets/394a82d3-9b7c-4f15-ac54-60a128fb575f)


## Canlı Uygulama Arayüzü
- Kullanıcı başlangıç ve hedef istasyonlarını seçer.
- Rota türü olarak "En Hızlı" veya "En Az Aktarmalı" seçilir.
- Yolculuk saati girilir.
- "Rota Bul" butonuna tıklandığında hem güzergah hem de kalabalık tahmini çıkar.

## 📊 Örnek Kalabalık Tahmini
  <img width="1411" alt="Screenshot 2025-03-24 at 21 47 55" src="https://github.com/user-attachments/assets/be4a52d8-42aa-48df-beb5-53a3145a8e34" />

   ## 🔹 Rota Gösterimi
  <img width="1446" alt="Screenshot 2025-03-24 at 21 57 21" src="https://github.com/user-attachments/assets/d57a5814-d48c-424c-b117-1f40efbc4155" />
  <img width="1377" alt="Screenshot 2025-03-24 at 21 57 32" src="https://github.com/user-attachments/assets/9cd20a5b-8f34-4d92-9eac-822c0d3ae1b1" />

---

## 🔎 Proje Bileşenleri

### 1. **Rota Hesaplama Algoritmaları**
- **En Hızlı Rota**: Dijkstra algoritmasına dayalıdır.
- **En Az Aktarmalı**: BFS (Breadth-First Search) ile en az hat değiştiren yol hesaplanır.

### 2. **Metro Ağı Modeli** (`metro.py`)
- Her istasyon bir `Istasyon` sınıfı olarak tanımlanır.
- Hatlar, koordinatlar ve komşuluklar Flask için JSON formatında sunulur.

### 3. **Yolcu Yoğunluğu Tahmini** (`density.py`)
- Kullanıcı sorgusu tahmin modülüne gider.
- ChatGPT'den dönen çıktı yorum olarak arayüzde sunulur.
- Bu yorum, saatin "iş çıkışına denk gelmesi", "yoğun istasyonlar", "aktarma sayısı" gibi verilerden üretilir.
  
![Screenshot 2025-03-24 at 21 56 55](https://github.com/user-attachments/assets/f436c172-7440-4b2a-ab7e-dbf0b5115374)


### 4. **Arayüz** (`index.html`)
Form alanları: Başlangıç, hedef, rota türü, saat.
Sonuç: Harita + Yolculuk bilgisi + ChatGPT kalabalık yorumu içerir.

---


## 📚 Kurulum Talimatları

1. **Bağımlılıkları yükleyin**
```bash
pip install flask openai python-dotenv
```

2. **API Anahtarlarını tanımlayın** (.env dosyasına ekleyin)
```
OPENAI_API_KEY=your-key-here
OPENAI_ORG_ID=your-org-id
```

3. **Sunucuyu başlatın**
```bash
python app.py
```

---

## 📓 Dosya Yapısı
```
- app.py               # Flask uygulaması
- metro.py            # Metro ağı tanımları ve rota algoritmaları
- density.py          # Kalabalık tahmin modülü (ChatGPT)
- templates/
  - index.html        # HTML arayüz
- static/
  - style.css         # Stil dosyası
- .env                # API anahtarları
```

---



