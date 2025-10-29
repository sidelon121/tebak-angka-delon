import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Tebak Angka Delon", page_icon="🎯", layout="centered")

# Fungsi untuk garis pemisah
def garis():
    st.markdown("<hr style='border:1px solid #bbb;'>", unsafe_allow_html=True)

# Fungsi keluar
def keluar():
    garis()
    st.success("Terima kasih sudah bermain Tebak Angka!\nSampai jumpa lagi! 🎉")
    st.stop()

# Level kesulitan
levels = {
    "Easy": {"range": (1, 10), "max_tebakan": 3},
    "Medium": {"range": (1, 20), "max_tebakan": 4},
    "Hard": {"range": (1, 50), "max_tebakan": 5},
    "Expert": {"range": (1, 100), "max_tebakan": 6},
    "Crazy": {"range": (1, 1000), "max_tebakan": 10},
    "Bahlil": {"range": (1, 100000), "max_tebakan": 20},
    "Luhut": {"range": (1, 500000), "max_tebakan": 25},
    "Gbran": {"range": (1, 1000000), "max_tebakan": 30},
    "Wowo": {"range": (1, 1500000), "max_tebakan": 35},
    "Mulyono": {"range": (1, 2000000), "max_tebakan": 40}
}

# Fungsi game tebak angka
def app_game(level_name):
    level = levels[level_name]
    min_num, max_num = level["range"]
    max_tebakan = level["max_tebakan"]

    # Inisialisasi session state jika belum ada
    if 'angka_acak' not in st.session_state or st.session_state.get('level') != level_name:
        st.session_state.angka_acak = random.randint(min_num, max_num)
        st.session_state.tebakan_count = 0
        st.session_state.level = level_name
        st.session_state.game_over = False
        st.session_state.won = False

    garis()
    st.markdown(f"<h4 style='text-align:center;'>LEVEL {level_name.upper()} - Tebak Angka {min_num}-{max_num}</h4>", unsafe_allow_html=True)
    garis()

    if not st.session_state.game_over:
        st.write(f"Tebakan tersisa: {max_tebakan - st.session_state.tebakan_count}")
        angka_user = st.number_input(f"Masukkan angka tebakan ({min_num}-{max_num}):", min_value=min_num, max_value=max_num, step=1, key="tebakan")

        if st.button("Tebak!"):
            st.session_state.tebakan_count += 1
            if angka_user > st.session_state.angka_acak:
                st.warning("Angka tebakan terlalu besar! 🔽")
            elif angka_user < st.session_state.angka_acak:
                st.warning("Angka tebakan terlalu kecil! 🔼")
            else:
                st.session_state.game_over = True
                st.session_state.won = True
                st.success(f"Selamat! Angka yang benar adalah {st.session_state.angka_acak} 🎉")
                st.balloons()

            if st.session_state.tebakan_count >= max_tebakan and not st.session_state.won:
                st.session_state.game_over = True
                st.error(f"Anda telah mencapai batas tebakan! Angka yang benar adalah {st.session_state.angka_acak} 😢")

    if st.session_state.game_over:
        if st.button("Main Lagi"):
            # Reset session state
            del st.session_state.angka_acak
            del st.session_state.tebakan_count
            del st.session_state.level
            del st.session_state.game_over
            del st.session_state.won
            st.rerun()

# Fungsi menu utama
def app_menu():
    # Global CSS bertema minimalis-elegan
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        .stApp {
            background: radial-gradient(1200px 600px at 100% 0%, rgba(118,75,162,0.25) 0%, rgba(118,75,162,0) 60%),
                        radial-gradient(900px 500px at 0% 100%, rgba(102,126,234,0.25) 0%, rgba(102,126,234,0) 60%),
                        linear-gradient(180deg, #0E0E10 0%, #0B0B0D 100%);
            color: #EAEAF2;
            font-family: 'Poppins', system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, 'Helvetica Neue', Arial, 'Noto Sans', 'Apple Color Emoji', 'Segoe UI Emoji';
        }

        /* Kontainer utama menjadi kartu elegan */
        .block-container {
            max-width: 760px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .app-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            padding: 28px 28px;
        }

        /* Judul dengan gradien tipografi */
        .title {
            text-align: center;
            font-weight: 700;
            font-size: 38px;
            letter-spacing: 0.5px;
            background: linear-gradient(90deg, #EAEAF2 0%, #B7B8C8 50%, #EAEAF2 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin: 0.25rem 0 0.5rem 0;
        }

        hr {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.15);
            margin: 12px 0 18px 0;
        }

        /* Badge level */
        .badges { text-align: center; margin: 4px 0 8px 0; }
        .badge {
            display: inline-block;
            padding: 6px 10px;
            margin: 6px 6px;
            font-size: 12px;
            font-weight: 600;
            color: #EAEAF2;
            background: rgba(255,255,255,0.065);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 999px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
            white-space: nowrap;
        }

        /* Tombol */
        .stButton>button {
            background: linear-gradient(180deg, #3D73F5 0%, #3B5EEA 100%);
            color: #fff;
            border: 0;
            border-radius: 12px;
            padding: 0.6rem 1.1rem;
            font-weight: 600;
            letter-spacing: 0.3px;
            box-shadow: 0 10px 20px rgba(59,94,234,0.28);
            transition: transform 0.06s ease, box-shadow 0.2s ease, filter 0.2s ease;
        }
        .stButton>button:hover { transform: translateY(-1px); filter: brightness(1.03); }
        .stButton>button:active { transform: translateY(0); box-shadow: 0 6px 14px rgba(59,94,234,0.22); }

        /* Selectbox */
        div[data-testid="stSelectbox"] div[role="combobox"] {
            background: rgba(255,255,255,0.055);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 12px;
        }
        div[data-testid="stSelectbox"] input {
            color: #EAEAF2 !important;
            font-weight: 500;
        }

        /* Number input */
        div[data-testid="stNumberInput"] input[type="number"] {
            background: rgba(255,255,255,0.055);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 12px;
            color: #EAEAF2;
            font-weight: 600;
        }

        /* Alert */
        .stAlert {
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.12);
            background: rgba(255,255,255,0.04);
        }

        /* Text */
        .muted { color: #B7B8C8; font-size: 14px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>Tebak Angka</div>", unsafe_allow_html=True)
    garis()
    # Badges level auto dari konfigurasi
    badges_html = " ".join([
        f"<span class='badge'>{name}: {cfg['range'][0]}-{cfg['range'][1]} ({cfg['max_tebakan']}x)</span>"
        for name, cfg in levels.items()
    ])
    st.markdown(f"<div class='app-card'><div class='badges'>{badges_html}</div></div>", unsafe_allow_html=True)
    garis()

    pilihan = st.selectbox(
        "Pilih level:",
        ("Pilih Level", "Easy", "Medium", "Hard", "Expert", "Crazy", "Bahlil", "Luhut", "Gibran", "Wowo", "Mulyono", "Keluar"),
        format_func=lambda x: {
            "Pilih Level": "Pilih Level Kesulitan",
            "Easy": "Easy (1-10)",
            "Medium": "Medium (1-20)",
            "Hard": "Hard (1-50)",
            "Expert": "Expert (1-100)",
            "Crazy": "Crazy (1-1000)",
            "Bahlil": "Bahlil (1-100000)",
            "Luhut": "Luhut (1-500000)",
            "Gibran": "Gibran (1-1000000)",
            "Wowo": "Wowo (1-1500000)",
            "Mulyono": "Mulyono (1-2000000)",
            "Keluar": "Keluar"
        }[x]
    )

    if pilihan in ["Easy", "Medium", "Hard", "Expert", "Crazy", "Bahlil", "Luhut", "Gibran", "Wowo", "Mulyono"]:
        app_game(pilihan)
    elif pilihan == "Keluar":
        keluar()


app_menu()
