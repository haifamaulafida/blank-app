
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
# CUSTOM CSS (AESTHETIC UI)
# =========================================================
st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom right, #0f172a, #111827);
    color: white;
}

h1, h2, h3, h4 {
    color: #ffffff;
}

.stApp {
    background: linear-gradient(to bottom right, #0f172a, #111827);
}

.css-1d391kg {
    background-color: #111827;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.01);
    border: 1px solid #38bdf8;
}

.reaction-box {
    background: #020617;
    padding: 12px;
    border-radius: 12px;
    font-family: monospace;
    color: #7dd3fc;
    border-left: 4px solid #38bdf8;
}

.title-main {
    font-size: 55px;
    font-weight: bold;
    color: #7dd3fc;
}

.subtitle {
    font-size: 20px;
    color: #cbd5e1;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATABASE
# =========================================================
data_uji = [
    {
        "Nama Uji": "Uji Lucas",
        "Gugus Fungsi": "Alkohol",
        "Reagen": "HCl pekat + ZnCl2",
        "Prosedur": "Campurkan sampel dengan reagen Lucas pada suhu kamar.",
        "Hasil": "Terbentuk kekeruhan.",
        "Visual": "⚪ Keruh / 2 lapisan",
        "Reaksi": "R-OH + HCl → R-Cl + H2O"
    },

    {
        "Nama Uji": "Uji Tollens",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "AgNO3 + NH4OH",
        "Prosedur": "Panaskan sampel dengan reagen Tollens.",
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

st.write("")

# =========================================================
# SEARCH SECTION
# =========================================================
st.markdown("## 🔍 Pencarian")

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
# DISPLAY CARDS
# =========================================================
for index, row in filtered_df.iterrows():

    st.markdown(f"""
    <div class="card">

    <h2>🧪 {row['Nama Uji']}</h2>

    <p><b>🎯 Gugus Fungsi:</b><br>
    {row['Gugus Fungsi']}</p>

    <p><b>🔬 Reagen:</b><br>
    {row['Reagen']}</p>

    <p><b>📝 Prosedur:</b><br>
    {row['Prosedur']}</p>

    <p><b>💡 Hasil Positif:</b><br>
    {row['Hasil']}</p>

    <p><b>👁️ Pengamatan Visual:</b><br>
    {row['Visual']}</p>

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
```
