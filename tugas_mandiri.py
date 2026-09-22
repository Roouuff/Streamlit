import streamlit as st
import csv
import os

# ======================================================
# TUGAS MANDIRI - Aplikasi Pencatat Nilai Siswa (Pengembangan)
# Fitur tambahan: rata-rata nilai, pencarian nama, grafik Lulus vs Belum Lulus, reset data
# ======================================================

FILE_CSV = "tugas_mandiri_nilai.csv"

st.title("📚 Aplikasi Pencatat Nilai Siswa (Versi Pengembangan)")
st.write("Selamat datang! Silakan isi data siswa, cari data, dan lihat statistik kelas di bawah ini.")

# ---------- FUNGSI ----------
def tentukan_status(nilai):
    """Percabangan: menentukan status Lulus/Belum Lulus berdasarkan nilai."""
    if nilai >= 75:
        return "Lulus"
    else:
        return "Belum Lulus"

def simpan_data(nama, nilai, status):
    """Menyimpan satu baris data ke file CSV."""
    file_baru = not os.path.exists(FILE_CSV)
    with open(FILE_CSV, mode="a", newline="") as f:
        writer = csv.writer(f)
        if file_baru:
            writer.writerow(["Nama", "Nilai", "Status"])
        writer.writerow([nama, nilai, status])

def baca_semua_data():
    """Membaca seluruh data dari CSV, mengembalikan list baris (tanpa header)."""
    data = []
    if os.path.exists(FILE_CSV):
        with open(FILE_CSV) as f:
            reader = csv.reader(f)
            next(reader, None)  # lewati header
            for baris in reader:   # Perulangan (for)
                if len(baris) == 3:
                    data.append(baris)
    return data

def hitung_rata_rata(data):
    """Menghitung rata-rata nilai dari seluruh data siswa."""
    if len(data) == 0:
        return 0
    total = 0
    for baris in data:   # Perulangan (for)
        total += float(baris[1])
    return total / len(data)

# ---------- INPUT ----------
st.subheader("➕ Tambah Data Siswa")
nama = st.text_input("Nama siswa")
nilai = st.number_input("Nilai", min_value=0, max_value=100, step=1)

if st.button("Simpan"):
    if nama.strip() == "":
        st.warning("Nama siswa tidak boleh kosong.")
    else:
        status = tentukan_status(nilai)
        simpan_data(nama, nilai, status)
        st.success(f"Data {nama} berhasil disimpan dengan status: {status}")

# ---------- BACA DATA ----------
data = baca_semua_data()

# ---------- STATISTIK ----------
st.subheader("📊 Statistik Kelas")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Siswa", len(data))

with col2:
    rata_rata = hitung_rata_rata(data)
    st.metric("Rata-rata Nilai", f"{rata_rata:.2f}")

with col3:
    jumlah_lulus = sum(1 for b in data if b[2] == "Lulus")
    jumlah_belum = len(data) - jumlah_lulus
    st.metric("Lulus / Belum Lulus", f"{jumlah_lulus} / {jumlah_belum}")

if len(data) > 0:
    chart_data = {"Lulus": jumlah_lulus, "Belum Lulus": jumlah_belum}
    st.bar_chart(chart_data)

# ---------- PENCARIAN ----------
st.subheader("🔍 Cari Siswa")
kata_kunci = st.text_input("Cari berdasarkan nama")

if kata_kunci.strip() != "":
    hasil = [b for b in data if kata_kunci.lower() in b[0].lower()]
    if hasil:
        st.write(f"Ditemukan {len(hasil)} data untuk '{kata_kunci}':")
        st.dataframe(hasil, use_container_width=True)
    else:
        st.info("Tidak ada siswa dengan nama tersebut.")

# ---------- RIWAYAT DATA & RESET ----------
st.subheader("📋 Riwayat Data Siswa")
if data:
    st.dataframe(data, use_container_width=True)
else:
    st.info("Belum ada data yang disimpan.")

if st.button("🗑️ Hapus Semua Data"):
    if os.path.exists(FILE_CSV):
        os.remove(FILE_CSV)
    st.success("Semua data berhasil dihapus. Silakan refresh halaman.")
