import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import re
from matplotlib import cm
import warnings
warnings.filterwarnings('ignore')

# Stil ayarları
plt.style.use('default')
sns.set_palette("husl")

# Veriyi yükle
df = pd.read_excel("Talent_Academy_Case_DT_2025.xlsx", sheet_name="Sheet1")

print("🔥 TALENT ACADEMY - DETAYLI İSTATİSTİK RAPORU 🔥")
print("=" * 60)

# TEMEL İSTATİSTİKLER
print("📊 TEMEL İSTATİSTİKLER")
print("=" * 60)
print(f"📍 Toplam Kayıt Sayısı: {len(df):,}")
print(f"👥 Toplam Hasta Sayısı: {df['HastaNo'].nunique():,}")
print(f"📅 Veri Aralığı: {df['HastaNo'].min()} - {df['HastaNo'].max()}")
print("=" * 60)

# DUPLICATE ANALİZİ
print("\n🔍 DUPLICATE ANALİZİ")
print("=" * 60)
duplicate_rows = df.duplicated().sum()
duplicate_hasta = df.duplicated(subset=['HastaNo']).sum()
print(f"🔁 Tamamen Aynı Kayıt Sayısı: {duplicate_rows}")
print(f"👥 Aynı Hasta Numarasına Sahip Kayıt Sayısı: {duplicate_hasta}")
print(f"📈 Duplicate Oranı: {(duplicate_rows/len(df))*100:.2f}%")
print("=" * 60)

# CİNSİYET İSTATİSTİKLERİ
print("\n👥 CİNSİYET İSTATİSTİKLERİ")
print("=" * 60)
cinsiyet_dagilim = df['Cinsiyet'].value_counts()
print(f"👩 Kadın Hasta Sayısı: {cinsiyet_dagilim.get('Kadın', 0)}")
print(f"👨 Erkek Hasta Sayısı: {cinsiyet_dagilim.get('Erkek', 0)}")

# Yaş istatistikleri
kadin_yas = df[df['Cinsiyet'] == 'Kadın']['Yas'].mean()
erkek_yas = df[df['Cinsiyet'] == 'Erkek']['Yas'].mean()

print(f"📊 Kadın Hasta Yaş Ortalaması: {kadin_yas:.1f}")
print(f"📊 Erkek Hasta Yaş Ortalaması: {erkek_yas:.1f}")
print(f"📈 Genel Yaş Ortalaması: {df['Yas'].mean():.1f}")
print("=" * 60)

# YAŞ ANALİZİ
print("\n🎂 YAŞ DAĞILIMI")
print("=" * 60)
print(f"🔽 Minimum Yaş: {df['Yas'].min():.0f}")
print(f"🔼 Maksimum Yaş: {df['Yas'].max():.0f}")
print(f"📏 Medyan Yaş: {df['Yas'].median():.1f}")
print(f"📊 Standart Sapma: {df['Yas'].std():.1f}")

# Yaş grupları
def yas_grubu(yas):
    if pd.isna(yas): return 'Bilinmiyor'
    if yas < 18: return '0-17 (Çocuk)'
    elif yas < 30: return '18-29 (Genç)'
    elif yas < 45: return '30-44 (Yetişkin)'
    elif yas < 60: return '45-59 (Orta Yaş)'
    elif yas < 75: return '60-74 (İleri Yaş)'
    else: return '75+ (Yaşlı)'

df['YasGrubu'] = df['Yas'].apply(yas_grubu)
yas_grup_dagilim = df['YasGrubu'].value_counts()

print("\n👥 YAŞ GRUPLARI:")
for grup, sayi in yas_grup_dagilim.items():
    print(f"   {grup}: {sayi} hasta")
print("=" * 60)

# KRONİK HASTALIK ANALİZİ
print("\n🏥 KRONİK HASTALIK ANALİZİ")
print("=" * 60)

def extract_diseases(text):
    if pd.isna(text): return []
    diseases = [disease.strip() for disease in str(text).split(',')]
    return [d for d in diseases if d]

all_diseases = []
for diseases in df['KronikHastalik'].apply(extract_diseases):
    all_diseases.extend(diseases)

disease_counts = Counter(all_diseases)
top_10_diseases = disease_counts.most_common(10)

print("🔝 EN ÇOK GÖRÜLEN 10 KRONİK HASTALIK:")
for i, (disease, count) in enumerate(top_10_diseases, 1):
    print(f"   {i:2d}. {disease}: {count} hasta")

# Kronik hastalık sayısı
df['KronikHastalikSayisi'] = df['KronikHastalik'].apply(lambda x: len(extract_diseases(x)) if pd.notna(x) else 0)
print(f"\n📊 Ortalama Kronik Hastalık Sayısı: {df['KronikHastalikSayisi'].mean():.1f}")
print(f"🔽 Minimum Kronik Hastalık: {df['KronikHastalikSayisi'].min()}")
print(f"🔼 Maksimum Kronik Hastalık: {df['KronikHastalikSayisi'].max()}")
print("=" * 60)

# TANI ANALİZİ
print("\n📋 TANI ANALİZİ")
print("=" * 60)

def extract_diagnoses(text):
    if pd.isna(text): return []
    diagnoses = [diag.strip() for diag in str(text).split(',')]
    return [d for d in diagnoses if d]

all_diagnoses = []
for diagnoses in df['Tanilar'].apply(extract_diagnoses):
    all_diagnoses.extend(diagnoses)

diagnosis_counts = Counter(all_diagnoses)
top_10_diagnoses = diagnosis_counts.most_common(10)

print("🔝 EN ÇOK KARŞILAŞILAN 10 TANI:")
for i, (diagnosis, count) in enumerate(top_10_diagnoses, 1):
    print(f"   {i:2d}. {diagnosis}: {count} hasta")
print("=" * 60)

# TEDAVİ ANALİZİ
print("\n💊 TEDAVİ ANALİZİ")
print("=" * 60)

def extract_session_count(text):
    if pd.isna(text): return None
    match = re.search(r'(\d+)\s*Seans', str(text))
    return int(match.group(1)) if match else None

df['Seans_Sayisi'] = df['TedaviSuresi'].apply(extract_session_count)

# Tedavi türleri
tedavi_dagilim = df['TedaviAdi'].value_counts().head(10)
print("🔝 EN ÇOK UYGULANAN 10 TEDAVİ:")
for i, (tedavi, count) in enumerate(tedavi_dagilim.items(), 1):
    print(f"   {i:2d}. {tedavi}: {count} uygulama")

print(f"\n⏰ Ortalama Seans Sayısı: {df['Seans_Sayisi'].mean():.1f}")
print(f"🔽 Minimum Seans: {df['Seans_Sayisi'].min()}")
print(f"🔼 Maksimum Seans: {df['Seans_Sayisi'].max()}")
print("=" * 60)

# BÖLÜM ANALİZİ
print("\n🏥 BÖLÜM ANALİZİ")
print("=" * 60)
bolum_dagilim = df['Bolum'].value_counts().head(8)
print("📊 BÖLÜMLERE GÖRE HASTA DAĞILIMI:")
for bolum, sayi in bolum_dagilim.items():
    print(f"   {bolum}: {sayi} hasta")
print("=" * 60)

# KAN GRUBU ANALİZİ
print("\n💉 KAN GRUBU ANALİZİ")
print("=" * 60)
kan_grubu_dagilim = df['KanGrubu'].value_counts()
print("🩸 KAN GRUPLARI DAĞILIMI:")
for kan_grubu, sayi in kan_grubu_dagilim.items():
    print(f"   {kan_grubu}: {sayi} hasta")
print("=" * 60)

# UYGULAMA YERLERİ ANALİZİ
print("\n📍 UYGULAMA YERLERİ ANALİZİ")
print("=" * 60)

def extract_locations(text):
    if pd.isna(text): return []
    locations = [loc.strip() for loc in str(text).split(',')]
    return [loc for loc in locations if loc]

all_locations = []
for locations in df['UygulamaYerleri'].apply(extract_locations):
    all_locations.extend(locations)

location_counts = Counter(all_locations)
top_locations = location_counts.most_common(8)

print("🔝 EN ÇOK UYGULAMA YAPILAN 8 BÖLGE:")
for i, (location, count) in enumerate(top_locations, 1):
    print(f"   {i:2d}. {location}: {count} uygulama")
print("=" * 60)

# ALERJİ ANALİZİ
print("\n🤧 ALERJİ ANALİZİ")
print("=" * 60)
alerji_dagilim = df['Alerji'].value_counts().head(10)
print("🔝 EN ÇOK GÖRÜLEN 10 ALERJİ:")
for i, (alerji, count) in enumerate(alerji_dagilim.items(), 1):
    if pd.notna(alerji) and alerji != '':
        print(f"   {i:2d}. {alerji}: {count} hasta")
print("=" * 60)

# KORELASYON ANALİZİ
print("\n📈 KORELASYON ANALİZİ")
print("=" * 60)
numeric_df = df[['Yas', 'Seans_Sayisi', 'KronikHastalikSayisi']].corr()
yas_seans_korelasyon = numeric_df.iloc[0, 1]
yas_hastalik_korelasyon = numeric_df.iloc[0, 2]
print(f"📊 Yaş - Seans Sayısı Korelasyonu: {yas_seans_korelasyon:.3f}")
print(f"📊 Yaş - Kronik Hastalık Korelasyonu: {yas_hastalik_korelasyon:.3f}")
print("=" * 60)

# ÖZET RAPOR
print("\n🎯 ÖZET RAPOR")
print("=" * 60)
print(f"👥 Toplam Hasta: {df['HastaNo'].nunique():,}")
print(f"📊 Ortalama Yaş: {df['Yas'].mean():.1f}")
print(f"🏥 Ortalama Kronik Hastalık: {df['KronikHastalikSayisi'].mean():.1f}")
print(f"⏰ Ortalama Seans: {df['Seans_Sayisi'].mean():.1f}")
print(f"👩 Kadın/Oran: {cinsiyet_dagilim.get('Kadın', 0)} ({(cinsiyet_dagilim.get('Kadın', 0)/len(df)*100):.1f}%)")
print(f"👨 Erkek/Oran: {cinsiyet_dagilim.get('Erkek', 0)} ({(cinsiyet_dagilim.get('Erkek', 0)/len(df)*100):.1f}%)")
print("=" * 60)

print("\n🔥 RAPOR TAMAMLANDI! 🚀")
print("📊 Detaylı analizler için görseller oluşturuluyor...")
print("=" * 60)

# GÖRSELLERİ OLUŞTUR
# 1. CİNSİYET DAĞILIMI GRAFİĞİ
plt.figure(figsize=(10, 6))
cinsiyet_dagilim = df['Cinsiyet'].value_counts()
plt.pie(cinsiyet_dagilim.values, labels=cinsiyet_dagilim.index, autopct='%1.1f%%', startangle=90)
plt.title('Cinsiyet Dağılımı', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('cinsiyet_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. YAŞ DAĞILIMI HISTOGRAMI
plt.figure(figsize=(10, 6))
plt.hist(df['Yas'].dropna(), bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.title('Yaş Dağılımı', fontsize=16, fontweight='bold')
plt.xlabel('Yaş')
plt.ylabel('Hasta Sayısı')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('yas_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. YAŞ GRUPLARI ÇUBUK GRAFİĞİ
plt.figure(figsize=(12, 6))
yas_grup_dagilim = df['YasGrubu'].value_counts()
yas_grup_dagilim.plot(kind='bar', color='lightcoral')
plt.title('Yaş Gruplarına Göre Dağılım', fontsize=16, fontweight='bold')
plt.xlabel('Yaş Grupları')
plt.ylabel('Hasta Sayısı')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('yas_gruplari.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. KRONİK HASTALIKLAR GRAFİĞİ
plt.figure(figsize=(12, 8))
all_diseases = []
for diseases in df['KronikHastalik'].apply(extract_diseases):
    all_diseases.extend(diseases)
disease_counts = Counter(all_diseases)
top_10_diseases = disease_counts.most_common(10)

diseases_df = pd.DataFrame(top_10_diseases, columns=['Hastalık', 'Sayı'])
plt.barh(range(len(diseases_df)), diseases_df['Sayı'], color='lightgreen')
plt.yticks(range(len(diseases_df)), diseases_df['Hastalık'])
plt.title('En Yaygın 10 Kronik Hastalık', fontsize=16, fontweight='bold')
plt.xlabel('Hasta Sayısı')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.75)
plt.tight_layout()
plt.savefig('kronik_hastaliklar.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. TANI DAĞILIMI GRAFİĞİ
plt.figure(figsize=(12, 8))
all_diagnoses = []
for diagnoses in df['Tanilar'].apply(extract_diagnoses):
    all_diagnoses.extend(diagnoses)
diagnosis_counts = Counter(all_diagnoses)
top_10_diagnoses = diagnosis_counts.most_common(10)

diagnoses_df = pd.DataFrame(top_10_diagnoses, columns=['Tanı', 'Sayı'])
plt.barh(range(len(diagnoses_df)), diagnoses_df['Sayı'], color='orange')
plt.yticks(range(len(diagnoses_df)), diagnoses_df['Tanı'])
plt.title('En Yaygın 10 Tanı', fontsize=16, fontweight='bold')
plt.xlabel('Hasta Sayısı')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.75)
plt.tight_layout()
plt.savefig('tani_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 6. TEDAVİ DAĞILIMI GRAFİĞİ
plt.figure(figsize=(12, 8))
tedavi_dagilim = df['TedaviAdi'].value_counts().head(10)
tedavi_df = pd.DataFrame(tedavi_dagilim).reset_index()
tedavi_df.columns = ['Tedavi', 'Sayı']

plt.barh(range(len(tedavi_df)), tedavi_df['Sayı'], color='purple')
plt.yticks(range(len(tedavi_df)), tedavi_df['Tedavi'])
plt.title('En Yaygın 10 Tedavi', fontsize=16, fontweight='bold')
plt.xlabel('Uygulama Sayısı')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.75)
plt.tight_layout()
plt.savefig('tedavi_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 7. BÖLÜM DAĞILIMI GRAFİĞİ
plt.figure(figsize=(12, 8))
bolum_dagilim = df['Bolum'].value_counts().head(8)
bolum_df = pd.DataFrame(bolum_dagilim).reset_index()
bolum_df.columns = ['Bölüm', 'Sayı']

plt.barh(range(len(bolum_df)), bolum_df['Sayı'], color='teal')
plt.yticks(range(len(bolum_df)), bolum_df['Bölüm'])
plt.title('Bölümlere Göre Hasta Dağılımı', fontsize=16, fontweight='bold')
plt.xlabel('Hasta Sayısı')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.75)
plt.tight_layout()
plt.savefig('bolum_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 8. KAN GRUBU DAĞILIMI GRAFİĞİ
plt.figure(figsize=(10, 6))
kan_grubu_dagilim = df['KanGrubu'].value_counts()
kan_grubu_df = pd.DataFrame(kan_grubu_dagilim).reset_index()
kan_grubu_df.columns = ['Kan Grubu', 'Sayı']

plt.bar(kan_grubu_df['Kan Grubu'], kan_grubu_df['Sayı'], color='salmon')
plt.title('Kan Grupları Dağılımı', fontsize=16, fontweight='bold')
plt.xlabel('Kan Grubu')
plt.ylabel('Hasta Sayısı')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('kan_grubu_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 9. KORELASYON MATRİSİ GRAFİĞİ
plt.figure(figsize=(10, 8))
numeric_df = df[['Yas', 'Seans_Sayisi', 'KronikHastalikSayisi']].corr()
corr_matrix = numeric_df.corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=.5, cbar_kws={"shrink": .8})
plt.title('Korelasyon Matrisi', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('korelasyon_matrisi.png', dpi=300, bbox_inches='tight')
plt.show()

# 10. KRONİK HASTALIK SAYISI DAĞILIMI
plt.figure(figsize=(10, 6))
kronik_dagilim = df['KronikHastalikSayisi'].value_counts().sort_index()
plt.bar(kronik_dagilim.index, kronik_dagilim.values, color='lightblue', edgecolor='black')
plt.title('Kronik Hastalık Sayısı Dağılımı', fontsize=16, fontweight='bold')
plt.xlabel('Kronik Hastalık Sayısı')
plt.ylabel('Hasta Sayısı')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('kronik_hastalik_sayisi.png', dpi=300, bbox_inches='tight')
plt.show()

# 11. SEANS SAYISI DAĞILIMI
plt.figure(figsize=(10, 6))
seans_dagilim = df['Seans_Sayisi'].value_counts().sort_index()
plt.bar(seans_dagilim.index, seans_dagilim.values, color='lightpink', edgecolor='black')
plt.title('Seans Sayısı Dağılımı', fontsize=16, fontweight='bold')
plt.xlabel('Seans Sayısı')
plt.ylabel('Hasta Sayısı')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('seans_sayisi_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

# 12. UYGULAMA YERLERİ GRAFİĞİ
plt.figure(figsize=(12, 8))
all_locations = []
for locations in df['UygulamaYerleri'].apply(extract_locations):
    all_locations.extend(locations)
location_counts = Counter(all_locations)
top_locations = location_counts.most_common(8)

locations_df = pd.DataFrame(top_locations, columns=['Lokasyon', 'Sayı'])
plt.barh(range(len(locations_df)), locations_df['Sayı'], color='goldenrod')
plt.yticks(range(len(locations_df)), locations_df['Lokasyon'])
plt.title('En Çok Uygulama Yapılan 8 Bölge', fontsize=16, fontweight='bold')
plt.xlabel('Uygulama Sayısı')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.75)
plt.tight_layout()
plt.savefig('uygulama_yerleri.png', dpi=300, bbox_inches='tight')
plt.show()

# 13. ALERJİ DAĞILIMI GRAFİĞİ
plt.figure(figsize=(12, 8))
alerji_dagilim = df['Alerji'].value_counts().head(10)
alerji_df = pd.DataFrame(alerji_dagilim).reset_index()
alerji_df.columns = ['Alerji', 'Sayı']
alerji_df = alerji_df[alerji_df['Alerji'].notna() & (alerji_df['Alerji'] != '')]

plt.barh(range(len(alerji_df)), alerji_df['Sayı'], color='lightcoral')
plt.yticks(range(len(alerji_df)), alerji_df['Alerji'])
plt.title('En Yaygın 10 Alerji', fontsize=16, fontweight='bold')
plt.xlabel('Hasta Sayısı')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.75)
plt.tight_layout()
plt.savefig('alerji_dagilimi.png', dpi=300, bbox_inches='tight')
plt.show()

print("🎯 TÜM İSTATİSTİKLER TERMINAL'DE GÖSTERİLDİ!")
print("📊 13 FARKLI GRAFİK PNG FORMATINDA KAYDEDİLDİ!")
print("💪 ANALİZ TAMAMLANDI!")
print("=" * 60)