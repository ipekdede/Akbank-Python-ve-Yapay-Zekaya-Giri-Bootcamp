# Metro Rota Bulucu

Ankara metrosu için geliştirilmiş bu web tabanlı uygulama, kullanıcıya **en hızlı** ya da **en az aktarmalı** metro rotasını bulma imkânı sunar. Bunun yanı sıra, yolculuk saatine göre **ChatGPT destekli kalabalık tahmini** de yapar. Kullanıcı dostu arayüzü ve detaylı metro ağı modellemesiyle Ankara için önemli bir akıllı ulaşım uygulaması prototipidir.

---

## Canlı Uygulama Arayüzü
- Kullanıcı başlangıç ve hedef istasyonlarını seçer.
- Rota türü olarak "En Hızlı" veya "En Az Aktarmalı" seçilir.
- Yolculuk saati girilir.
- "Rota Bul" butonuna tıklandığında hem güzergah hem de kalabalık tahmini çıkar.

---

## 🔎 Proje Bileşenleri

### 1. **Rota Hesaplama Algoritmaları**
- **En Hızlı Rota**: Dijkstra algoritmasına dayalıdır.
- **En Az Aktarmalı**: BFS (Breadth-First Search) ile en az hat değiştiren yol hesaplanır.

### 2. **Metro Ağı Modeli** (`metro.py`)
- Her istasyon bir `Istasyon` sınıfı olarak tanımlanır.
- Hatlar, koordinatlar ve komşuluklar Flask için JSON formatında sunulur.

### 3. **Yolcu Yoğunluğu Tahmini** (`density.py`)
ChatGPT'den alınan özelleştirilmiş prompt:
```python
Sen bir metro danışmanısın. Kullanıcı {saat} saatinde '{baslangic_ad}' istasyonundan '{hedef_ad}' istasyonuna gitmek istiyor.


Sen bir Ankara metrosu uzmanısın.
İş çıkış saatleri, istasyon yoğunlukları, popülerlik, aktarma ihtimali gibi faktörleri göz önünde bulundur.
Yolculuk hakkında kısa, net ve kullanıcı dostu bir yorum yap. Gerekiyorsa zamanlama veya alternatif öneriler ver.
Yorumun 3-4 cümleyi geçmesin.
```

### 4. **Arayüz** (`index.html`)
Form alanları: Başlangıç, hedef, rota türü, saat.
Sonuç: Harita + Yolculuk bilgisi + ChatGPT kalabalık yorumu.

---

## 📊 Örnek Kalabalık Tahmini
![Kalabalık Tahmini](uploads/file-5FphRkVB26VQrpuSKXeAwd)

---

## 🔹 Rota Gösterimi
![Rota](uploads/file-GZK9utLj8MvsmLM69cNLaf)

- Zaman bilgisiyle birlikte güzergah harita ücretinde renklendirilir.
- Aktarma noktaları otomatik algılanır ve görsel olarak belirtilir.

---

## 📒 Metodoloji: Yolcu Yoğunluğu Tahmin Modülü
![Modül Metodolojisi](uploads/file-95TaJwnYJkfA3kbEeypUwC)

- Kullanıcı sorgusu tahmin modülüne gider.
- ChatGPT'den dönen çıktı yorum olarak arayüzde sunulur.
- Bu yorum, saatin "iş çıkışına denk gelmesi", "yoğun istasyonlar", "aktarma sayısı" gibi verilerden üretilir.

---

## 🔄 Akış Diyagramı
![Akış Diyagramı](uploads/file-DxTRk2QzkRFtKhSNFjM9mw)

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



