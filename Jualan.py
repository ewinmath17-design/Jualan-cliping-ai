import streamlit as st

# --- 1. SETUP HALAMAN ---
st.set_page_config(page_title="PROMO: AutoClip Cuan Engine", page_icon="🚨", layout="centered")

# --- 2. KONFIGURASI LINK & GAMBAR ---
# Masukkan Link WA Master di sini
LINK_WA = "https://wa.me/6281234567890?text=Halo%20Admin,%20saya%20mau%20beli%20AutoClip%20Cuan%20Engine%20harga%20promo%2099rb!"

# Link Gambar Placeholder (Nanti Master bisa ganti link ini dengan link gambar produk Master sendiri)
IMG_HERO = "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1000&auto=format&fit=crop" # Gambar ilustrasi FYP/TikTok
IMG_MOCKUP = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop" # Gambar ilustrasi Software/Laptop

# --- 3. CSS KUSTOM (DESAIN PREMIUM & ANIMASI) ---
st.markdown("""
<style>
    /* Latar belakang & Font */
    .stApp { background-color: #FAFAFA; font-family: 'Inter', sans-serif; }
    
    /* Headline Premium */
    .hero-title { text-align: center; color: #B71C1C; font-size: 36px; font-weight: 900; line-height: 1.2; margin-bottom: 15px; text-transform: uppercase; }
    .hero-subtitle { text-align: center; color: #555; font-size: 18px; margin-bottom: 30px; font-style: italic; }
    
    /* Box Fitur */
    .feature-box { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #E53935; margin-bottom: 15px; }
    .feature-title { font-weight: 800; font-size: 18px; color: #222; margin-bottom: 5px; }
    
    /* Box Harga */
    .price-box { background: linear-gradient(135deg, #111 0%, #333 100%); color: white; padding: 35px 20px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 40px 0; border: 2px solid #FFD700; }
    .price-coret { text-decoration: line-through; color: #aaa; font-size: 20px; }
    .price-final { color: #FFD700; font-size: 48px; font-weight: 900; margin: 10px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    
    /* Tombol Animasi Denyut (Pulse) */
    .btn-wa { display: block; background: linear-gradient(to right, #25D366, #128C7E); color: white !important; text-align: center; padding: 18px 20px; font-size: 22px; font-weight: 900; border-radius: 50px; text-decoration: none; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4); animation: pulse 2s infinite; margin-top: 15px; border: 2px solid white; }
    .btn-wa:hover { transform: scale(1.05); background: linear-gradient(to right, #128C7E, #075E54); }
    
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }
    
    /* Teks Peringatan */
    .urgency-text { text-align: center; color: #D32F2F; font-weight: bold; font-size: 16px; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. BAGIAN HERO (ATAS) ---
st.markdown('<div class="hero-title">🚨 CETAK RATUSAN VIDEO VIRAL DALAM 10 MENIT, TANPA PUSING EDITING! 🚨</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">"Pabrik Gaib" yang akan membedah video panjang, memotong otomatis, dan menulis Judul Clickbait-nya. Cukup 1x Klik!</div>', unsafe_allow_html=True)

# Menampilkan Gambar Hero Premium
st.image(IMG_HERO, use_container_width=True, caption="Rahasia Mendominasi Algoritma Tanpa Lelah")

st.divider()

# --- 5. BAGIAN MASALAH & SOLUSI (KOLOM) ---
col1, col2 = st.columns(2)

with col1:
    st.error("**❌ CARA LAMA (Melelahkan)**")
    st.write("- Download video berjam-jam.")
    st.write("- Plototin layar cari 'Hook' viral.")
    st.write("- Potong manual di CapCut/Premiere.")
    st.write("- Pusing mikir judul konten.")
    st.write("- Bayar langganan AI bule Rp 300rb/bulan.")

with col2:
    st.success("**✅ CARA BARU (Auto-Cuan)**")
    st.write("- Cukup Paste Link YouTube.")
    st.write("- Robot AI mencari bagian terbaik.")
    st.write("- Dipotong otomatis jadi vertikal.")
    st.write("- Dibuatkan judul Clickbait.")
    st.write("- Bayar 1x, pakai seumur hidup!")

st.divider()

# --- 6. MEKANISME UNIK (FITUR PRODUK) ---
st.markdown("<h3 style='text-align: center; color: #222;'>💎 3 Fitur Gila yang Membuat Kompetitor Menangis:</h3><br>", unsafe_allow_html=True)

st.markdown("""
<div class="feature-box">
    <div class="feature-title">🎥 Teknologi Sutradara Kamera</div>
    Video aslinya ada dua orang (Kiri dan Kanan)? AI kami tidak asal potong di tengah! Atur fokus lensa untuk mengunci wajah Host atau Tamu.
</div>
<div class="feature-box">
    <div class="feature-title">✍️ Magic Auto-Copywriter</div>
    Mesin membaca pikiran audiens dan <b>MENULISKAN JUDUL CLICKBAIT</b> untuk setiap klip secara otomatis!
</div>
<div class="feature-box">
    <div class="feature-title">🛡️ Tameng Anti-Shadowban</div>
    Manipulasi durasi 5% secara halus. Mesin TikTok akan mengira ini adalah video 100% baru buatan Anda. Bebas pelanggaran hak cipta!
</div>
""", unsafe_allow_html=True)

# Gambar Mockup Software
st.image(IMG_MOCKUP, use_container_width=True, caption="Tampilan Software Premium AutoClip Cuan Engine")

# --- 7. BAGIAN HARGA & TOMBOL CTA (CALL TO ACTION) ---
st.markdown(f"""
<div class="price-box">
    <h3 style="color: white; margin-bottom: 5px;">HAK MILIK PENUH - SEUMUR HIDUP</h3>
    <p style="color: #ddd;">Berhenti bayar langganan bulanan mahal!</p>
    <div class="price-coret">Harga Normal: Rp 499.000</div>
    <div class="price-final">Rp 99.000,-</div>
    <a href="{LINK_WA}" target="_blank" class="btn-wa">👉 AMBIL LISENSI SAYA SEKARANG! 👈</a>
    <div class="urgency-text">⚠️ Peringatan: Harga Early Bird ini hanya berlaku untuk 10 pembeli pertama hari ini.</div>
</div>
""", unsafe_allow_html=True)

# --- 8. BAGIAN FAQ (Tanya Jawab) ---
st.markdown("<h4 style='text-align: center; margin-bottom: 20px;'>Sering Ditanyakan (FAQ)</h4>", unsafe_allow_html=True)

with st.expander("Apakah butuh laptop spesifikasi dewa?"):
    st.write("Tidak! Mesin ini sangat ringan. Bisa dijalankan di Windows 10/11 biasa. Proses render dilakukan dengan metode *Fast-Stream* yang efisien.")

with st.expander("Apakah benar bisa dikendalikan lewat HP?"):
    st.write("Sangat benar! Cukup nyalakan aplikasinya di laptop, Anda akan mendapatkan sebuah Link Lokal. Buka link tersebut di browser HP Anda saat terhubung di WiFi yang sama, dan Anda bisa memproduksi video sambil rebahan!")

with st.expander("Bagaimana cara pengirimannya?"):
    st.write("Setelah pembayaran terkonfirmasi via WhatsApp, Anda akan langsung menerima Link Google Drive berisi File Instalasi Resmi (ZIP) + Video Panduan Cara Pakainya.")

st.markdown("---")
st.caption("<p style='text-align: center;'>© 2024 Kavling Digital. All rights reserved.</p>", unsafe_allow_html=True)
