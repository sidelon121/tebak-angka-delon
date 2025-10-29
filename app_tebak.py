import streamlit as st
import random

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
    # Background dengan CSS
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stSelectbox>div>div>input {
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color: white;'>🎯 TEBAK ANGKA DELON 🎯</h1>", unsafe_allow_html=True)
    garis()
    st.markdown("""
    <div style='text-align:center; color: white;'>
    <b>Pilih Level Kesulitan:</b><br>
    <span>Easy: 1-10 (3 tebakan)</span><br>
    <span>Medium: 1-20 (4 tebakan)</span><br>
    <span>Hard: 1-50 (5 tebakan)</span><br>
    <span>Expert: 1-100 (6 tebakan)</span><br>
    <span>Crazy: 1-1000 (10 tebakan)</span><br>
    <span>Bahlil: 1-100000 (20 tebakan)</span><br>
    <span>Luhut: 1-500000 (25 tebakan)</span><br>
    <span>Gibran: 1-1000000 (30 tebakan)</span><br>
    <span>Wowo: 1-1500000 (35 tebakan)</span><br>
    <span>Mulyono: 1-2000000 (40 tebakan)</span><br>
    
    </div>
    """, unsafe_allow_html=True)
    garis()

    pilihan = st.selectbox(
        "Pilih opsi:",
        ("Pilih Level", "Easy", "Medium", "Hard", "Expert", "Crazy", "Bahlil", "Luhut", "Gibran", "Wowo", "Mulyono", "Keluar"),
        format_func=lambda x: {
            "Pilih Level": "Pilih Level Kesulitan",
            "Easy": "🎮 Easy (1-10)",
            "Medium": "🎯 Medium (1-20)",
            "Hard": "🔥 Hard (1-50)",
            "Expert": "💀 Expert (1-100)",
            "Crazy": "☠️ Crazy (1-1000)",
            "Bahlil": "🥰 Bahlil (1-100000)",
            "Luhut": "😍 Luhut (1-500000)",
            "Gibran": "😎 Gibran (1000000)",
            "Wowo": "☺️ Wowo (1500000)",
            "Mulyono": "😋 Mulyono (2000000)",
            "Keluar": "🚪 Keluar"
        }[x]
    )

    if pilihan in ["Easy", "Medium", "Hard", "Expert", "Crazy", "Bahlil", "Luhut", "Gibran", "Wowo", "Mulyono"]:
        app_game(pilihan)
    elif pilihan == "Keluar":
        keluar()


app_menu()









