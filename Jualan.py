import streamlit as st

st.set_page_config(page_title="Pabrik Video FYP - AutoClip Engine", page_icon="🚨", layout="centered")

# --- KONFIGURASI LINK & GAMBAR ---
LINK_WA = "https://wa.me/6281234567890?text=Halo%20Admin,%20saya%20mau%20beli%20AutoClip%20Cuan%20Engine%20harga%20promo%2099rb!"
IMG_HERO = "box.jpg" # Pastikan file box.jpg sudah ada di GitHub

# --- CSS PREMIUM ---
st.markdown("""
<style>
    .stApp { background-color: #FAFAFA; font-family: 'Inter', sans-serif; }
    .hero-title { text-align: center; color: #B71C1C; font-size: 38px; font-weight: 900; line-height: 1.2; margin-bottom: 15px; text-transform: uppercase; }
    .hero-subtitle { text-align: center; color: #444; font-size: 20px; font-weight: 600; margin-bottom: 25px; }
    .highlight { background-color: #FFF176; padding: 0 5px; }
    
    /* Tabel Penderitaan */
    .vs-box { background: white; padding: 25px; border-radius: 15px; border: 2px solid #E0E0E0; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 30px; }
    .vs-title { text-align: center; font-size: 24px; font-weight: 800; margin-bottom: 20px; color: #111; }
    
    /* Box Bonus */
    .bonus-box { background: #E8F5E9; padding: 20px; border-radius: 12px; border: 2px dashed #4CAF50; margin-bottom: 20px; }
    
    /* Harga & Tombol */
    .price-box { background: linear-gradient(135deg, #111 0%, #333 100%); color: white; padding: 40px 20px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 30px 0; border: 3px solid #FFD700; }
    .price-coret { text-decoration: line-through; color: #aaa; font-size: 22px; }
    .price-final { color: #FFD700; font-size: 55px; font-weight: 900; margin: 10px 0; }
    .btn-wa { display: block; background: linear-gradient(to right, #25D366, #128C7E); color: white !important; text-align: center; padding: 20px; font-size: 24px; font-weight: 900; border-radius: 50px; text-decoration: none; animation: pulse 2s infinite; border: 2px solid white; margin-top: 15px; }
    .btn-wa:hover { transform: scale(1.05); background: linear-gradient(to right, #128C7E, #075E54); }
    
    @keyframes pulse { 0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); } 70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); } 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); } }
</style>
""", unsafe_allow_html=True)

# --- HEADER (SUDAH DI-UPDATE MULTI-PLATFORM) ---
st.markdown('<div class="hero-title">🚨 UBAH 1 PODCAST JADI PULUHAN KONTEN VIRAL UNTUK TIKTOK, FB PRO, REELS & SHORTS! 🚨</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Berhenti mengedit manual! Biarkan <span class="highlight">Robot AI Bekerja 24 Jam</span> memotong video, menulis judul clickbait, dan meracik hashtag untuk Anda.</div>', unsafe_allow_html=True)

# Gambar Produk
try:
    st.image(IMG_HERO, use_container_width=True)
except:
    st.info("Gambar 3D Box akan muncul setelah di-upload ke GitHub.")

st.markdown("---")

# --- KALKULATOR PENDERITAAN ---
st.markdown("""
<div class="vs-box">
    <div class="vs-title">🥊 CARA LAMA vs AUTO-CUAN ENGINE</div>
    <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <tr style="background: #f8f9fa; border-bottom: 2px solid #ddd;">
            <th style="padding: 10px; width: 50%; color: #D32F2F;">❌ Cara Manual (Kuno)</th>
            <th style="padding: 10px; width: 50%; color: #2E7D32;">✅ Menggunakan Software Ini</th>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px;">Download video berjam-jam</td>
            <td style="padding: 10px; font-weight: bold;">Cukup Paste Link YouTube</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px;">Nonton ulang cari "Hook" menarik</td>
            <td style="padding: 10px; font-weight: bold;">AI mencari Hook paling viral otomatis</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px;">Potong & Zoom wajah manual di CapCut</td>
            <td style="padding: 10px; font-weight: bold;">Kamera AI otomatis fokus ke wajah pembicara</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Pusing mikir Caption & Hashtag</td>
            <td style="padding: 10px; font-weight: bold;">Dibuatkan file Caption & Hashtag siap Copy-Paste!</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# --- KUALIFIKASI TARGET PASAR (SUDAH DI-UPDATE) ---
st.markdown("### 🎯 Software Ini Tercipta Khusus Untuk:")
st.markdown("""
* **Pemain FB Pro (Monetisasi):** Kejar jam tayang dan *followers* tanpa perlu repot ngedit tiap malam. Algoritma kami kebal dari deteksi *Unoriginal Content*!
* **Affiliate TikTok & Shopee Video:** Butuh suplai konten harian tak terbatas tanpa perlu tampil wajah? Mesin ini jawabannya.
* **YouTuber Shorts & Selebgram:** Tinggal masukkan *link* podcast/kajian panjang, biarkan mesin memanen puluhan klipnya.
* **Content Creator:** Yang mulai kelelahan dan tidak punya dana untuk menggaji Video Editor bulanan.
""")

st.markdown("---")

# --- FITUR ANTI BANNED (PENJELASAN BARU) ---
st.markdown("### 🛡️ Mengapa Aman dari Banned Multi-Platform?")
st.write("Dilengkapi **Tameng Anti-Shadowban**, mesin kami menyisipkan manipulasi durasi dan kecepatan 5% secara halus pada level piksel. Akibatnya, robot algoritma milik Meta (Facebook/IG), YouTube, dan TikTok akan mengira video Anda adalah **100% karya baru**, bukan hasil *re-upload*! Anda bebas barbar *upload* massal!")

st.markdown("---")

# --- VALUE STACK (BONUS) ---
st.markdown("<h3 style='text-align: center;'>🎁 AMBIL LISENSINYA HARI INI & DAPATKAN BONUS GILA INI:</h3>", unsafe_allow_html=True)
st.markdown("""
<div class="bonus-box">
    <h4>☑️ BONUS 1: Cheat Sheet "Algoritma FYP Multi-Platform" (Senilai Rp 150.000)</h4>
    <p>Rahasia jam tayang dan cara optimasi khusus untuk TikTok, FB Pro, dan YouTube Shorts.</p>
</div>
<div class="bonus-box">
    <h4>☑️ BONUS 2: 100+ Template Hook Copywriting (Senilai Rp 99.000)</h4>
    <p>Kumpulan kalimat pembuka video yang dijamin membuat penonton berhenti *scroll*.</p>
</div>
""", unsafe_allow_html=True)

# --- HARGA & CALL TO ACTION ---
st.markdown(f"""
<div class="price-box">
    <h3 style="color: white; margin-bottom: 5px;">HAK MILIK PENUH - TANPA BIAYA BULANAN</h3>
    <p style="color: #ddd;">Total Nilai Software + Bonus: <s>Rp 748.000</s></p>
    <div class="price-coret">Harga Normal: Rp 499.000</div>
    <div class="price-final">HANYA Rp 99.000,-</div>
    <p style="color: #FFF176; font-weight: bold;">(Diskon 80% Berlaku Khusus Hari Ini!)</p>
    <a href="{LINK_WA}" target="_blank" class="btn-wa">🛒 YA, SAYA MAU MESIN CUAN INI!</a>
    <p style="margin-top: 15px; font-size: 14px; color: #aaa;">Proses pengiriman file otomatis via WhatsApp setelah pembayaran.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("<p style='text-align: center;'>© 2026 Kavling Digital. All rights reserved.</p>", unsafe_allow_html=True)
