
import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="ChemQual Premium",
    page_icon="🧪",
    layout="wide"
)

# =========================================================
# CUSTOM CSS (LIGHT MODE AESTHETIC)
# =========================================================
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.stApp {
    background: linear-gradient(to bottom right, #f8fafc, #e2e8f0);
}

.title-main {
    font-size: 42px;
    font-weight: 700;
    color: #0f172a;
}

.subtitle {
    font-size: 17px;
    color: #475569;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-2px);
}

.reaction-box {
    background: #eff6ff;
    padding: 10px;
    border-radius: 10px;
    border-left: 4px solid #38bdf8;
    font-family: monospace;
    color: #0f172a;
    margin-top: 10px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
    font-size: 14px;
}

.small-text {
    font-size: 15px;
    color: #334155;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATABASE UJI ORGANIK
# =========================================================
data_uji = [

    {
        "Nama Uji": "Uji Lucas",
        "Gugus Fungsi": "Alkohol",
        "Reagen": "HCl pekat + ZnCl2",
        "Prosedur": "Campurkan sampel dengan reagen Lucas.",
        "Hasil": "Terbentuk kekeruhan.",
        "Visual": "⚪ Keruh / 2 lapisan",
        "Reaksi": "R-OH + HCl → R-Cl + H2O"
    },

    {
        "Nama Uji": "Uji Tollens",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "AgNO3 + NH4OH",
        "Prosedur": "Panaskan dengan reagen Tollens.",
        "Hasil": "Cermin perak terbentuk.",
        "Visual": "🪞 Silver mirror",
        "Reaksi": "R-CHO → Ag(s)"
    },

    {
        "Nama Uji": "Uji Fehling",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "Fehling A + Fehling B",
        "Prosedur": "Panaskan campuran dengan sampel.",
        "Hasil": "Endapan merah bata.",
        "Visual": "🔴 Endapan merah",
        "Reaksi": "Cu²⁺ → Cu2O"
    },

    {
        "Nama Uji": "Uji Ferri Klorida",
        "Gugus Fungsi": "Fenol",
        "Reagen": "FeCl3",
        "Prosedur": "Tambahkan FeCl3 ke sampel.",
        "Hasil": "Warna ungu/biru/hijau.",
        "Visual": "🟣 Kompleks berwarna",
        "Reaksi": "Fenol + Fe³⁺"
    },

    {
        "Nama Uji": "Uji Baeyer",
        "Gugus Fungsi": "Alkena / Alkuna",
        "Reagen": "KMnO4",
        "Prosedur": "Tambahkan KMnO4 ke sampel.",
        "Hasil": "Warna ungu hilang.",
        "Visual": "🟤 Endapan coklat",
        "Reaksi": "KMnO4 → MnO2"
    },

    {
        "Nama Uji": "Uji Iodoform",
        "Gugus Fungsi": "Metil Keton / Etanol",
        "Reagen": "I2 + NaOH",
        "Prosedur": "Tambahkan iodin dan NaOH lalu panaskan perlahan.",
        "Hasil": "Terbentuk endapan kuning.",
        "Visual": "🟡 Endapan kuning iodoform",
        "Reaksi": "CH3CO- + I2 → CHI3"
    },

    {
        "Nama Uji": "Uji Benedict",
        "Gugus Fungsi": "Gula Pereduksi",
        "Reagen": "Larutan Benedict",
        "Prosedur": "Panaskan sampel dengan larutan Benedict.",
        "Hasil": "Warna berubah menjadi merah bata.",
        "Visual": "🟠 Endapan merah bata",
        "Reaksi": "Cu²⁺ → Cu2O"
    },

    {
        "Nama Uji": "Uji Bromin",
        "Gugus Fungsi": "Alkena",
        "Reagen": "Br2/CCl4",
        "Prosedur": "Tambahkan bromin ke sampel.",
        "Hasil": "Warna bromin hilang.",
        "Visual": "🟤 Warna coklat hilang",
        "Reaksi": "C=C + Br2 → C-C"
    }

]

df = pd.DataFrame(data_uji)

# =========================================================
# HEADER
# =========================================================
st.markdown(
    "<div class='title-main'>🧪 ChemQual Premium</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Katalog Modern Uji Kualitatif Senyawa Organik</div>",
    unsafe_allow_html=True
)

# =========================================================
# SEARCH
# =========================================================
st.markdown("### 🔍 Pencarian")

col1, col2 = st.columns(2)

with col1:
    gugus = st.selectbox(
        "Pilih Gugus Fungsi",
        ["Semua"] + list(df["Gugus Fungsi"].unique())
    )

with col2:
    keyword = st.text_input(
        "Cari nama uji / reagen",
        placeholder="Contoh: Tollens"
    )

filtered_df = df.copy()

if gugus != "Semua":
    filtered_df = filtered_df[
        filtered_df["Gugus Fungsi"] == gugus
    ]

if keyword:
    filtered_df = filtered_df[
        filtered_df["Nama Uji"].str.contains(keyword, case=False)
        |
        filtered_df["Reagen"].str.contains(keyword, case=False)
    ]

st.write("")

# =========================================================
# CARD DISPLAY
# =========================================================
for index, row in filtered_df.iterrows():

    st.markdown(f"""
    <div class="card">

    <h3>🧪 {row['Nama Uji']}</h3>

    <div class="small-text">

    <b>🎯 Gugus Fungsi:</b><br>
    {row['Gugus Fungsi']}<br><br>

    <b>🔬 Reagen:</b><br>
    {row['Reagen']}<br><br>

    <b>📝 Prosedur:</b><br>
    {row['Prosedur']}<br><br>

    <b>💡 Hasil Positif:</b><br>
    {row['Hasil']}<br><br>

    <b>👁️ Pengamatan Visual:</b><br>
    {row['Visual']}

    </div>

    <div class="reaction-box">
    ⚗️ {row['Reaksi']}
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class='footer'>
© 2026 ChemQual Premium — Organic Chemistry Lab Assistant
</div>
""", unsafe_allow_html=True)
