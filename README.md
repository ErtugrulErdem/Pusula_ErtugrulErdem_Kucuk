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
