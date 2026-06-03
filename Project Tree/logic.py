# logic.py

class TreeNode:
    def __init__(self, name, node_type="Kategori", data=None):
        self.name = name
        self.node_type = node_type  # Root, Kategori, Produk
        self.data = data or {}
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class GeneralTree:
    def __init__(self, root_name):
        self.root = TreeNode(root_name, node_type="Root")

    def find_node(self, current_node, name):
        """DFS untuk cari node"""
        if current_node.name.lower() == name.lower():
            return current_node
        for child in current_node.children:
            found = self.find_node(child, name)
            if found:
                return found
        return None

    def find_parent_node(self, current_node, target_name):
        """Cari parent node (untuk hapus)"""
        for child in current_node.children:
            if child.name.lower() == target_name.lower():
                return current_node
            found = self.find_parent_node(child, target_name)
            if found:
                return found
        return None

    def insert_node(self, parent_name, new_node):
        """Insert node baru"""
        parent = self.find_node(self.root, parent_name)
        if parent:
            parent.add_child(new_node)
            return True
        return False

    def remove_node(self, target_name):
        """Hapus node dari pohon"""
        if target_name.lower() == self.root.name.lower():
            raise ValueError("Root tidak boleh dihapus!")
        
        parent = self.find_parent_node(self.root, target_name)
        if parent:
            parent.children = [
                child for child in parent.children
                if child.name.lower() != target_name.lower()
            ]
            return True
        return False

    def count_nodes(self, current_node=None):
        """Hitung total node"""
        if current_node is None:
            current_node = self.root
        count = 1
        for child in current_node.children:
            count += self.count_nodes(child)
        return count

    def get_tree_height(self, current_node=None):
        """Hitung kedalaman tree"""
        if current_node is None:
            current_node = self.root
        if not current_node.children:
            return 0
        return 1 + max(self.get_tree_height(child) for child in current_node.children)

    def get_all_nodes(self, current_node=None):
        """Kumpulkan semua node"""
        if current_node is None:
            current_node = self.root
        nodes = [current_node]
        for child in current_node.children:
            nodes.extend(self.get_all_nodes(child))
        return nodes