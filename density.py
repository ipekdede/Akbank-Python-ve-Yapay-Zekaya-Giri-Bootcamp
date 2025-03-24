import openai

def yolcu_yogunlugu_tahmini(baslangic_ad, hedef_ad, saat):
    prompt = f"""
        Sen bir metro danışmanısın. Kullanıcı {saat} saatinde '{baslangic_ad}' istasyonundan '{hedef_ad}' istasyonuna gitmek istiyor.

        Sen bir Ankara metrosu uzmanısın. 
        İş çıkış saatleri, istasyon yoğunlukları, popülerlik, aktarma ihtimali gibi faktörleri göz önünde bulundur. 
        Yolculuk hakkında kısa, net ve kullanıcı dostu bir yorum yap. Gerekiyorsa zamanlama veya alternatif öneriler ver.
        Yorumun 3-4 cümleyi geçmesin.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
