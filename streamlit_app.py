 import streamlit as st
import pandas as pd

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="ChemQual - Katalog Organik",
    page_icon="🧪",
    layout="wide"
)

# =========================================================
# DATABASE UJI KUALITATIF ORGANIK
# =========================================================
data_uji = [
    {
        "Nama Uji": "Uji Lucas",
        "Gugus Fungsi": "Alkohol (Substitusi)",
        "Reagen": "HCl pekat + ZnCl2 (Reagen Lucas)",
        "Prosedur Singkat": "Campurkan sampel dengan reagen Lucas pada suhu kamar, amati kecepatan terbentuknya kekeruhan/fasa cair terpisah.",
        "Hasil Positif": "Tersier: Instan (<1 menit)\nSekunder: 5-10 menit\nPrimer: Tidak bereaksi pada suhu kamar",
        "Warna/Visual": "⚪ Kekeruhan / Terbentuk 2 Lapisan",
        "Reaksi Kimia": "R-OH + HCl --(ZnCl2)--> R-Cl + H2O"
    },
    {
        "Nama Uji": "Uji Tollens",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "AgNO3 + NaOH + NH4OH (Reagen Tollens)",
        "Prosedur Singkat": "Tambahkan sampel ke dalam reagen Tollens, lalu panaskan di penangas air selama beberapa menit.",
        "Hasil Positif": "Terbentuk lapisan perak mengkilap di dinding tabung reaksi.",
        "Warna/Visual": "🪞 Cermin Perak (Silver Mirror)",
        "Reaksi Kimia": "R-CHO + 2[Ag(NH3)2]+ + 3OH- --> R-COO- + 2Ag (s) + 4NH3 + 2H2O"
    },
    {
        "Nama Uji": "Uji Fehling",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "Fehling A (CuSO4) + Fehling B (K-Na-tartrat + NaOH)",
        "Prosedur Singkat": "Campurkan Fehling A dan B (1:1), tambahkan sampel, lalu panaskan di penangas air.",
        "Hasil Positif": "Warna biru tua reagen akan berubah menjadi endapan merah bata.",
        "Warna/Visual": "🔴 Endapan Merah Bata",
        "Reaksi Kimia": "R-CHO + 2Cu2+ + 5OH- --> R-COO- + Cu2O (s) + 3H2O"
    },
    {
        "Nama Uji": "Uji Ferri Klorida",
        "Gugus Fungsi": "Fenol",
        "Reagen": "Larutan FeCl3 1% atau 5%",
        "Prosedur Singkat": "Larutkan sampel dalam air/etanol, lalu teteskan beberapa tetes larutan FeCl3.",
        "Hasil Positif": "Terbentuk warna ungu, hijau, atau biru kompleks yang pekat.",
        "Warna/Visual": "🟣 Warna Ungu / Biru / Hijau Pekat",
        "Reaksi Kimia": "6Ar-OH + Fe3+ --> [Fe(OAr)6]3- (kompleks berwarna) + 6H+"
    },
    {
        "Nama Uji": "Uji Natrium Bikarbonat",
        "Gugus Fungsi": "Asam Karboksilat",
        "Reagen": "Larutan NaHCO3 5%",
        "Prosedur Singkat": "Tambahkan sampel organik ke dalam larutan NaHCO3 jenuh.",
        "Hasil Positif": "Terbentuk gelembung gas dengan cepat (efervesen).",
        "Warna/Visual": "🫧 Gelembung Gas (CO2)",
        "Reaksi Kimia": "R-COOH + NaHCO3 --> R-COONa + H2O + CO2 (g)"
    },
    {
        "Nama Uji": "Uji Baeyer",
        "Gugus Fungsi": "Alkena / Alkuna (Ikatan Rangkap)",
        "Reagen": "Larutan KMnO4 1% (Basa/Netral)",
        "Prosedur Singkat": "Teteskan larutan KMnO4 ke dalam sampel sambil dikocok.",
        "Hasil Positif": "Warna ungu dari KMnO4 hilang dan terbentuk endapan coklat.",
        "Warna/Visual": "🟤 Warna Ungu Hilang & Endapan Coklat",
        "Reaksi Kimia": "3R-CH=CH-R + 2KMnO4 + 4H2O --> 3R-CH(OH)-CH(OH)-R + 2MnO2 (s) + 2KOH"
    }
]

# =========================================================
# DATAFRAME
# =========================================================
df = pd.DataFrame(data_uji)

# =========================================================
# HEADER APLIKASI
# =========================================================
st.title("🧪 ChemQual v1.0")
st.subheader("Katalog Uji Kualitatif Senyawa Organik")

st.write(
    "Aplikasi saku untuk membantu mahasiswa/siswa "
    "mengidentifikasi gugus fungsi organik di laboratorium."
)

st.divider()

# =========================================================
# NAVIGASI TABS
# =========================================================
tab1, tab2 = st.tabs([
    "🔍 Pencarian & Filter",
    "📚 Semua Daftar Uji"
])

# =========================================================
# TAB 1 — PENCARIAN
# =========================================================
with tab1:

    st.markdown("## 🔍 Cari Berdasarkan Parameter")

    # Variabel default
    search_gugus = "Semua Gugus"
    search_name = ""

    # Kolom input
    col1, col2 = st.columns(2)

    with col1:
        search_gugus = st.selectbox(
            "Pilih Gugus Fungsi:",
            ["Semua Gugus"] + list(df["Gugus Fungsi"].unique())
        )

    with col2:
        search_name = st.text_input(
            "Cari nama uji / reagen:",
            placeholder="Contoh: Tollens, FeCl3"
        )

    # Filter dataframe
    filtered_df = df.copy()

    if search_gugus != "Semua Gugus":
        filtered_df = filtered_df[
            filtered_df["Gugus Fungsi"] == search_gugus
        ]

    if search_name:
        filtered_df = filtered_df[
            filtered_df["Nama Uji"].str.contains(search_name, case=False) |
            filtered_df["Reagen"].str.contains(search_name, case=False)
        ]

    # Tampilkan hasil
    if filtered_df.empty:
        st.warning("❌ Uji tidak ditemukan.")
    else:
        for index, row in filtered_df.iterrows():

            with st.expander(
                f"🧪 {row['Nama Uji']} — {row['Gugus Fungsi']}",
                expanded=True
            ):

                c1, c2 = st.columns([2, 1])

                with c1:
                    st.markdown(f"### 🔬 Reagen")
                    st.write(row["Reagen"])

                    st.markdown("### 📝 Prosedur")
                    st.write(row["Prosedur Singkat"])

                    st.markdown("### ⚗️ Persamaan Reaksi")
                    st.code(row["Reaksi Kimia"], language="text")

                with c2:
                    st.info(
                        f"💡 Hasil Positif:\n\n{row['Hasil Positif']}"
                    )

                    st.success(
                        f"👁️ Pengamatan Visual:\n\n{row['Warna/Visual']}"
                    )

# =========================================================
# TAB 2 — SEMUA DATA
# =========================================================
with tab2:

    st.markdown("## 📚 Daftar Lengkap Uji Kualitatif")

    for index, row in df.iterrows():

        with st.container():

            st.markdown(f"# 🧪 {row['Nama Uji']}")

            col1, col2 = st.columns([2, 1])

            with col1:
                st.write(
                    f"### 🎯 Gugus Fungsi\n{row['Gugus Fungsi']}"
                )

                st.write(
                    f"### 🔬 Reagen\n{row['Reagen']}"
                )

                st.write(
                    f"### 📝 Prosedur\n{row['Prosedur Singkat']}"
                )

                st.write("### ⚗️ Reaksi Kimia")
                st.code(row["Reaksi Kimia"], language="text")

            with col2:
                st.info(
                    f"💡 Hasil Positif:\n\n{row['Hasil Positif']}"
                )

                st.success(
                    f"👁️ Visual:\n\n{row['Warna/Visual']}"
                )

            st.divider()

# =========================================================
# FOOTER
# =========================================================
st.caption("© 2026 ChemQual — Katalog Uji Organik")
