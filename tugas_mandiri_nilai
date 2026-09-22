import streamlit as st
import csv
import os
import pandas as pd

# ======================================================
# TUGAS MANDIRI - Aplikasi Pencatat Nilai Siswa (Versi UI Kekinian)
# Fitur: tema gelap/terang, kartu status berwarna, statistik, pencarian, grafik, reset
# ======================================================

FILE_CSV = "tugas_mandiri_nilai.csv"

st.set_page_config(
    page_title="Pencatat Nilai Siswa",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- STATE TEMA ----------
if "tema" not in st.session_state:
    st.session_state.tema = "Terang"

# ---------- SIDEBAR: PILIH TEMA ----------
with st.sidebar:
    st.markdown("### ⚙️ Pengaturan Tampilan")
    st.session_state.tema = st.radio(
        "Pilih tema",
        options=["Terang", "Gelap"],
        index=0 if st.session_state.tema == "Terang" else 1,
        horizontal=True
    )

# ---------- CSS DINAMIS SESUAI TEMA ----------
if st.session_state.tema == "Gelap":
    bg_color = "#0e1117"
    card_bg = "#1c1f26"
    text_color = "#f0f2f6"
    subtext_color = "#a0a6b1"
    accent = "#7c9cff"
    border_color = "#2a2e37"
else:
    bg_color = "#f7f9fc"
    card_bg = "#ffffff"
    text_color = "#1a1a1a"
    subtext_color = "#5a5a5a"
    accent = "#4361ee"
    border_color = "#e5e9f2"

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .main-header {{
        text-align: center;
        padding: 1.8rem 1rem;
        background: linear-gradient(135deg, {accent} 0%, #7209b7 100%);
        border-radius: 18px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }}
    .main-header h1 {{
        color: white !important;
        font-size: 1.8rem;
        margin: 0;
    }}
    .main-header p {{
        color: rgba(255,255,255,0.85) !important;
        margin: 0.3rem 0 0 0;
        font-size: 0.95rem;
    }}
    .card {{
        background-color: {card_bg};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }}
    .card h3 {{
        margin-top: 0;
        color: {text_color};
    }}
    .status-box {{
        padding: 1rem 1.2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.05rem;
        margin-top: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }}
    .status-lulus {{
        background-color: rgba(34, 197, 94, 0.15);
        color: #16a34a;
        border: 1px solid rgba(34, 197, 94, 0.4);
    }}
    .status-belum {{
        background-color: rgba(239, 68, 68, 0.15);
        color: #dc2626;
        border: 1px solid rgba(239, 68, 68, 0.4);
    }}
    .subtext {{
        color: {subtext_color};
        font-size: 0.9rem;
    }}
    div[data-testid="stMetric"] {{
        background-color: {card_bg};
        border: 1px solid {border_color};
        border-radius: 14px;
        padding: 0.9rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}
    .stButton > button {{
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
        transition: all 0.2s ease;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
    <div class="main-header">
        <h1>📚 Aplikasi Pencatat Nilai Siswa</h1>
        <p>Catat, pantau, dan analisis nilai siswa dengan tampilan yang lebih rapi ✨</p>
    </div>
""", unsafe_allow_html=True)

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
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### ➕ Tambah Data Siswa")
col_a, col_b = st.columns([2, 1])
with col_a:
    nama = st.text_input("Nama siswa", placeholder="Contoh: Budi Santoso")
with col_b:
    nilai = st.number_input("Nilai", min_value=0, max_value=100, step=1)

if st.button("💾 Simpan Data", use_container_width=True):
    if nama.strip() == "":
        st.warning("⚠️ Nama siswa tidak boleh kosong.")
    else:
        status = tentukan_status(nilai)
        simpan_data(nama, nilai, status)

        if status == "Lulus":
            st.markdown(f"""
                <div class="status-box status-lulus">
                    ✅ Data <b>{nama}</b> (nilai {nilai}) berhasil disimpan — Status: <b>LULUS</b>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="status-box status-belum">
                    ❌ Data <b>{nama}</b> (nilai {nilai}) berhasil disimpan — Status: <b>BELUM LULUS</b>
                </div>
            """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- BACA DATA ----------
data = baca_semua_data()

# ---------- STATISTIK ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📊 Statistik Kelas")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Jumlah Siswa", len(data))

with col2:
    rata_rata = hitung_rata_rata(data)
    st.metric("📈 Rata-rata Nilai", f"{rata_rata:.2f}")

with col3:
    jumlah_lulus = sum(1 for b in data if b[2] == "Lulus")
    jumlah_belum = len(data) - jumlah_lulus
    st.metric("🎯 Lulus / Belum", f"{jumlah_lulus} / {jumlah_belum}")

if len(data) > 0:
    chart_df = pd.DataFrame({
        "Status": ["Lulus", "Belum Lulus"],
        "Jumlah": [jumlah_lulus, jumlah_belum]
    }).set_index("Status")
    st.bar_chart(chart_df, color=["#22c55e"])
st.markdown('</div>', unsafe_allow_html=True)

# ---------- PENCARIAN ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🔍 Cari Siswa")
kata_kunci = st.text_input("Cari berdasarkan nama", placeholder="Ketik nama siswa...")

if kata_kunci.strip() != "":
    hasil = [b for b in data if kata_kunci.lower() in b[0].lower()]
    if hasil:
        st.markdown(f'<p class="subtext">Ditemukan {len(hasil)} data untuk "{kata_kunci}"</p>', unsafe_allow_html=True)
        df_hasil = pd.DataFrame(hasil, columns=["Nama", "Nilai", "Status"])
        st.dataframe(df_hasil, use_container_width=True, hide_index=True)
    else:
        st.info("Tidak ada siswa dengan nama tersebut.")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- RIWAYAT DATA & RESET ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📋 Riwayat Data Siswa")
if data:
    df_semua = pd.DataFrame(data, columns=["Nama", "Nilai", "Status"])

    def warnai_status(val):
        if val == "Lulus":
            return "background-color: rgba(34,197,94,0.15); color: #16a34a; font-weight: 600;"
        else:
            return "background-color: rgba(239,68,68,0.15); color: #dc2626; font-weight: 600;"

    styled_df = df_semua.style.map(warnai_status, subset=["Status"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
else:
    st.info("Belum ada data yang disimpan.")

if st.button("🗑️ Hapus Semua Data", use_container_width=True):
    if os.path.exists(FILE_CSV):
        os.remove(FILE_CSV)
    st.success("Semua data berhasil dihapus. Silakan refresh halaman.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f'<p class="subtext" style="text-align:center; margin-top:1rem;">Dibuat dengan ❤️ menggunakan Streamlit</p>', unsafe_allow_html=True)
