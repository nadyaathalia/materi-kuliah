# Visualisasi Antrian di RS dengan GTTS untuk pemanggilan Antrian
from gtts import gTTS
import streamlit as st
import os

# Memanggil class Queue dari file queue2.py kamu
import queue2

st.set_page_config(page_title="Antrian Rumah Sakit", layout="centered", page_icon="🏥")

# Title
st.title("🏥 Visualisasi Antrian di RS dengan GTTS")

# Inisialisasi session Antrian
if 'queue2' not in st.session_state:
    st.session_state.queue2 = queue2.Queue()

# ==========================================
# HALAMAN INPUT PASIEN (FRONT OFFICE)
# ==========================================
st.header("➡️ Pendaftaran Pasien")
pasien = st.text_input("Masukkan Nama Pasien:", placeholder="Contoh: Ahmad")

if st.button("Tambah Pasien Ke Antrian"):
    if pasien.strip() != "":
        st.session_state.queue2.enqueue(pasien.strip())
        st.success(f"Pasien '{pasien}' berhasil didaftarkan!")
        # Memicu Streamlit untuk menggambar ulang layar agar nama langsung muncul
        st.rerun() 
    else:
        st.error("Nama pasien tidak boleh kosong!")

# ==========================================
# MENAMPILKAN ANTRIAN SAAT INI
# ==========================================
st.markdown("---")
st.header("📋 Daftar Antrian Saat Ini")

if not st.session_state.queue2.is_empty():
    st.write(f"**Total Pasien Menunggu:** {st.session_state.queue2.size()} orang")
    
    # Loop untuk menampilkan seluruh antrian dari Head sampai Tail
    current = st.session_state.queue2.head
    no = 1
    
    # Membuat container estetik untuk daftar pasien
    with st.expander("Lihat Detail Urutan Antrian", expanded=True):
        while current:
            st.write(f"**[{no}]** Pasien: {current.data}")
            no += 1
            current = current.next
else:
    st.info("Alhamdulillah, saat ini antrian kosong atau semua pasien sudah dilayani.")

# ==========================================
# TOMBOL PANGGIL PASIEN (RUANG DOKTER)
# ==========================================
st.markdown("---")
st.header("🔊 Pemanggilan Pasien")

if st.button("Panggil Pasien Berikutnya 🗣️"):
    if not st.session_state.queue2.is_empty():
        # 1. Ambil nama pasien di antrian paling depan (Head)
        nama_pasien = st.session_state.queue2.head.data
        
        # 2. Proses teks ke suara menggunakan gTTS
        teks_panggilan = f"Pasien atas nama {nama_pasien}, Silahkan Menuju Ruang Dokter."
        tts = gTTS(text=teks_panggilan, lang='id', slow=False)
        
        # 3. Simpan audio dengan nama unik agar tidak bentrok di sistem
        nama_file = f"panggilan_{nama_pasien}.mp3"
        tts.save(nama_file)
        
        # 4. Mainkan audio secara otomatis (Autoplay)
        st.audio(nama_file, format="audio/mp3", autoplay=True)
        st.success(f"Sedang memanggil: **{nama_pasien}**")
        
        # 5. Hapus pasien dari antrian (FIFO - First In First Out)
        st.session_state.queue2.dequeue()
        
        # 6. Beri jeda sedikit lalu refresh halaman agar antrian ter-update di layar
        st.rerun()
    else:
        st.warning("Tidak ada pasien di dalam antrian.")