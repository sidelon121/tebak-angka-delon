import streamlit as st
import streamlit.components.v1 as components
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

# Fallback notifikasi agar kompatibel lintas versi Streamlit
def notify(message: str):
    try:
        toast_fn = getattr(st, "toast", None)
        if callable(toast_fn):
            toast_fn(message)
        else:
            st.success(message)
    except Exception:
        st.success(message)

# Level kesulitan
levels = {
    "Easy": {"range": (1, 10), "max_tebakan": 3},
    "Medium": {"range": (1, 20), "max_tebakan": 4},
    "Hard": {"range": (1, 50), "max_tebakan": 5},
    "Expert": {"range": (1, 100), "max_tebakan": 6},
    "Crazy": {"range": (1, 1000), "max_tebakan": 10},
    "Bahlil": {"range": (1, 100000), "max_tebakan": 20},
    "Luhut": {"range": (1, 500000), "max_tebakan": 25},
    "Gibran": {"range": (1, 1000000), "max_tebakan": 30},
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

    # Anchor untuk auto-scroll masuk ke area game
    st.markdown("<div id='game-start'></div>", unsafe_allow_html=True)
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

    # Tampilkan tombol kembali ke Menu Level
    cols_back = st.columns([1, 1, 1])
    with cols_back[0]:
        if st.button("← Menu", key="back_to_menu"):
            # Reset hanya pilihan level, tidak menghapus hasil angka acak agar game baru saat kembali pilih level
            st.session_state.selected_level = "Pilih Level"
            st.session_state["level_select"] = "Pilih Level"
            st.rerun()

# Fungsi menu utama
def app_menu():
    # Global CSS bertema minimalis-elegan
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

        .stApp {
            background: radial-gradient(1200px 600px at 100% 0%, rgba(31,119,255,0.25) 0%, rgba(31,119,255,0) 60%),
                        radial-gradient(900px 500px at 0% 100%, rgba(0,193,144,0.25) 0%, rgba(0,193,144,0) 60%),
                        linear-gradient(180deg, #0B0C10 0%, #0A0B0E 100%);
            color: #F2F3F7;
            font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, 'Helvetica Neue', Arial, 'Noto Sans', 'Apple Color Emoji', 'Segoe UI Emoji';
            animation: bgFloat 18s ease-in-out infinite alternate;
        }

        @keyframes bgFloat {
            0% { background-position: 0 0, 0 0, 0 0; }
            100% { background-position: 20px -30px, -30px 20px, 0 0; }
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
            animation: fadeUp 0.6s ease both;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Judul dengan gradien tipografi */
        .title {
            text-align: center;
            font-weight: 800;
            font-size: 38px;
            letter-spacing: 0.5px;
            background: linear-gradient(90deg, #FFFFFF 0%, #D9DCEA 50%, #FFFFFF 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin: 0.25rem 0 0.5rem 0;
            animation: shimmer 2.6s linear infinite;
        }

        @keyframes shimmer {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }

        hr {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.15);
            margin: 12px 0 18px 0;
        }

        /* Badge level */
        .badges { text-align: center; margin: 8px 0 10px 0; }
        .badge {
            display: inline-block;
            padding: 8px 12px;
            margin: 6px 6px;
            font-size: 13px;
            font-weight: 600;
            color: #F2F3F7;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 999px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
            white-space: nowrap;
            transform: translateY(0);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            animation: popIn 0.5s ease both;
        }
        .badge:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(0,0,0,0.25); }

        @keyframes popIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Tombol */
        .stButton>button {
            background: linear-gradient(180deg, #4C84FF 0%, #3D6DF2 100%);
            color: #fff;
            border: 0;
            border-radius: 12px;
            padding: 0.6rem 1.1rem;
            font-weight: 600;
            letter-spacing: 0.3px;
            box-shadow: 0 10px 20px rgba(61,109,242,0.28);
            transition: transform 0.06s ease, box-shadow 0.2s ease, filter 0.2s ease;
            position: relative;
            overflow: hidden;
        }
        .stButton>button:hover { transform: translateY(-1px); filter: brightness(1.03); }
        .stButton>button:active { transform: translateY(0); box-shadow: 0 6px 14px rgba(59,94,234,0.22); }

        /* Ripple halus */
        .stButton>button::after {
            content: "";
            position: absolute;
            left: 50%; top: 50%;
            width: 0; height: 0;
            background: rgba(255,255,255,0.35);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: width 0.4s ease, height 0.4s ease, opacity 0.4s ease;
        }
        .stButton>button:active::after {
            width: 220px; height: 220px; opacity: 0.14;
        }

        /* Selectbox */
        div[data-testid="stSelectbox"] div[role="combobox"] {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
        }
        div[data-testid="stSelectbox"] input {
            color: #F2F3F7 !important;
            font-weight: 600;
        }

        /* Number input */
        div[data-testid="stNumberInput"] input[type="number"] {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            color: #F2F3F7;
            font-weight: 700;
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

    st.markdown("<div class='title'>Menu</div>", unsafe_allow_html=True)
    st.markdown("<div class='title'>Tebak Angka Delon</div>", unsafe_allow_html=True)
    garis()
    # Badges interaktif: klik untuk memilih level (sinkron dengan selectbox)
    if 'selected_level' not in st.session_state:
        st.session_state.selected_level = "Pilih Level"
    if 'just_navigated' not in st.session_state:
        st.session_state.just_navigated = False

    levels_order = list(levels.keys())
    cols_per_row = 5
    rows = (len(levels_order) + cols_per_row - 1) // cols_per_row
    idx = 0
    for _ in range(rows):
        cols = st.columns(cols_per_row)
        for c in range(cols_per_row):
            if idx >= len(levels_order):
                break
            name = levels_order[idx]
            with cols[c]:
                if st.button(name, key=f"badge_{name}"):
                    st.session_state.selected_level = name
                    # Set nilai widget selectbox secara langsung agar sinkron tanpa pilihan manual
                    st.session_state["level_select"] = name
                    notify(f"Level {name} dipilih ✅")
                    st.session_state.just_navigated = True
                    st.rerun()
            idx += 1

    garis()

    choices = ("Pilih Level",) + tuple(levels_order) + ("Keluar",)

    pilihan = st.selectbox(
        "Pilih level:",
        choices,
        key="level_select",
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
        }.get(x, x)
    )

    # Sinkronkan state jika user ubah via selectbox
    if pilihan != st.session_state.selected_level:
        st.session_state.selected_level = pilihan
        if pilihan != "Pilih Level" and pilihan != "Keluar":
            st.session_state.just_navigated = True
            st.rerun()

    if pilihan in ["Easy", "Medium", "Hard", "Expert", "Crazy", "Bahlil", "Luhut", "Gibran", "Wowo", "Mulyono"]:
        app_game(pilihan)
        # Scroll otomatis ke anchor game-start saat baru navigasi dari menu
        if st.session_state.just_navigated:
            components.html("""
            <script>
                const el = document.getElementById('game-start');
                if (el) { el.scrollIntoView({behavior: 'smooth', block: 'start'}); }
            </script>
            """, height=0)
            st.session_state.just_navigated = False
    elif pilihan == "Keluar":
        keluar()


app_menu()
