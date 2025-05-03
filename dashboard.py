import pandas as pd
import matplotlib.pyplot as plt
import os

# Wczytanie danych
df = pd.read_csv('sales_data.csv')

# Konwersja kolumny 'Data' do typu daty
df['Data'] = pd.to_datetime(df['Data'])

# Tworzenie folderu na wykresy, jeśli nie istnieje
if not os.path.exists('wykresy'):
    os.makedirs('wykresy')

# 🔹 Analiza 1: Top 5 produktów wg przychodu
top_produkty = df.groupby('Produkt')['Przychod'].sum().sort_values(ascending=False).head(5)

# Wykres słupkowy
plt.figure(figsize=(8, 5))
top_produkty.plot(kind='bar', color='skyblue')
plt.title('Top 5 produktów wg przychodu')
plt.ylabel('Przychód (PLN)')
plt.tight_layout()
plt.savefig('wykresy/top_produkty.png')
plt.close()

# 🔹 Analiza 2: Przychód miesięczny
df['Miesiac'] = df['Data'].dt.to_period('M')
miesieczny_przychod = df.groupby('Miesiac')['Przychod'].sum()

# Wykres liniowy
plt.figure(figsize=(10, 5))
miesieczny_przychod.plot(marker='o')
plt.title('Przychód miesięczny')
plt.ylabel('Przychód (PLN)')
plt.xlabel('Miesiąc')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('wykresy/przychody_miesieczne.png')
plt.close()

print("Wykresy zostały zapisane w folderze 'wykresy'.")
