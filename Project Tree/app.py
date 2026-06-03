# app.py
import streamlit as st
import graphviz
from ecommerce import EcommerceCatalog

st.set_page_config(layout="wide", page_title="E-Commerce Catalog", page_icon="🛒")
st.title("🛒 E-Commerce Catalog Manager")
st.caption("Struktur Data: General Tree | UAS Struktur Data (INF62305)")
st.markdown("**Manajemen katalog e-commerce dengan hierarki kategori**")

# Inisialisasi
if 'catalog' not in st.session_state:
    cat = EcommerceCatalog("TokoPusat")
    cat.add_category("TokoPusat", "Elektronik")
    cat.add_category("TokoPusat", "Pakaian")
    cat.add_category("Elektronik", "Komputer")
    cat.add_category("Elektronik", "Mobile")
    cat.add_product("Komputer", "Laptop Asus", 8500000, 15)
    cat.add_product("Komputer", "Desktop Gaming", 12000000, 8)
    cat.add_product("Mobile", "Smartphone", 4500000, 25)
    cat.add_product("Mobile", "Tablet", 5000000, 12)
    cat.add_category("Pakaian", "Pria")
    cat.add_category("Pakaian", "Wanita")
    cat.add_product("Pria", "Kemeja", 250000, 50)
    cat.add_product("Wanita", "Dress", 350000, 35)
    st.session_state.catalog = cat

fs = st.session_state.catalog

# Sidebar - Statistik
with st.sidebar:
    st.header("📊 Statistik")
    stats = fs.get_statistics()
    col1, col2 = st.columns(2)
    col1.metric("📦 Produk", stats['total_produk'])
    col2.metric("📁 Kategori", stats['total_kategori'])
    col1.metric("🌳 Depth", stats['tree_height'])
    col2.metric("📊 Node", stats['total_nodes'])
    st.divider()
    st.metric("💰 Nilai", f"Rp {stats['total_inventory_value']:,}")
    st.metric("📦 Total Stok", stats['total_stock'])

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["➕ Tambah", "🗑️ Hapus", "🔍 Cari", "📊 Visualisasi"])

# TAB 1: Tambah
with tab1:
    st.header("Tambah Kategori & Produk")
    col1, col2 = st.columns(2)
    categories = fs.get_all_categories()
    
    with col1:
        st.subheader("📁 Kategori")
        with st.form("form_cat"):
            parent = st.selectbox("Parent:", categories, key="p1")
            name = st.text_input("Nama:")
            if st.form_submit_button("Tambah", use_container_width=True):
                try:
                    fs.add_category(parent, name)
                    st.success("✅ Sukses!")
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
    
    with col2:
        st.subheader("📦 Produk")
        with st.form("form_prod"):
            parent = st.selectbox("Kategori:", categories, key="p2")
            name = st.text_input("Nama:")
            price = st.number_input("Harga:", min_value=0, step=10000)
            stock = st.number_input("Stok:", min_value=0, step=1)
            if st.form_submit_button("Tambah", use_container_width=True):
                try:
                    fs.add_product(parent, name, int(price), int(stock))
                    st.success("✅ Sukses!")
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

# TAB 2: Hapus
with tab2:
    st.header("Hapus Item")
    deletable = fs.get_all_deletable_nodes()
    
    if deletable:
        st.warning("⚠️ Hapus kategori = hapus semua produk di dalamnya")
        with st.form("form_del"):
            item = st.selectbox("Pilih:", deletable)
            confirm = st.checkbox("Yakin?")
            if st.form_submit_button("Hapus", use_container_width=True):
                if confirm:
                    try:
                        fs.delete_item(item)
                        st.success(f"✅ '{item}' dihapus!")
                        st.rerun()
                    except ValueError as e:
                        st.error(str(e))
                else:
                    st.error("Centang dulu")

# TAB 3: Cari
with tab3:
    st.header("Cari Produk")
    keyword = st.text_input("Nama produk:")
    if keyword:
        node = fs.find_node(fs.root, keyword)
        if node and node.node_type == "Produk":
            st.success(f"✅ Ditemukan!")
            st.write(f"*Nama:* {node.name}")
            st.write(f"*Harga:* Rp {node.data['harga']:,}")
            st.write(f"*Stok:* {node.data['stok']}")
        else:
            st.error("❌ Produk tidak ditemukan.")

# TAB 4: Visualisasi
with tab4:
    st.header("Visualisasi Tree")
    dot = graphviz.Digraph(engine="dot")
    dot.attr(rankdir='TB')
    fs.generate_graphviz_structure(dot)
    st.graphviz_chart(dot, use_container_width=True)

st.divider()
st.caption("General Tree Implementation | UAS Struktur Data")