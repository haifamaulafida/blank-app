import streamlit as st

# ==================================
# KONFIGURASI
# ==================================

st.set_page_config(
    page_title="Uji Kualitatif Organik",
    page_icon="🧪",
    layout="centered"
)

# ==================================
# CSS
# ==================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

h1{
    text-align:center;
    color:#1565C0;
}

.stButton button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.kartu{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SESSION STATE
# ==================================

if "page" not in st.session_state:
    st.session_state.page = "start"

# ==================================
# HALAMAN START
# ==================================

if st.session_state.page == "start":

    st.markdown("<h1>🧪 UJI KUALITATIF ORGANIK</h1>",
                unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    st.markdown(
        """
        <div class='kartu'>
        Website identifikasi senyawa organik berdasarkan hasil pengujian laboratorium.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("START"):
        st.session_state.page = "input"
        st.rerun()

# ==================================
# HALAMAN INPUT
# ==================================

elif st.session_state.page == "input":

    st.title("Input Hasil Pengujian")

    brom = st.selectbox(
        "Uji Brom",
        [
            "Tidak diuji",
            "Warna hilang",
            "Tetap berwarna"
        ]
    )

    baeyer = st.selectbox(
        "Uji Baeyer (KMnO4)",
        [
            "Tidak diuji",
            "Positif",
            "Negatif"
        ]
    )

    fecl3 = st.selectbox(
        "Uji FeCl3",
        [
            "Tidak diuji",
            "Ungu",
            "Hijau",
            "Biru",
            "Tidak berubah"
        ]
    )

    tollens = st.selectbox(
        "Uji Tollens",
        [
            "Tidak diuji",
            "Cermin perak",
            "Negatif"
        ]
    )

    fehling = st.selectbox(
        "Uji Fehling",
        [
            "Tidak diuji",
            "Merah bata",
            "Negatif"
        ]
    )

    lucas = st.selectbox(
        "Uji Lucas",
        [
            "Tidak diuji",
            "Keruh cepat",
            "Keruh lambat",
            "Tidak bereaksi"
        ]
    )

    if st.button("IDENTIFIKASI"):

        hasil = []

        # Fenol

        if fecl3 in ["Ungu", "Hijau", "Biru"]:
            hasil.append(
                "✓ Mengandung gugus FENOL"
            )

        # Aldehid

        if tollens == "Cermin perak":
            hasil.append(
                "✓ Mengandung ALDEHID"
            )

        if fehling == "Merah bata":
            hasil.append(
                "✓ Aldehid alifatik"
            )

        # Alkohol

        if lucas == "Keruh cepat":
            hasil.append(
                "✓ Alkohol Tersier"
            )

        elif lucas == "Keruh lambat":
            hasil.append(
                "✓ Alkohol Sekunder"
            )

        elif lucas == "Tidak bereaksi":
            hasil.append(
                "✓ Alkohol Primer"
            )

        # Ikatan rangkap

        if brom == "Warna hilang":
            hasil.append(
                "✓ Kemungkinan memiliki ikatan rangkap"
            )

        if baeyer == "Positif":
            hasil.append(
                "✓ Mengandung alkena/alkuna"
            )

        if len(hasil) == 0:
            hasil.append(
                "Belum dapat diidentifikasi berdasarkan data yang diberikan."
            )

        st.session_state.hasil = hasil
        st.session_state.page = "hasil"

        st.rerun()

# ==================================
# HALAMAN HASIL
# ==================================

elif st.session_state.page == "hasil":

    st.title("Hasil Identifikasi")

    for item in st.session_state.hasil:
        st.success(item)

    st.write("")
    st.write("Interpretasi ini berdasarkan kombinasi hasil uji yang dipilih.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Kembali"):
            st.session_state.page = "input"
            st.rerun()

    with col2:
        if st.button("Home"):
            st.session_state.page = "start"
            st.rerun()
