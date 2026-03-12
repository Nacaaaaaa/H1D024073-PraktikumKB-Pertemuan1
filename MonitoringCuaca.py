import random      # Library untuk mengambil suhu secara acak
import statistics  # Library untuk menghitung rata-rata

def main():
    print("=== PROGRAM MONITORING CUACA ===")

    # Struktur data riawayat suhu selama seminggu terakhir
    riwayat_suhu = [25, 28, 30, 27, 29, 31, 26]
    
    # mengambil suhu secara acak antara 20 hingga 35 untuk hari ini
    suhu_hari_ini = random.randint(20, 35)
    # menambahkan suhu hari ini ke dalam data
    riwayat_suhu.append(suhu_hari_ini)

    # mengitung rata-rata suhu selama seminggu terakhir yang telah diperbarui dengan suhu hari ini
    rata_rata = statistics.mean(riwayat_suhu)

    print(f"Suhu hari ini: {suhu_hari_ini}°C")
    print(f"Rata-rata suhu seminggu terakhir: {rata_rata:.1f}°C")

    # Struktur kontrol pengambilan keputusan berdasarkan suhu hari ini
    if suhu_hari_ini > 30:
        kondisi = "Panas Terik"
        komentar = "Yaudah sih dirumah aja, gausah keluar rumah."
    elif 25 <= suhu_hari_ini <= 30:
        kondisi = "Normal"
        komentar = "Chill aja dawg."
    else:
        kondisi = "Dingin/Mendung/Hujan"
        komentar = "Turu enak nih."

    print(f"Kondisi: {kondisi}")
    print(f"Komentar: {komentar}")

if __name__ == "__main__":
    main()
