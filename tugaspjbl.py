import streamlit as st

# Mengonfigurasi judul halaman dan ikon tab browser
st.set_page_config(
    page_title="Matematika Geometri Baru",
    page_icon="📐"
)

# --- BAGIAN SIDEBAR (KIRI) ---
with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Tetap menggunakan logo yo.png milikmu
        st.image("yo.png", width=380) 
        
    st.title("Bangun Datar")
    
    # Menambahkan Trapesium dan Belah Ketupat ke dalam menu pilihan
    pilihan = st.selectbox(
        "Pilihan Bangun Datar",
        ["Persegi", "Persegi Panjang", "Lingkaran", "Trapesium", "Belah Ketupat"]
    )
    
    st.caption("Dibuat oleh Haka Narrendra Tamam")

# --- BAGIAN HALAMAN UTAMA (KANAN) ---
match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung luas dan keliling `persegi`")
        sisi = st.number_input("Masukkan Sisi", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.snow()
            st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung luas dan keliling `persegi panjang`")
        panjang = st.number_input("Masukkan Panjang", min_value=0.0)
        lebar = st.number_input("Masukkan Lebar", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.balloons()
            st.success(f"Luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung luas dan keliling `lingkaran`")
        jari_jari = st.number_input("Masukkan Jari-Jari", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            st.balloons()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric(label="Keliling", value=f"{keliling:.2f}", border=True)

    # --- GANTIAN 1: TRAPESIUM SAMA KAKI ---
    case "Trapesium":
        st.title("Trapesium Sama Kaki")
        st.markdown("Menghitung luas dan keliling `trapesium sama kaki`")
        sisi_atas = st.number_input("Masukkan Sisi Sejajar Atas (a)", min_value=0.0)
        sisi_bawah = st.number_input("Masukkan Sisi Sejajar Bawah (b)", min_value=0.0)
        tinggi = st.number_input("Masukkan Tinggi (t)", min_value=0.0)
        sisi_miring = st.number_input("Masukkan Panjang Sisi Miring", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
            keliling = sisi_atas + sisi_bawah + (2 * sisi_miring) # Keliling trapesium sama kaki
            st.snow()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric(label="Keliling", value=f"{keliling:.2f}", border=True)

    # --- GANTIAN 2: BELAH KETUPAT ---
    case "Belah Ketupat":
        st.title("Belah Ketupat")
        st.markdown("Menghitung luas dan keliling `belah ketupat`")
        d1 = st.number_input("Masukkan Diagonal 1 (d1)", min_value=0.0)
        d2 = st.number_input("Masukkan Diagonal 2 (d2)", min_value=0.0)
        sisi_luar = st.number_input("Masukkan Panjang Sisi Luar", min_value=0.0)
        
        if st.button("Hitung", type="primary"):
            luas = 0.5 * d1 * d2
            keliling = 4 * sisi_luar
            st.balloons()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric(label="Keliling", value=f"{keliling:.2f}", border=True)
                
    case _:
        st.error("Terjadi kesalahan")
