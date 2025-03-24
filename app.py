import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import openai
from metro import MetroAgi
from density import yolcu_yogunlugu_tahmini

app = Flask(__name__)
metro = MetroAgi()


load_dotenv()
print("Yüklenen Anahtar:", os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG_ID")


def metro_agini_olustur():
    # İstasyonlar
    # Mavi Hat (OSB Törekent - Batıkent)
    metro.istasyon_ekle("M1", "OSB", "Mavi Hat", (40, 280))
    metro.istasyon_ekle("M2", "Törekent 2", "Mavi Hat", (80, 280))
    metro.istasyon_ekle("M3", "Törekent 1", "Mavi Hat", (120, 280))
    metro.istasyon_ekle("M4", "GOP", "Mavi Hat", (160, 280))
    metro.istasyon_ekle("M5", "Fatih Mah.", "Mavi Hat", (200, 280))
    metro.istasyon_ekle("M6", "Devlet Mah.", "Mavi Hat", (240, 280))
    metro.istasyon_ekle("M7", "Eryaman 3", "Mavi Hat", (280, 280))
    metro.istasyon_ekle("M8", "Eryaman 1-2", "Mavi Hat", (320, 280))
    metro.istasyon_ekle("M9", "İstanbul Yolu", "Mavi Hat", (360, 280))
    metro.istasyon_ekle("M10", "Botanik", "Mavi Hat", (400, 280))
    metro.istasyon_ekle("M11", "MESA", "Mavi Hat", (440, 280))
    metro.istasyon_ekle("M12", "Batıkent", "Mavi Hat", (480, 280))

    # Kırmızı Hat (Batıkent – Kızılay)
    metro.istasyon_ekle("K1", "Batıkent", "Kırmızı Hat", (480, 280)) # Ortak istasyon
    metro.istasyon_ekle("K2", "OSTİM", "Kırmızı Hat", (520, 280))
    metro.istasyon_ekle("K3", "Macunköy", "Kırmızı Hat", (560, 250))
    metro.istasyon_ekle("K4", "Hastane", "Kırmızı Hat", (600, 250))
    metro.istasyon_ekle("K5", "Demetevler", "Kırmızı Hat", (640, 250))
    metro.istasyon_ekle("K6", "Yenimahalle", "Kırmızı Hat", (680, 250))
    metro.istasyon_ekle("K7", "İvedik", "Kırmızı Hat", (720, 290))
    metro.istasyon_ekle("K8", "Akköprü", "Kırmızı Hat", (760, 290))
    metro.istasyon_ekle("K9", "AKM", "Kırmızı Hat", (800, 330))
    metro.istasyon_ekle("K10", "Ulus", "Kırmızı Hat", (840, 370))
    metro.istasyon_ekle("K11", "Sıhhiye", "Kırmızı Hat", (840, 410))
    metro.istasyon_ekle("K12", "Kızılay", "Kırmızı Hat", (840, 450))

    # Sarı Hat (Kızılay – Çayyolu)
    metro.istasyon_ekle("S1", "Kızılay", "Sarı Hat", (840, 450)) # Ortak istasyon
    metro.istasyon_ekle("S2", "TBMM", "Sarı Hat", (800, 490))
    metro.istasyon_ekle("S3", "TCK", "Sarı Hat", (760, 490))
    metro.istasyon_ekle("S4", "Milli Kütüphane", "Sarı Hat", (720, 490))
    metro.istasyon_ekle("S5", "Balgat", "Sarı Hat", (680, 490))
    metro.istasyon_ekle("S6", "Söğütözü", "Sarı Hat", (640, 530))
    metro.istasyon_ekle("S7", "MTA", "Sarı Hat", (600, 530))
    metro.istasyon_ekle("S8", "ODTÜ", "Sarı Hat", (560, 530))
    metro.istasyon_ekle("S9", "Bilkent", "Sarı Hat", (520, 530))
    metro.istasyon_ekle("S10", "Köy Hizmetleri", "Sarı Hat", (480, 530))
    metro.istasyon_ekle("S11", "Beytepe", "Sarı Hat", (440, 530))
    metro.istasyon_ekle("S12", "Etimesgut", "Sarı Hat", (400, 530))
    metro.istasyon_ekle("S13", "Ümitköy", "Sarı Hat", (360, 530))
    metro.istasyon_ekle("S14", "Çayyolu 1", "Sarı Hat", (320, 530))

    # Mor Hat (Ulus – Keçiören)
    metro.istasyon_ekle("M_1", "Ulus", "Mor Hat", (840, 330)) # Ortak istasyon
    metro.istasyon_ekle("M_2", "Dışkapı", "Mor Hat", (840, 270))
    metro.istasyon_ekle("M_3", "Meteoroloji", "Mor Hat", (880, 230))
    metro.istasyon_ekle("M_4", "Belediye", "Mor Hat", (880, 190))
    metro.istasyon_ekle("M_5", "Mecidiye", "Mor Hat", (880, 150))
    metro.istasyon_ekle("M_6", "Kuyubaşı", "Mor Hat", (880, 110))
    metro.istasyon_ekle("M_7", "Dutluk", "Mor Hat", (840, 70))
    metro.istasyon_ekle("M_8", "Gazino", "Mor Hat", (800, 30))

    # Yeşil Hat (Ulus – Keçiören)
    metro.istasyon_ekle("Y1", "Kızılay", "Yeşil Hat", (840, 450)) # Ortak istasyon
    metro.istasyon_ekle("Y2", "Kolej", "Yeşil Hat", (880, 450))
    metro.istasyon_ekle("Y3", "Kurtuluş", "Yeşil Hat", (920, 410))
    metro.istasyon_ekle("Y4", "Dikimevi", "Yeşil Hat", (960, 410))
    metro.istasyon_ekle("Y5", "Demirtepe", "Yeşil Hat", (800, 430))
    metro.istasyon_ekle("Y6", "Maltepe", "Yeşil Hat", (760, 390))
    metro.istasyon_ekle("Y7", "Tandoğan", "Yeşil Hat", (720, 390))
    metro.istasyon_ekle("Y8", "Beşevler", "Yeşil Hat", (680, 390))
    metro.istasyon_ekle("Y9", "Bahçelievler", "Yeşil Hat", (620, 390))
    metro.istasyon_ekle("Y10", "Emek", "Yeşil Hat", (580, 410))
    metro.istasyon_ekle("Y11", "AŞTİ", "Yeşil Hat", (580, 450))

    # Gri Hat
    metro.istasyon_ekle("G1", "Gazi Mahallesi", "Gri Hat", (680, 340))
    metro.istasyon_ekle("G2", "Hipodrom", "Gri Hat", (740, 340))
    metro.istasyon_ekle("G3", "Gar", "Gri Hat", (810, 380))
    metro.istasyon_ekle("G4", "Yenişehir", "Gri Hat", (880, 390))
    metro.istasyon_ekle("G5", "Kurtuluş", "Gri Hat", (920, 410)) # Ortak istasyon
    metro.istasyon_ekle("G6", "Cebeci", "Gri Hat", (960, 330))
    metro.istasyon_ekle("G7", "Demirlibahçe", "Gri Hat", (1000, 290))
    metro.istasyon_ekle("G8", "Gülveren", "Gri Hat", (1040, 250))
    metro.istasyon_ekle("G9", "Saimekadın", "Gri Hat", (1100, 250))
    metro.istasyon_ekle("G10", "Mamak", "Gri Hat", (1140, 290))

    # Bağlantılar
    # Mavi Hat bağlantılar
    metro.baglanti_ekle("M1", "M2", 2)
    metro.baglanti_ekle("M2", "M3", 2)
    metro.baglanti_ekle("M3", "M4", 2)
    metro.baglanti_ekle("M4", "M5", 2)
    metro.baglanti_ekle("M5", "M6", 2)
    metro.baglanti_ekle("M6", "M7", 2)
    metro.baglanti_ekle("M7", "M8", 2)
    metro.baglanti_ekle("M8", "M9", 2)
    metro.baglanti_ekle("M9", "M10", 2)
    metro.baglanti_ekle("M10", "M11", 2)
    metro.baglanti_ekle("M11", "M12", 2)

    # Kırmızı Hat bağlantılar
    metro.baglanti_ekle("K1", "K2", 2)
    metro.baglanti_ekle("K2", "K3", 2)
    metro.baglanti_ekle("K3", "K4", 2)
    metro.baglanti_ekle("K4", "K5", 2)
    metro.baglanti_ekle("K5", "K6", 2)
    metro.baglanti_ekle("K6", "K7", 2)
    metro.baglanti_ekle("K7", "K8", 2)
    metro.baglanti_ekle("K8", "K9", 2)
    metro.baglanti_ekle("K9", "K10", 2)
    metro.baglanti_ekle("K10", "K11", 2)
    metro.baglanti_ekle("K11", "K12", 2)
    

    # Sarı Hat bağlantılar 
    metro.baglanti_ekle("S1", "S2", 2)
    metro.baglanti_ekle("S2", "S3", 2)
    metro.baglanti_ekle("S3", "S4", 2)
    metro.baglanti_ekle("S4", "S5", 2)
    metro.baglanti_ekle("S5", "S6", 2)
    metro.baglanti_ekle("S6", "S7", 2)
    metro.baglanti_ekle("S7", "S8", 2)
    metro.baglanti_ekle("S8", "S9", 2)
    metro.baglanti_ekle("S9", "S10", 2)
    metro.baglanti_ekle("S10", "S11", 2)
    metro.baglanti_ekle("S11", "S12", 2)
    metro.baglanti_ekle("S12", "S13", 2)
    metro.baglanti_ekle("S13", "S14", 2)

    # Mor Hat bağlantılar 
    metro.baglanti_ekle("M_1", "M_2", 2)
    metro.baglanti_ekle("M_2", "M_3", 2)
    metro.baglanti_ekle("M_3", "M_4", 2)
    metro.baglanti_ekle("M_4", "M_5", 2)
    metro.baglanti_ekle("M_5", "M_6", 2)
    metro.baglanti_ekle("M_6", "M_7", 2)
    metro.baglanti_ekle("M_7", "M_8", 2)

    # Yeşil Hat bağlantılar
    metro.baglanti_ekle("Y1", "Y2", 2)
    metro.baglanti_ekle("Y2", "Y3", 2)
    metro.baglanti_ekle("Y3", "Y4", 2)
    metro.baglanti_ekle("Y1", "Y5", 2)
    metro.baglanti_ekle("Y5", "Y6", 2)
    metro.baglanti_ekle("Y6", "Y7", 2)
    metro.baglanti_ekle("Y7", "Y8", 2)
    metro.baglanti_ekle("Y8", "Y9", 2)
    metro.baglanti_ekle("Y9", "Y10", 2)
    metro.baglanti_ekle("Y10", "Y11", 2)

    # Gri Hat bağlantılar
    metro.baglanti_ekle("G1", "G2", 2)
    metro.baglanti_ekle("G2", "G3", 2)
    metro.baglanti_ekle("G3", "G4", 2)
    metro.baglanti_ekle("G4", "G5", 2)
    metro.baglanti_ekle("G5", "G6", 2)
    metro.baglanti_ekle("G6", "G7", 2)
    metro.baglanti_ekle("G7", "G8", 2)
    metro.baglanti_ekle("G8", "G9", 2)
    metro.baglanti_ekle("G9", "G10", 2)

    # Aktarma noktaları
    metro.baglanti_ekle("M12", "K1", 1)  # Batıkent (Mavi -Kırmızı)
    metro.baglanti_ekle("K12", "S1", 1)  # Kızılay (Kırmızı - Sarı)
    metro.baglanti_ekle("K12", "Y1", 1)  # Kızılay (Kırmızı - Yeşil)
    metro.baglanti_ekle("S1", "Y1", 1)   # Kızılay (Sarı - Yeşil)
    metro.baglanti_ekle("K10", "M_1", 1) # Ulus (Kırmızı - Mor)
    metro.baglanti_ekle("Y3", "G5", 1)   # Kurtuluş (Yeşil - Gri)


metro_agini_olustur()


def get_hat_rengi(hat):
    renkler = {
        "Kırmızı Hat": "red",
        "Mavi Hat": "deepskyblue",
        "Turuncu Hat": "orange",
        "Yeşil Hat": "lime",
        "Mor Hat": "violet",
        "Sarı Hat": "gold"
    }
    return renkler.get(hat, "gray")

def aktarma_noktalari(rota):
    aktarmalar = []
    for i in range(1, len(rota)):
        if rota[i].hat != rota[i - 1].hat:
            aktarmalar.append(rota[i])
    return aktarmalar


@app.route('/', methods=['GET', 'POST'])
def index():
    #Aynı isme sahip istasyonların bir kez gösterilmesi
    gorunen_istasyonlar = {}
    for ist in metro.istasyonlar.values():
        if ist.ad not in gorunen_istasyonlar:
            gorunen_istasyonlar[ist.ad] = ist
    form_icin_istasyonlar = list(gorunen_istasyonlar.values())

    rota = []
    sure = None
    rota_turu = ""
    rota_ids = []
    tahminler = []
    secilen_saat = "18:00"
    tahmin = None  # <-- Burası önemli

    if request.method == 'POST':
        baslangic = request.form['baslangic']
        hedef = request.form['hedef']
        rota_turu = request.form['rota_turu']
        secilen_saat = request.form.get('saat', "18:00")

        if rota_turu == 'hizli':
            sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
            if sonuc:
                rota, sure = sonuc
        else:
            rota = metro.en_az_aktarma_bul(baslangic, hedef)

        if rota:
            rota_ids = [ist.idx for ist in rota]
            tahmin = yolcu_yogunlugu_tahmini(rota[0].ad, rota[-1].ad, secilen_saat)



    istasyonlar_json = [{
        "idx": ist.idx,
        "ad": ist.ad,
        "hat": ist.hat,
        "x": ist.konum[0],
        "y": ist.konum[1],
        "renk": get_hat_rengi(ist.hat),
        "komsular": [{
            "idx": k.idx,
            "x": k.konum[0],
            "y": k.konum[1]
        } for k, _ in ist.komsular]
    } for ist in metro.istasyonlar.values()]

    return render_template(
        'index.html',
        istasyonlar=form_icin_istasyonlar,
        istasyonlar_json=istasyonlar_json,
        rota=rota,
        rota_ids=rota_ids,
        sure=sure,
        rota_turu=rota_turu,
        tahmin=tahmin,
        secilen_saat=secilen_saat

    )


if __name__ == '__main__':
    app.run(debug=True, port=5001)
