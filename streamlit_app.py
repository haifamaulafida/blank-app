import streamlit as st

st.set_page_config(
    page_title="Uji Kualitatif Kimia Organik",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

DB = {
  "Alkohol":{
    "formula":"R-OH",
    "desc":"Senyawa organik yang mengandung gugus hidroksil (-OH) terikat pada atom karbon.",
    "badge":"b-teal",
    "uji":[
      {"nama":"Uji Lucas","reagen":"ZnCl₂ + HCl pekat","badge":"b-teal",
       "alasan":"Uji Lucas digunakan untuk membedakan alkohol primer, sekunder, dan tersier. Reagen Lucas (ZnCl₂/HCl) bereaksi dengan alkohol melalui mekanisme SN1 atau SN2. Alkohol tersier bereaksi paling cepat karena menghasilkan karbokation tersier yang paling stabil. Alkohol sekunder bereaksi dalam beberapa menit, sedangkan alkohol primer tidak bereaksi tanpa pemanasan.",
       "reaksi":["Tersier:  R₃C-OH  +  HCl  →  R₃C-Cl  +  H₂O     (segera keruh)","Sekunder: R₂CH-OH +  HCl  →  R₂CH-Cl + H₂O     (~5 menit)","Primer:   RCH₂-OH +  HCl  →  tidak bereaksi tanpa pemanasan"],
       "pos":"✦ Larutan keruh / terbentuk 2 lapisan (alkil klorida tidak larut)",
       "neg":"✦ Tetap bening → alkohol primer"},
      {"nama":"Uji Oksidasi K₂Cr₂O₇","reagen":"K₂Cr₂O₇ + H₂SO₄ encer","badge":"b-amber",
       "alasan":"Dikromat dalam suasana asam adalah oksidator kuat yang mengoksidasi alkohol primer menjadi aldehida/asam karboksilat, sekunder menjadi keton. Alkohol tersier tidak dapat dioksidasi karena tidak ada H pada karbon yang mengikat -OH. Perubahan warna Cr(VI) oranye menjadi Cr(III) hijau menjadi indikator visual yang jelas.",
       "reaksi":["Primer:   3 RCH₂OH + Cr₂O₇²⁻ + 8H⁺  →  3 RCHO + 2Cr³⁺ + 7H₂O","Sekunder: 3 R₂CHOH + Cr₂O₇²⁻ + 8H⁺  →  3 R₂CO  + 2Cr³⁺ + 7H₂O","Tersier:  R₃COH   + Cr₂O₇²⁻          →  tidak bereaksi"],
       "pos":"✦ Warna berubah dari oranye → hijau/biru-hijau",
       "neg":"✦ Tetap oranye → alkohol tersier"}
    ]
  },
  "Aldehida":{
    "formula":"R-CHO",
    "desc":"Senyawa karbonil dengan gugus -CHO di ujung rantai karbon; bersifat pereduksi kuat.",
    "badge":"b-amber",
    "uji":[
      {"nama":"Uji Tollens (Cermin Perak)","reagen":"AgNO₃ + NH₃","badge":"b-teal",
       "alasan":"Aldehida memiliki atom H pada gugus karbonil yang membuatnya mudah teroksidasi. Reagen Tollens mengandung ion kompleks [Ag(NH₃)₂]⁺ sebagai oksidator lemah yang cukup untuk mengoksidasi aldehida menjadi asam karboksilat, sementara Ag⁺ tereduksi menjadi Ag logam. Keton tidak bereaksi karena tidak memiliki H karbonil.",
       "reaksi":["RCHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻  →  RCOO⁻ + 2Ag(s)↓ + 4NH₃ + H₂O","Ag⁺ + e⁻  →  Ag⁰   (cermin perak pada dinding tabung)"],
       "pos":"✦ Terbentuk cermin perak berkilat pada dinding tabung",
       "neg":"✦ Tidak ada endapan → bukan aldehida"},
      {"nama":"Uji Fehling","reagen":"Fehling A (CuSO₄) + Fehling B (NaOH/tartrat)","badge":"b-amber",
       "alasan":"Reagen Fehling mengandung Cu²⁺ dalam kompleks tartrat yang menjaga Cu²⁺ tetap larut. Aldehida alifatik mereduksi Cu²⁺ (biru) menjadi Cu₂O (merah bata). Uji ini spesifik: aldehida aromatik dan keton umumnya tidak bereaksi, berguna membedakan aldehida alifatik dari senyawa karbonil lainnya.",
       "reaksi":["RCHO + 2Cu²⁺ + 5OH⁻  →  RCOO⁻ + Cu₂O↓(merah) + 3H₂O","Cu²⁺ (biru)  →  Cu⁺ dalam Cu₂O (merah bata)"],
       "pos":"✦ Endapan merah bata (Cu₂O) terbentuk saat dipanaskan",
       "neg":"✦ Tetap biru → bukan aldehida alifatik"}
    ]
  },
  "Keton":{
    "formula":"R-CO-R'",
    "desc":"Senyawa karbonil dengan dua gugus alkil/aril yang terikat pada atom karbon karbonil.",
    "badge":"b-amber",
    "uji":[
      {"nama":"Uji Iodoform","reagen":"I₂ + NaOH","badge":"b-amber",
       "alasan":"Keton yang memiliki gugus metil (CH₃CO-) menjalani reaksi halogenasi di posisi alfa. Dalam suasana basa, ketiga H pada CH₃ tersubtitusi oleh I, membentuk CI₃ yang terhidrolisis menghasilkan iodoform (CHI₃) berwarna kuning. Uji ini spesifik untuk metil keton (R-CO-CH₃) dan etanol/asetaldehida.",
       "reaksi":["CH₃COR + 3I₂ + 3OH⁻  →  CI₃COR + 3I⁻ + 3H₂O","CI₃COR  + OH⁻       →  CHI₃↓  + RCOO⁻","CHI₃ = iodoform, endapan kuning pucat berbau khas"],
       "pos":"✦ Endapan kuning CHI₃ dengan bau khas seperti antiseptik",
       "neg":"✦ Tidak ada endapan → bukan metil keton"},
      {"nama":"Uji 2,4-DNP (Brady's Test)","reagen":"2,4-Dinitrofenilhidrazin + H₂SO₄","badge":"b-rose",
       "alasan":"Gugus karbonil C=O pada keton (dan aldehida) bereaksi dengan 2,4-DNP melalui reaksi kondensasi adisi-eliminasi. Nitrogen nukleofilik menyerang karbon karbonil yang elektronegatif, lalu eliminasi air menghasilkan hidrazon berwarna kuning-oranye-merah sesuai konjugasi senyawa.",
       "reaksi":["R₂C=O + H₂N-NH-C₆H₃(NO₂)₂  →  R₂C=N-NH-C₆H₃(NO₂)₂ + H₂O","Produk: 2,4-dinitrofenilhidrazon (kuning / oranye / merah)"],
       "pos":"✦ Endapan kuning, oranye, atau merah terbentuk",
       "neg":"✦ Tidak ada endapan → tidak ada gugus karbonil"}
    ]
  },
  "Asam Karboksilat":{
    "formula":"R-COOH",
    "desc":"Senyawa organik dengan gugus karboksil (-COOH) yang bersifat asam lemah.",
    "badge":"b-rose",
    "uji":[
      {"nama":"Uji Lakmus / pH","reagen":"Kertas lakmus merah/biru atau pH meter","badge":"b-rose",
       "alasan":"Asam karboksilat mengionisasi dalam air melepaskan H⁺ sehingga larutan bersifat asam (pH < 7). Gugus -COOH memiliki pKa sekitar 4-5, menjadikannya asam lemah yang terionisasi sebagian. Uji lakmus merupakan cara paling sederhana untuk konfirmasi sifat asam.",
       "reaksi":["R-COOH  ⇌  R-COO⁻ + H⁺    (Ka ~ 10⁻⁴ – 10⁻⁵)","H⁺ menyebabkan lakmus biru → merah","pH larutan encer ~ 3 – 5"],
       "pos":"✦ Lakmus biru berubah merah; pH < 7",
       "neg":"✦ Tidak berubah → bukan senyawa asam"},
      {"nama":"Uji Na₂CO₃ (Gelembung CO₂)","reagen":"Na₂CO₃ atau NaHCO₃","badge":"b-rose",
       "alasan":"Asam karboksilat cukup kuat untuk mereaksikan karbonat/bikarbonat menghasilkan CO₂. Reaksi ini sangat spesifik: fenol dan alkohol (asam sangat lemah) tidak bereaksi dengan NaHCO₃. Gas CO₂ yang terbentuk dapat dideteksi dengan air kapur (Ca(OH)₂) yang menjadi keruh.",
       "reaksi":["2 R-COOH + Na₂CO₃  →  2 R-COONa + H₂O + CO₂↑","R-COOH  + NaHCO₃  →  R-COONa  + H₂O + CO₂↑","CO₂ + Ca(OH)₂    →  CaCO₃↓ + H₂O   (air kapur keruh)"],
       "pos":"✦ Gelembung CO₂; air kapur menjadi keruh",
       "neg":"✦ Tidak ada gelembung → bukan asam karboksilat"}
    ]
  },
  "Amina":{
    "formula":"R-NH₂",
    "desc":"Turunan amonia dengan gugus organik mengganti H amonia; bersifat basa.",
    "badge":"b-blue",
    "uji":[
      {"nama":"Uji Hinsberg","reagen":"C₆H₅SO₂Cl + NaOH","badge":"b-blue",
       "alasan":"Uji Hinsberg membedakan amina primer, sekunder, dan tersier berdasarkan reaktivitas terhadap benzensulfonil klorida. Amina primer membentuk sulfonamida yang larut dalam NaOH (masih ada H asam). Amina sekunder membentuk sulfonamida yang tidak larut. Amina tersier tidak bereaksi karena tidak ada H pada N.",
       "reaksi":["Primer:   R-NH₂ + C₆H₅SO₂Cl → R-NH-SO₂C₆H₅ + HCl   (larut NaOH)","Sekunder: R₂NH  + C₆H₅SO₂Cl → R₂N-SO₂C₆H₅  + HCl   (tidak larut NaOH)","Tersier:  R₃N   + C₆H₅SO₂Cl → tidak bereaksi"],
       "pos":"✦ Amina primer: endapan larut saat ditambah NaOH berlebih",
       "neg":"✦ Tidak bereaksi → amina tersier"},
      {"nama":"Uji Lakmus (Sifat Basa)","reagen":"Kertas lakmus merah + uap amina","badge":"b-blue",
       "alasan":"Amina memiliki pasangan elektron bebas pada N yang dapat menerima proton (basa Bronsted). Larutan amina memiliki pH > 7 dan mengubah lakmus merah menjadi biru. Amina alifatik lebih basa dari amina aromatik karena resonansi pada cincin benzena mengurangi kerapatan elektron pada N.",
       "reaksi":["R-NH₂ + H₂O  ⇌  R-NH₃⁺ + OH⁻","OH⁻ menyebabkan lakmus merah → biru","pH larutan ~ 8 – 11"],
       "pos":"✦ Lakmus merah menjadi biru; bau menyengat seperti amonia",
       "neg":"✦ Tidak berubah → bukan amina"}
    ]
  },
  "Ester":{
    "formula":"R-COO-R'",
    "desc":"Produk kondensasi asam karboksilat dan alkohol; memiliki aroma khas buah-buahan.",
    "badge":"b-teal",
    "uji":[
      {"nama":"Uji Hidroksamat Fe(III)","reagen":"NH₂OH·HCl + NaOH, lalu FeCl₃","badge":"b-teal",
       "alasan":"Ester bereaksi dengan hidroksilamin (NH₂OH) dalam suasana basa menghasilkan asam hidroksamat, yang kemudian membentuk kompleks berwarna ungu/magenta stabil dengan Fe³⁺. Uji ini sangat spesifik untuk ikatan ester (termasuk lakton). Asam karboksilat dan keton tidak memberi warna yang sama.",
       "reaksi":["R-COO-R' + NH₂OH → R-CO-NHOH + R'OH      (suasana basa)","3 R-CO-NHOH + FeCl₃ → [Fe(RCONHO)₃] + 3HCl","Kompleks Fe³⁺-hidroksamat: warna ungu / magenta intens"],
       "pos":"✦ Larutan berubah ungu atau merah-ungu (magenta)",
       "neg":"✦ Tidak berubah → bukan ester"},
      {"nama":"Uji Saponifikasi","reagen":"NaOH berlebih + pemanasan","badge":"b-amber",
       "alasan":"Ester terhidrolisis dalam suasana basa menghasilkan garam karboksilat (sabun) dan alkohol. Tanda keberhasilan: aroma khas ester menghilang, larutan menjadi homogen. Jika diasamkan kembali akan terbentuk asam karboksilat.",
       "reaksi":["R-COO-R' + NaOH → R-COONa + R'OH    (dipanaskan)","R-COONa  + HCl  → R-COOH↓ + NaCl    (jika diasamkan)"],
       "pos":"✦ Aroma ester menghilang setelah pemanasan; larutan jernih",
       "neg":"✦ Aroma tetap ada → bukan ester"}
    ]
  }
}

if "halaman" not in st.session_state:
    st.session_state.halaman = "intro"
if "pilihan_senyawa" not in st.session_state:
    st.session_state.pilihan_senyawa = "Alkohol"
if "pilihan_uji" not in st.session_state:
    st.session_state.pilihan_uji = []

def halaman_intro():
    st.markdown("""
    <div style="min-height:80vh;display:flex;flex-direction:column;align-items:center;
                justify-content:center;text-align:center;padding:3rem 2rem;">
      <p style="font-family:monospace;font-size:.75rem;color:#475569;letter-spacing:.12em;margin-bottom:1.5rem;">
        C₆H₁₂O₆ · · · CH₃COOH · · · C₂H₅OH · · · C₆H₅NH₂
      </p>
      <p style="font-size:.75rem;font-weight:600;letter-spacing:.28em;text-transform:uppercase;
                color:#00d4aa;margin-bottom:1rem;">🧪 Kimia Organik — Analisis Kualitatif</p>
      <h1 style="font-family:'Georgia',serif;font-size:3.5rem;font-weight:900;
                 line-height:1.1;color:#f0f4ff;margin-bottom:.8rem;">
        Identifikasi<br>
        <span style="background:linear-gradient(135deg,#00d4aa,#3b82f6);
                     -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
          Gugus Fungsi
        </span>
      </h1>
      <p style="font-size:1rem;color:#94a3b8;max-width:460px;line-height:1.7;margin-bottom:2.5rem;">
        Platform interaktif untuk mempelajari uji kualitatif kimia organik —
        reaksi, reagen, dan interpretasi hasil uji gugus fungsi.
      </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🚀  Mulai Uji Kualitatif", use_container_width=True, type="primary"):
            st.session_state.halaman = "utama"
            st.rerun()

def halaman_utama():
    st.markdown("""
    <h1 style="font-family:'Georgia',serif;font-size:1.8rem;color:#f0f4ff;margin-bottom:.3rem;">
      🔬 Uji Kualitatif Kimia Organik
    </h1>
    <p style="color:#94a3b8;font-size:.85rem;margin-bottom:1.5rem;">
      Pilih golongan senyawa dan jenis uji yang ingin dipelajari
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown('<p style="font-size:.7rem;font-weight:600;letter-spacing:.25em;text-transform:uppercase;color:#00d4aa;">① Pilih Golongan Senyawa</p>', unsafe_allow_html=True)
        pilihan = st.radio(
            "Senyawa", list(DB.keys()),
            format_func=lambda x: f"{x}  —  {DB[x]['formula']}",
            label_visibility="collapsed",
            index=list(DB.keys()).index(st.session_state.pilihan_senyawa)
        )
        st.session_state.pilihan_senyawa = pilihan
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1e293b;border-radius:10px;
                    padding:1rem 1.2rem;margin-top:.75rem;font-size:.84rem;
                    color:#94a3b8;line-height:1.65;">
          <strong style="color:#f0f4ff;">{pilihan}</strong> &nbsp;
          <code style="color:#f59e0b;">{DB[pilihan]['formula']}</code><br><br>
          {DB[pilihan]['desc']}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p style="font-size:.7rem;font-weight:600;letter-spacing:.25em;text-transform:uppercase;color:#00d4aa;">② Pilih Uji yang Dilakukan</p>', unsafe_allow_html=True)
        uji_tersedia = [u["nama"] for u in DB[pilihan]["uji"]]
        pilih_uji = st.multiselect(
            "Pilih Uji", uji_tersedia, default=uji_tersedia,
            label_visibility="collapsed",
            placeholder="Pilih minimal satu uji..."
        )
        st.session_state.pilihan_uji = pilih_uji

        for u in DB[pilihan]["uji"]:
            if u["nama"] in pilih_uji:
                st.markdown(f"""
                <div style="background:#111827;border:1px solid #1e293b;border-radius:10px;
                            padding:.75rem 1rem;margin-bottom:.5rem;">
                  <strong style="font-size:.88rem;color:#f0f4ff;">🧫 {u['nama']}</strong><br>
                  <code style="font-size:.72rem;color:#f59e0b;">{u['reagen']}</code>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        if st.button("← Beranda", use_container_width=True):
            st.session_state.halaman = "intro"
            st.rerun()
    with c3:
        if st.button("Lihat Hasil Uji →", use_container_width=True, type="primary",
                     disabled=(len(pilih_uji) == 0)):
            st.session_state.halaman = "output"
            st.rerun()

def halaman_output():
    senyawa = st.session_state.pilihan_senyawa
    uji_dipilih = st.session_state.pilihan_uji
    d = DB[senyawa]

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#111827,#1a2235);border:1px solid #1e293b;
                border-radius:14px;padding:1.75rem;margin-bottom:1.75rem;">
      <p style="font-family:monospace;font-size:.68rem;color:#00d4aa;
                letter-spacing:.05em;margin-bottom:.5rem;">
        {d['formula']} &nbsp;|&nbsp; {len(uji_dipilih)} Uji Dilakukan
      </p>
      <h2 style="font-family:'Georgia',serif;font-size:1.6rem;color:#f0f4ff;margin-bottom:.4rem;">
        Hasil Uji: {senyawa}
      </h2>
      <p style="font-size:.84rem;color:#94a3b8;line-height:1.65;margin:0;">{d['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    for i, nama_uji in enumerate(uji_dipilih, 1):
        uji = next((u for u in d["uji"] if u["nama"] == nama_uji), None)
        if not uji:
            continue
        reaksi_html = "\n".join(uji["reaksi"])
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1e293b;border-radius:14px;
                    padding:1.75rem;margin-bottom:1.25rem;">
          <p style="font-family:monospace;font-size:.68rem;color:#f59e0b;margin-bottom:.5rem;">
            {uji['reagen']}
          </p>
          <h3 style="font-family:'Georgia',serif;font-size:1.15rem;color:#f0f4ff;margin-bottom:1.1rem;">
            {i}. {uji['nama']}
          </h3>

          <p style="font-size:.68rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;
                    color:#475569;margin-bottom:.4rem;">💡 Mengapa Uji Ini Digunakan?</p>
          <p style="font-size:.87rem;color:#94a3b8;line-height:1.75;margin-bottom:1.1rem;">
            {uji['alasan']}
          </p>

          <p style="font-size:.68rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;
                    color:#475569;margin-bottom:.4rem;">⚗️ Reaksi Kimia</p>
          <div style="background:#060b18;border:1px solid #1e293b;border-left:3px solid #00d4aa;
                      border-radius:8px;padding:.9rem 1.1rem;font-family:monospace;font-size:.77rem;
                      color:#00d4aa;line-height:2;margin-bottom:1.1rem;white-space:pre;">
{reaksi_html}
          </div>

          <p style="font-size:.68rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;
                    color:#475569;margin-bottom:.4rem;">📊 Interpretasi Hasil</p>
          <div style="background:rgba(0,212,170,.06);border:1px solid rgba(0,212,170,.2);
                      border-radius:8px;padding:.7rem 1rem;font-size:.85rem;color:#00d4aa;
                      margin-bottom:.5rem;">{uji['pos']}</div>
          <div style="background:rgba(244,63,94,.06);border:1px solid rgba(244,63,94,.2);
                      border-radius:8px;padding:.7rem 1rem;font-size:.85rem;color:#f43f5e;">
            {uji['neg']}
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#111827,#1a2235);border:1px solid #1e293b;
                border-radius:12px;padding:1.5rem;margin-top:1rem;font-size:.86rem;
                color:#94a3b8;line-height:1.75;">
      <p style="font-size:.68rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;
                color:#475569;margin-bottom:.5rem;">📋 Ringkasan Pengujian</p>
      Senyawa <strong style="color:#f0f4ff;">{senyawa}</strong>
      (<code style="color:#f59e0b;">{d['formula']}</code>)
      diuji menggunakan <strong style="color:#f0f4ff;">{len(uji_dipilih)} metode</strong>:
      {', '.join(uji_dipilih)}.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("← Ubah Pilihan", use_container_width=True):
            st.session_state.halaman = "utama"
            st.rerun()
    with c2:
        if st.button("🏠 Beranda", use_container_width=True):
            st.session_state.halaman = "intro"
            st.rerun()

if st.session_state.halaman == "intro":
    halaman_intro()
elif st.session_state.halaman == "utama":
    halaman_utama()
elif st.session_state.halaman == "output":
    halaman_output()
