# Pusula_ErtugrulErdem_Kucuk
 Pusula Talent Academy Data Science Case
Ertuğrul Erdem Küçük
ekucuk29@gmail.com

Amaç

Bu Python scripti, sağlık verileri içeren bir Excel dosyasını analiz ederek istatistiksel raporlar ve görselleştirmeler üretir.
Kod hem terminal çıktısı verir hem de 13 farklı grafik PNG formatında kaydeder.

----------------------------------------------------------------------------------------------------------------------------------------

Kullanılan Teknolojiler

pandas → Veri okuma, işleme ve istatistiksel hesaplamalar

matplotlib → Grafik çizimi

seaborn → Estetik görselleştirme (heatmap vb.)

numpy → Matematiksel işlemler (korelasyon, standart sapma)

collections.Counter → Tekrarlayan değerlerin hızlı sayımı

----------------------------------------------------------------------------------------------------------------------------------------

Veri Seti

Excel dosyası: Talent_Academy_Case_DT_2025.xlsx

Beklenen sütunlar:

HastaNo → Hasta numarası

Cinsiyet → Kadın / Erkek

Yas → Hastanın yaşı

KronikHastalik → Kronik hastalık listesi

Tanilar → Konulan tanılar

TedaviAdi → Uygulanan tedavi türü

TedaviSuresi → Seans bilgisi (örn: "10 Seans")

Bolum → Hastanın başvurduğu bölüm

KanGrubu → A, B, AB, 0 (+/-)

UygulamaYerleri → Uygulama yapılan bölgeler

Alerji → Belirtilen alerjiler

----------------------------------------------------------------------------------------------------------------------------------------

Üretilen Analizler

Temel istatistikler (toplam hasta sayısı, kayıt sayısı, yaş ortalaması vb.)

Duplicate analizi

Cinsiyet dağılımı ve yaş ortalamaları

Yaş analizi (min, max, medyan, standart sapma)

Yaş grupları (0-17, 18-29, 30-44, 45-59, 60-74, 75+)

Kronik hastalıklar (en yaygın 10 hastalık, ortalama sayı)

Tanılar (en yaygın 10 tanı)

Tedaviler (en yaygın 10 tedavi, ortalama seans sayısı)


Bölümler (en çok başvurulan 8 bölüm)

Kan grupları dağılımı

Uygulama yerleri (en çok kullanılan 8 bölge)

Alerjiler (en yaygın 10 alerji)

Korelasyon analizi (yaş ↔ seans, yaş ↔ kronik hastalık)

----------------------------------------------------------------------------------------------------------------------------------------

Kaydedilen Grafikler (PNG)


cinsiyet_dagilimi.png

yas_dagilimi.png

yas_gruplari.png

kronik_hastaliklar.png

tani_dagilimi.png


tedavi_dagilimi.png

bolum_dagilimi.png

kan_grubu_dagilimi.png

korelasyon_matrisi.png

kronik_hastalik_sayisi.png

seans_sayisi_dagilimi.png

uygulama_yerleri.png

alerji_dagilimi.png

----------------------------------------------------------------------------------------------------------------------------------------

Çalışma Mantığı

Excel’den veri okunur (pandas)

Veri temizlenir ve kategorilere ayrılır (yaş grupları, kronik hastalık listeleri, seans sayıları vb.)

İstatistiksel hesaplamalar yapılır (ortalama, medyan, korelasyon)

Sonuçlar terminale yazdırılır

Grafikler oluşturulur ve PNG formatında kaydedilir

----------------------------------------------------------------------------------------------------------------------------------------

Terminal Outputu

🔥 TALENT ACADEMY - DETAYLI İSTATİSTİK RAPORU 🔥
============================================================
📊 TEMEL İSTATİSTİKLER
============================================================
📍 Toplam Kayıt Sayısı: 1,297
👥 Toplam Hasta Sayısı: 404
📅 Veri Aralığı: 145134 - 145537
============================================================

🔍 DUPLICATE ANALİZİ
============================================================
🔁 Tamamen Aynı Kayıt Sayısı: 0
👥 Aynı Hasta Numarasına Sahip Kayıt Sayısı: 893
📈 Duplicate Oranı: 0.00%
============================================================

👥 CİNSİYET İSTATİSTİKLERİ
============================================================
👩 Kadın Hasta Sayısı: 718
👨 Erkek Hasta Sayısı: 477
📊 Kadın Hasta Yaş Ortalaması: 47.8
📊 Erkek Hasta Yaş Ortalaması: 47.5
📈 Genel Yaş Ortalaması: 47.3
============================================================

🎂 YAŞ DAĞILIMI
============================================================
🔽 Minimum Yaş: 2
🔼 Maksimum Yaş: 92
📏 Medyan Yaş: 46.0
📊 Standart Sapma: 15.5

👥 YAŞ GRUPLARI:
   30-44 (Yetişkin): 463 hasta
   45-59 (Orta Yaş): 450 hasta
   60-74 (İleri Yaş): 198 hasta
   18-29 (Genç): 77 hasta
   75+ (Yaşlı): 60 hasta
   0-17 (Çocuk): 49 hasta
============================================================

🏥 KRONİK HASTALIK ANALİZİ
============================================================
🔝 EN ÇOK GÖRÜLEN 10 KRONİK HASTALIK:
    1. Limb-Girdle Musküler Distrofi: 228 hasta
    2. Aritmi: 226 hasta
    3. Hiportiroidizm: 223 hasta
    4. Astım: 201 hasta
    5. Hipertiroidizm: 188 hasta
    6. Duchenne Musküler Distrofisi: 182 hasta
    7. Myastenia gravis: 180 hasta
    8. Hipertansiyon: 175 hasta
    9. Kalp yetmezliği: 171 hasta
   10. Fascioscapulohumeral Distrofi: 170 hasta

📊 Ortalama Kronik Hastalık Sayısı: 1.9
🔽 Minimum Kronik Hastalık: 0
🔼 Maksimum Kronik Hastalık: 4
============================================================

📋 TANI ANALİZİ
============================================================
🔝 EN ÇOK KARŞILAŞILAN 10 TANI:
    1. DORSALJİ: 372 hasta
    2. DİĞER: 360 hasta
    3. tanımlanmamış: 219 hasta
    4. Omuzun darbe sendromu: 159 hasta
    5. İntervertebral disk bozuklukları: 128 hasta
    6. LUMBOSAKRAL BÖLGE: 127 hasta
    7. SERVİKOTORASİK BÖLGE: 116 hasta
    8. SERVİKAL BÖLGE: 90 hasta
    9. Eklem ağrısı: 67 hasta
   10. Dorsalji: 57 hasta
============================================================

💊 TEDAVİ ANALİZİ
============================================================
🔝 EN ÇOK UYGULANAN 10 TEDAVİ:
    1. Dorsalji -Boyun+trapez: 119 uygulama
    2. İV DİSK BOZUKLUĞU-BEL: 104 uygulama
    3. Dorsalji 1: 58 uygulama
    4. Gonartroz-Meniskopati: 54 uygulama
    5. Dorsalji-Bel: 54 uygulama
    6. SAĞ OMUZ İMPİNGEMENT: 46 uygulama
    7. Sol omuz İmpingement: 33 uygulama
    8. Dorsalji-Dorsal: 30 uygulama
    9. Boyun-Trapezz: 29 uygulama
   10. Alt ekstremite atrofi-Bilateral: 28 uygulama

⏰ Ortalama Seans Sayısı: 14.2
🔽 Minimum Seans: 1
🔼 Maksimum Seans: 37
============================================================

🏥 BÖLÜM ANALİZİ
============================================================
📊 BÖLÜMLERE GÖRE HASTA DAĞILIMI:
   Fiziksel Tıp Ve Rehabilitasyon,Solunum Merkezi: 1147 hasta
   Ortopedi Ve Travmatoloji: 78 hasta
   İç Hastalıkları: 22 hasta
   Nöroloji: 13 hasta
   Kardiyoloji: 9 hasta
   Genel Cerrahi: 5 hasta
   Laboratuar: 5 hasta
   Göğüs Hastalıkları: 5 hasta
============================================================

💉 KAN GRUBU ANALİZİ
============================================================
🩸 KAN GRUPLARI DAĞILIMI:
   0 Rh+: 352 hasta
   A Rh+: 319 hasta
   B Rh+: 122 hasta
   AB Rh+: 51 hasta
   B Rh-: 40 hasta
   A Rh-: 29 hasta
   0 Rh-: 17 hasta
   AB Rh-: 6 hasta
============================================================

📍 UYGULAMA YERLERİ ANALİZİ
============================================================
🔝 EN ÇOK UYGULAMA YAPILAN 8 BÖLGE:
    1. Bel: 267 uygulama
    2. Boyun: 201 uygulama
    3. Diz: 105 uygulama
    4. Sağ Omuz Bölgesi: 90 uygulama
    5. Sol Omuz Bölgesi: 74 uygulama
    6. Tüm Vücut Bölgesi: 61 uygulama
    7. Sol El Bilek Bölgesi: 55 uygulama
    8. Sırt: 53 uygulama
============================================================

🤧 ALERJİ ANALİZİ
============================================================
🔝 EN ÇOK GÖRÜLEN 10 ALERJİ:
    1. Polen: 115 hasta
    2. POLEN: 77 hasta
    3. Toz: 68 hasta
    4. NOVALGIN: 59 hasta
    5. Sucuk: 54 hasta
    6. ARVELES,CORASPIN: 54 hasta
    7. Polen,Yer Fıstığı: 50 hasta
    8. TOZ: 46 hasta
    9. SUCUK: 46 hasta
   10. Novalgin: 28 hasta
============================================================

📈 KORELASYON ANALİZİ
============================================================
📊 Yaş - Seans Sayısı Korelasyonu: -0.021
📊 Yaş - Kronik Hastalık Korelasyonu: -0.053
============================================================

🎯 ÖZET RAPOR
============================================================
👥 Toplam Hasta: 404
📊 Ortalama Yaş: 47.3
🏥 Ortalama Kronik Hastalık: 1.9
⏰ Ortalama Seans: 14.2
👩 Kadın/Oran: 718 (55.4%)
👨 Erkek/Oran: 477 (36.8%)
============================================================

🔥 RAPOR TAMAMLANDI! 🚀
📊 Detaylı analizler için görseller oluşturuluyor...
============================================================
🎯 TÜM İSTATİSTİKLER TERMINAL'DE GÖSTERİLDİ!
📊 13 FARKLI GRAFİK PNG FORMATINDA KAYDEDİLDİ!
💪 ANALİZ TAMAMLANDI!
============================================================
