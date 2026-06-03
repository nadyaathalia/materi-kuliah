# ecommerce.py
from logic import TreeNode, GeneralTree

class EcommerceCatalog(GeneralTree):
    def __init__(self, store_name):
        super().__init__(store_name)

    def add_category(self, parent_name, category_name):
        """Tambah kategori"""
        if not category_name.strip():
            raise ValueError("Nama kategori tidak boleh kosong.")
        if self.find_node(self.root, category_name):
            raise ValueError(f"Nama '{category_name}' sudah ada.")
        
        parent = self.find_node(self.root, parent_name)
        if not parent:
            raise ValueError(f"Parent '{parent_name}' tidak ditemukan.")
        if parent.node_type == "Produk":
            raise ValueError("Produk tidak bisa punya sub-kategori!")
        
        new_cat = TreeNode(category_name, node_type="Kategori")
        self.insert_node(parent_name, new_cat)

    def add_product(self, category_name, product_name, price, stock):
        """Tambah produk"""
        if not product_name.strip():
            raise ValueError("Nama produk tidak boleh kosong.")
        if price < 0 or stock < 0:
            raise ValueError("Harga/stok tidak boleh negatif.")
        if self.find_node(self.root, product_name):
            raise ValueError(f"Produk '{product_name}' sudah ada.")
        
        parent = self.find_node(self.root, category_name)
        if not parent:
            raise ValueError(f"Kategori '{category_name}' tidak ditemukan.")
        if parent.node_type == "Produk":
            raise ValueError("Tidak bisa tambah produk ke dalam produk!")
        
        new_prod = TreeNode(product_name, node_type="Produk", 
                           data={"harga": price, "stok": stock})
        self.insert_node(category_name, new_prod)

    def get_all_categories(self, current_node=None):
        """Ambil semua kategori"""
        if current_node is None:
            current_node = self.root
        cats = []
        if current_node.node_type in ["Root", "Kategori"]:
            cats.append(current_node.name)
            for child in current_node.children:
                cats.extend(self.get_all_categories(child))
        return cats

    def get_all_deletable_nodes(self, current_node=None):
        """Ambil semua node untuk hapus"""
        if current_node is None:
            current_node = self.root
        nodes = []
        if current_node.node_type != "Root":
            nodes.append(current_node.name)
        for child in current_node.children:
            nodes.extend(self.get_all_deletable_nodes(child))
        return nodes

    def delete_item(self, name):
        """Hapus item"""
        return self.remove_node(name)

    def get_statistics(self):
        """Statistik katalog"""
        all_nodes = self.get_all_nodes()
        products = [n for n in all_nodes if n.node_type == "Produk"]
        
        total_value = sum(p.data['harga'] * p.data['stok'] for p in products)
        total_stock = sum(p.data['stok'] for p in products)
        total_cat = sum(1 for n in all_nodes if n.node_type == "Kategori")
        
        return {
            'total_nodes': len(all_nodes),
            'total_kategori': total_cat,
            'total_produk': len(products),
            'tree_height': self.get_tree_height(),
            'total_inventory_value': total_value,
            'total_stock': total_stock
        }

    def generate_graphviz_structure(self, dot_graph, current_node=None):
        """Render ke Graphviz"""
        if current_node is None:
            current_node = self.root

        if current_node.node_type == "Root":
            dot_graph.node(current_node.name, current_node.name, 
                          shape="house", style="filled", fillcolor="#ffb6c1")
        elif current_node.node_type == "Kategori":
            dot_graph.node(current_node.name, current_node.name,
                          shape="folder", style="filled", fillcolor="#ffd700")
        else:  # Produk
            label = f"{current_node.name}\nRp {current_node.data['harga']:,}\nStok: {current_node.data['stok']}"
            dot_graph.node(current_node.name, label=label,
                          shape="note", style="filled", fillcolor="#98fb98")

        for child in current_node.children:
            self.generate_graphviz_structure(dot_graph, child)
            dot_graph.edge(current_node.name, child.name)