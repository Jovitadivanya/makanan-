import streamlit as st

# Konfigurasi Halaman Website
st.set_page_config(page_title="Warung Nusantara & Paket Hemat", page_icon="🍽️", layout="wide")

# Inisialisasi keranjang belanja di session_state
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# Data Menu Makanan, Minuman, dan Paket Hemat
menu_paket = [
    {
        "nama": "Paket Hemat 1: Nasi Goreng Spesial + Es Teh Manis",
        "deskripsi": "Lebih hemat Rp 5.000! Sudah termasuk Nasi Goreng Spesial dan Es Teh Manis segar.",
        "harga": 25000,
        "harga_asli": 30000,
        "gambar": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=500"
    },
    {
        "nama": "Paket Hemat 2: Ayam Bakar Madu + Nasi + Es Jeruk",
        "deskripsi": "Lebih hemat Rp 6.000! Ayam bakar bumbu madu, nasi hangat, lalapan, sambal, dan Es Jeruk.",
        "harga": 32000,
        "harga_asli": 38000,
        "gambar": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=500"
    },
    {
        "nama": "Paket Hemat 3: Mie Ayam Bakso + Es Teh Lemon",
        "deskripsi": "Lebih hemat Rp 4.000! Mie ayam porsi pas dengan bakso sapi dan Es Teh Lemon.",
        "harga": 23000,
        "harga_asli": 27000,
        "gambar": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=500"
    }
]

menu_makanan = [
    {"nama": "Nasi Goreng Spesial", "harga": 22000, "deskripsi": "Nasi goreng dengan telur, ayam suwir, dan kerupuk."},
    {"nama": "Ayam Bakar Madu + Nasi", "harga": 28000, "deskripsi": "Ayam bakar oles madu lengkap dengan nasi, sambal, dan lalapan."},
    {"nama": "Mie Ayam Bakso", "harga": 19000, "deskripsi": "Mie kenyal dengan topping ayam kecap dan 2 butir bakso."},
    {"nama": "Sate Ayam (10 Tusuk) + Lontong", "harga": 26000, "deskripsi": "Sate ayam bumbu kacang khas Madura."}
]

menu_minuman = [
    {"nama": "Es Teh Manis", "harga": 8000, "deskripsi": "Teh melati seduh dengan es batu."},
    {"nama": "Es Jeruk Peras", "harga": 10000, "deskripsi": "Jeruk peras asli segar."},
    {"nama": "Es Teh Lemon", "harga": 8000, "deskripsi": "Perpaduan teh dan perasan lemon segar."},
    {"nama": "Air Mineral", "harga": 5000, "deskripsi": "Air mineral botol 600ml."}
]

# Fungsi menambah item ke keranjang
def tambah_ke_keranjang(nama, harga):
    st.session_state.keranjang.append({"nama": nama, "harga": harga})
    st.toast(f"✅ {nama} ditambahkan ke keranjang!")

# Header Website
st.title("🍽️ Kedai Makan Nusantara")
st.write("Pilih menu favoritmu atau ambil **Paket Hemat** (Makan + Minum) untuk harga lebih terjangkau!")
st.divider()

# Layout Utama: Kiri untuk Menu, Kanan untuk Keranjang Pesanan
col_menu, col_keranjang = st.columns([2.2, 1])

with col_menu:
    # Bagian 1: Paket Hemat (Highlight)
    st.subheader("🔥 Pilihan Paket Hemat (Sudah Termasuk Makan & Minum)")
    cols_paket = st.columns(3)
    for idx, paket in enumerate(menu_paket):
        with cols_paket[idx]:
            with st.container(border=True):
                st.image(paket["gambar"], use_container_width=True)
                st.markdown(f"**{paket['nama']}**")
                st.caption(paket["deskripsi"])
                st.markdown(f"~~Rp {paket['harga_asli']:,}~~ ➡️ **Rp {paket['harga']:,}**")
                if st.button("Pesan Paket", key=f"paket_{idx}", use_container_width=True):
                    tambah_ke_keranjang(paket["nama"], paket["harga"])

    st.divider()

    # Bagian 2: Menu Satuan (Tab Makanan & Minuman)
    st.subheader("📋 Menu Satuan")
    tab1, tab2 = st.tabs(["🍛 Makanan Satuan", "🥤 Minuman Satuan"])

    with tab1:
        for idx, item in enumerate(menu_makanan):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"**{item['nama']}** — Rp {item['harga']:,}")
                    st.caption(item["deskripsi"])
                with c2:
                    if st.button("Tambah", key=f"mkn_{idx}", use_container_width=True):
                        tambah_ke_keranjang(item["nama"], item["harga"])

    with tab2:
        for idx, item in enumerate(menu_minuman):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"**{item['nama']}** — Rp {item['harga']:,}")
                    st.caption(item["deskripsi"])
                with c2:
                    if st.button("Tambah", key=f"mnm_{idx}", use_container_width=True):
                        tambah_ke_keranjang(item["nama"], item["harga"])

with col_keranjang:
    st.subheader("🛒 Keranjang Pesanan")
    with st.container(border=True):
        if len(st.session_state.keranjang) == 0:
            st.info("Keranjang masih kosong. Silakan pilih menu di samping.")
        else:
            total_harga = 0
            for i, item in enumerate(st.session_state.keranjang):
                st.write(f"{i+1}. {item['nama']} — **Rp {item['harga']:,}**")
                total_harga += item["harga"]

            st.divider()
            st.markdown(f"### Total: Rp {total_harga:,}")

            # Form Checkout
            nama_pemesan = st.text_input("Nama Pemesan")
            nomor_meja = st.text_input("Nomor Meja / Alamat Pengiriman")
            metode_bayar = st.selectbox("Metode Pembayaran", ["QRIS", "Transfer Bank", "Tunai (Bayar di Kasir)"])

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("Kosongkan", use_container_width=True):
                    st.session_state.keranjang = []
                    st.rerun()
            with col_btn2:
                if st.button("Pesan Sekarang", type="primary", use_container_width=True):
                    if nama_pemesan and nomor_meja:
                        st.success(f"Terima kasih **{nama_pemesan}**! Pesanan sebesar **Rp {total_harga:,}** sedang diproses untuk **{nomor_meja}**.")
                        st.session_state.keranjang = []
                    else:
                        st.warning("Mohon isi Nama Pemesan dan Nomor Meja/Alamat terlebih dahulu.")