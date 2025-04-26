def hitung_kebutuhan_air(berat_badan, aktivitas, iklim):
    # Kebutuhan air dasar (menggunakan rata-rata 35 mL/kg/hari)
    kebutuhan_dasar = berat_badan * 35 / 1000  # dalam liter

    # Penyesuaian berdasarkan aktivitas
    if aktivitas == "ringan":
        penyesuaian_aktivitas = 0.15  # rata-rata dari 10-20%
    elif aktivitas == "sedang":
        penyesuaian_aktivitas = 0.25  # rata-rata dari 20-30%
    elif aktivitas == "berat":
        penyesuaian_aktivitas = 0.35  # rata-rata dari 30-40%
    else:
        print("Aktivitas tidak dikenali. Gunakan: ringan, sedang, atau berat.")
        return None

    # Penyesuaian berdasarkan iklim
    if iklim == "normal":
        penyesuaian_iklim = 0.0
    elif iklim == "panas":
        penyesuaian_iklim = 0.15  # rata-rata dari 10-20%
    else:
        print("Iklim tidak dikenali. Gunakan: normal atau panas.")
        return None

    # Total kebutuhan air setelah penyesuaian
    kebutuhan_setelah_aktivitas = kebutuhan_dasar * (1 + penyesuaian_aktivitas)
    total_kebutuhan = kebutuhan_setelah_aktivitas * (1 + penyesuaian_iklim)

    return round(total_kebutuhan, 2)


def main():
    print("=== Kalkulator Kebutuhan Air Harian ===")
    
    try:
        umur = int(input("Masukkan umur Anda (tahun): "))
        jenis_kelamin = input("Masukkan jenis kelamin (L/P): ").strip().upper()
        berat_badan = float(input("Masukkan berat badan Anda (kg): "))
        aktivitas = input("Tingkat aktivitas (ringan/sedang/berat): ").strip().lower()
        iklim = input("Iklim tempat tinggal (normal/panas): ").strip().lower()

        kebutuhan_air = hitung_kebutuhan_air(berat_badan, aktivitas, iklim)
        if kebutuhan_air:
            print(f"\n👉 Kebutuhan air harian yang direkomendasikan: {kebutuhan_air} liter/hari")
    except ValueError:
        print("Input tidak valid. Pastikan angka dimasukkan dengan benar.")


if __name__ == "__main__":
    main()
