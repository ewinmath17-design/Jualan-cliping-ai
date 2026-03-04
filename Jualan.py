import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="AutoClip Cuan Engine - Promo Khusus", page_icon="🚨", layout="centered")

# CSS Kustom untuk mempercantik Landing Page
st.markdown("""
<style>
    .pre-headline { text-align: center; color: #555; font-size: 16px; margin-bottom: 10px; }
    .big-headline { text-align: center; color: #D32F2F; font-size: 38px; font-weight: 900; line-height: 1.2; font-family: 'Arial Black', sans-serif; margin-bottom: 20px; }
    .sub-headline { text-align: center; color: #333; font-size: 20px; font-style: italic; margin-bottom: 30px; }
    .body-text { font-size: 18px; color: #222; line-height: 1.6; }
    .highlight { background-color: #FFFF00; font-weight: bold; }
    .price-box { background-color: #FFF9C4; padding: 25px; border-radius: 12px; border: 3px dashed #FBC02D; text-align: center; margin: 30px 0; }
    .price-coret { text-decoration: line-through; color: #999; font-size: 24px; }
    .price-final { color: #D32F2F; font-size: 36px; font-weight: bold; margin-top: 10px; }
    .cta-button { display: block; width: 100%; text-align: center; background-color: #28a745; color: white !important; padding: 18px; font-size: 24px; font-weight: bold; text-decoration: none; border-radius: 8px; margin-top: 20px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .cta-button:hover { background-color: #218838; transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# --- BAGIAN HEADLINE ---
st.markdown('<div class="pre-headline">Perhatian Khusus untuk: Affiliate TikTok, Content Creator "Faceless", dan Pemilik Akun Publik...</div>', unsafe_allow_html=True)
st.markdown('<div class="big-headline">🚨 BAGAIMANA MENCETAK RATUSAN VIDEO VIRAL DALAM 10 MENIT, TANPA PERLU BUKA CAPCUT, DAN BISA DIKENDALIKAN DARI HP ANDA! 🚨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-headline">Lupakan biaya langganan bulanan aplikasi bule yang mahal. Temukan "Pabrik Gaib" yang akan membedah video, memotong otomatis, dan menulis Judul Clickbait-nya. Cukup 1x Klik!</div>', unsafe_allow_html=True)

st.divider()

# --- BAGIAN MASALAH ---
st.markdown("""
<div class="body-text">
<p>Jujur saja...</p>
<p>Membangun kolam <i>followers</i> di TikTok, Shopee Video, atau IG Reels itu <b>SANGAT MELELAHKAN</b>.</p>
<p>Anda tahu persis bahwa rahasia FYP adalah: <span class="highlight">KONSISTENSI UPLOAD 3-5 VIDEO PER HARI.</span></p>
<p>Tapi, realitanya:</p>
<ul>
    <li>❌ Anda harus <i>download</i> video podcast berjam-jam.</li>
    <li>❌ Anda harus memelototi videonya untuk mencari "Hook" yang menarik.</li>
    <li>❌ Anda harus memotongnya manual di aplikasi HP.</li>
    <li>❌ Anda kebingungan memikirkan teks Judul Clickbait.</li>
</ul>
<p>Satu video saja bisa memakan waktu 1 jam. Kapan Anda punya waktu untuk menikmati hidup?</p>
<p>Ada aplikasi AI luar negeri seperti OpusClip. Ya, mereka bagus. <b>TAPI HARGANYA GILA!</b> Anda harus bayar biaya langganan <b>Rp 300.000 SETIAP BULAN</b>.</p>
</div>
""", unsafe_allow_html=True)

# --- BAGIAN SOLUSI & MEKANISME ---
st.header("Memperkenalkan: Kavling AutoClip Cuan Engine 🤖🎬")
st.markdown("""
<div class="body-text">
<p>Ini BUKAN e-book teori. Ini adalah <b>SOFTWARE AI PRIBADI</b> yang Anda install di laptop Anda sendiri, dan luar biasanya... <b>Bisa Anda kendalikan lewat layar HP Anda!</b></p>
<p>Dilengkapi 3 Mekanisme Unik yang bikin kompetitor menangis:</p>
<ol>
    <li>🎥 <b>Sutradara AI Otomatis:</b> Atur fokus kamera ke tengah, host, atau tamu!</li>
    <li>✍️ <b>Auto-Copywriter AI:</b> AI membedah video dan menuliskan Judul Clickbait untuk Anda.</li>
    <li>🛡️ <b>Tameng Anti-Shadowban:</b> Mesin menyelipkan manipulasi durasi super halus agar bebas peringatan <i>Unoriginal Content</i>!</li>
</ol>
</div>
""", unsafe_allow_html=True)

# --- BAGIAN PENAWARAN & HARGA ---
st.markdown("""
<div class="price-box">
    <p style="font-size: 20px; font-weight: bold; margin-bottom: 5px;">Dapatkan Hak Milik Penuh Hari Ini!</p>
    <p style="margin-bottom: 10px;">Bayar 1x, Nikmati Seumur Hidup (Tanpa Biaya Bulanan)</p>
    <div class="price-coret">Harga Normal: Rp 499.000</div>
    <div class="price-final">HANYA Rp 99.000</div>
</div>
""", unsafe_allow_html=True)

# --- TOMBOL CALL TO ACTION ---
# GANTI LINK DI BAWAH INI DENGAN LINK WHATSAPP / SEJOLI / BERDU MASTER EWIN
link_pembelian = "https://wa.me/6282293274916?text=Halo%20Admin,%20saya%20mau%20beli%20AutoClip%20Cuan%20Engine%20harga%20promo%2099rb!"

st.markdown(f'<a href="{link_pembelian}" target="_blank" class="cta-button">👉 YA! SAYA MAU MESIN CUAN INI SEKARANG 👈</a>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; color: #777; font-size: 14px; margin-top: 10px;">
    <i>⚠️ PERINGATAN: Harga Rp 99.000 ini adalah Harga Early Bird. Harga akan segera naik kembali tanpa pemberitahuan.</i>
</p>
""", unsafe_allow_html=True)
