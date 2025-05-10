class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Thêm để sử dụng lại lớp này cho cây AVL
class BST:
    def __init__(self):
        self.root = None
        self.comparisons = 0  # Đếm số lần so sánh
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, root, key):
        # Nếu cây rỗng, tạo nút mới
        if not root:
            return Node(key)
        # Nếu không, đệ quy xuống cây
        self.comparisons += 1
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root
    def search(self, key):
        self.comparisons = 0  # Đặt lại bộ đếm
        return self._search(self.root, key)
    
    def _search(self, root, key):
        # Nếu cây rỗng hoặc tìm thấy khóa
        if not root:
            return False
        self.comparisons += 1
        if root.key == key:
            return True
        self.comparisons += 1
        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, root, key):
        # Nếu cây rỗng
        if not root:
            return None
        # Tìm nút cần xóa
        self.comparisons += 1
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            self.comparisons += 1
            root.right = self._delete(root.right, key)
        else:
            # Nút có 0 hoặc 1 con
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Nút có 2 con: Tìm phần tử kế thừa trật tự nội (successor)
            successor = self._find_min(root.right)
            root.key = successor.key
            root.right = self._delete(root.right, successor.key)
        return root
    def _find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    def height(self):
        return self._height(self.root)
    def _height(self, root):
        if not root:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result
    def _in_order(self, root, result):
        if root:
            self._in_order(root.left, result)
            result.append(root.key)
            self._in_order(root.right, result)
            
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None
        self.comparisons = 0  # Đếm số lần so sánh
        self.rotations = 0    # Đếm số lần xoay
    def _height(self, node):
        if not node:
            return 0
        return node.height
    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    def _update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self._height(node.left), self._height(node.right))
    
    def _right_rotate(self, y):
        self.rotations += 1
        x = y.left
        T2 = x.right
        # Thực hiện xoay
        x.right = y
        y.left = T2
        # Cập nhật chiều cao
        self._update_height(y)
        self._update_height(x)
        return x
    def _left_rotate(self, x):
        self.rotations += 1
        y = x.right
        T2 = y.left
        # Thực hiện xoay
        y.left = x
        x.right = T2
        
        # Cập nhật chiều cao
        self._update_height(x)
        self._update_height(y)
        return y
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, root, key):
        # Bước 1: Chèn thông thường như BST
        if not root:
            return AVLNode(key)
        self.comparisons += 1
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        # Bước 2: Cập nhật chiều cao của nút hiện tại
        self._update_height(root)
        # Bước 3: Kiểm tra hệ số cân bằng
        balance = self._balance_factor(root)
        # Trường hợp trái-trái
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)
        # Trường hợp phải-phải
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)
        # Trường hợp trái-phải
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        # Trường hợp phải-trái
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        return root
    def search(self, key):
        self.comparisons = 0  # Đặt lại bộ đếm
        return self._search(self.root, key)
    
    def _search(self, root, key):
        if not root:
            return False
        self.comparisons += 1
        if root.key == key:
            return True
        self.comparisons += 1
        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, root, key):
        # Bước 1: Xóa thông thường như BST
        if not root:
            return None
        self.comparisons += 1
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            self.comparisons += 1
            root.right = self._delete(root.right, key)
        else:
            # Nút có 0 hoặc 1 con
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Nút có 2 con: Tìm successor
            successor = self._find_min(root.right)
            root.key = successor.key
        if not root:
            return None
        # Bước 2: Cập nhật chiều cao
        self._update_height(root)
        # Bước 3: Kiểm tra hệ số cân bằng
        balance = self._balance_factor(root)
        # Trường hợp trái-trái
        if balance > 1 and self._balance_factor(root.left) >= 0:
            return self._right_rotate(root)
        # Trường hợp trái-phải
        if balance > 1 and self._balance_factor(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        # Trường hợp phải-phải
        if balance < -1 and self._balance_factor(root.right) <= 0:
            return self._left_rotate(root)
        # Trường hợp phải-trái
        if balance < -1 and self._balance_factor(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        return root
    def _find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def height(self):
        return self._height(self.root)
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result
    def _in_order(self, root, result):
        if root:
            self._in_order(root.left, result)
            result.append(root.key)
            self._in_order(root.right, result)

import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class TreeVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trình Mô Phỏng Cây Nhị Phân")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")
        # Khởi tạo các cây
        self.bst = BST()
        self.avl = AVLTree()
        # Tạo khung chính
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        # Khung điều khiển
        self.control_frame = ttk.LabelFrame(self.main_frame, text="Điều khiển")
        self.control_frame.pack(fill=tk.X, padx=5, pady=5)
        # Thêm các nút và ô nhập liệu
        ttk.Label(self.control_frame, text="Giá trị:").grid(row=0, column=0, padx=5, pady=5)
        self.value_entry = ttk.Entry(self.control_frame, width=10)
        self.value_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Chèn", command=self.insert_value).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Tìm kiếm", command=self.search_value).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Xóa", command=self.delete_value).grid(row=0, column=4, padx=5, pady=5)
        ttk.Label(self.control_frame, text="Số lượng:").grid(row=0, column=5, padx=5, pady=5)
        self.count_entry = ttk.Entry(self.control_frame, width=10)
        self.count_entry.grid(row=0, column=6, padx=5, pady=5)
        self.count_entry.insert(0, "100")
        ttk.Button(self.control_frame, text="Tạo ngẫu nhiên", command=self.random_insert).grid(row=0, column=7, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Tạo theo thứ tự", command=self.ordered_insert).grid(row=0, column=8, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Xóa tất cả", command=self.clear_trees).grid(row=0, column=9, padx=5, pady=5)
        ttk.Button(self.control_frame, text="So sánh hiệu suất", command=self.compare_performance).grid(row=0, column=10, padx=5, pady=5)
        # Khung hiển thị cây
        self.trees_frame = ttk.Frame(self.main_frame)
        self.trees_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Khung cho BST
        self.bst_frame = ttk.LabelFrame(self.trees_frame, text="Cây nhị phân tìm kiếm (BST)")
        self.bst_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Khung cho AVL
        self.avl_frame = ttk.LabelFrame(self.trees_frame, text="Cây AVL")
        self.avl_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # Tạo các canvas cho cả hai cây
        self.fig_bst, self.ax_bst = plt.subplots(figsize=(5, 4))
        self.canvas_bst = FigureCanvasTkAgg(self.fig_bst, master=self.bst_frame)
        self.canvas_bst.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.fig_avl, self.ax_avl = plt.subplots(figsize=(5, 4))
        self.canvas_avl = FigureCanvasTkAgg(self.fig_avl, master=self.avl_frame)
        self.canvas_avl.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        # Khung thông tin
        self.info_frame = ttk.LabelFrame(self.main_frame, text="Thông tin")
        self.info_frame.pack(fill=tk.X, padx=5, pady=5)
        # Thêm các nhãn thông tin
        self.bst_info = ttk.Label(self.info_frame, text="BST: Chiều cao = 0, Số phép so sánh = 0")
        self.bst_info.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.avl_info = ttk.Label(self.info_frame, text="AVL: Chiều cao = 0, Số phép so sánh = 0, Số phép xoay = 0")
        self.avl_info.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        # Khung biểu đồ hiệu suất
        self.performance_frame = ttk.LabelFrame(self.main_frame, text="Biểu đồ hiệu suất")
        self.performance_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.fig_perf, self.ax_perf = plt.subplots(figsize=(10, 4))
        self.canvas_perf = FigureCanvasTkAgg(self.fig_perf, master=self.performance_frame)
        self.canvas_perf.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        # Vẽ cây ban đầu
        self.draw_trees()
    def insert_value(self):
        try:
            value = int(self.value_entry.get())
            # Chèn vào cả hai cây
            self.bst.insert(value)
            self.avl.insert(value)
            # Cập nhật giao diện
            self.update_info()
            self.draw_trees()
            self.value_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ.")
    def search_value(self):
        try:
            value = int(self.value_entry.get())
            # Tìm kiếm trong cả hai cây
            bst_found = self.bst.search(value)
            avl_found = self.avl.search(value)
                        # Hiển thị kết quả
            bst_msg = f"BST: {'Tìm thấy' if bst_found else 'Không tìm thấy'} ({self.bst.comparisons} phép so sánh)"
            avl_msg = f"AVL: {'Tìm thấy' if avl_found else 'Không tìm thấy'} ({self.avl.comparisons} phép so sánh)"
            messagebox.showinfo("Kết quả tìm kiếm", f"{bst_msg}\n{avl_msg}")
            self.update_info()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ.")
    def delete_value(self):
        try:
            value = int(self.value_entry.get())
            # Xóa khỏi cả hai cây
            self.bst.delete(value)
            self.avl.delete(value)
            # Cập nhật giao diện
            self.update_info()
            self.draw_trees()
            self.value_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ.")
    def random_insert(self):
        try:
            count = int(self.count_entry.get())
            if count > 1000:
                messagebox.showwarning("Cảnh báo", "Số lượng lớn có thể làm chậm hệ thống. Sẽ giới hạn ở 1000.")
                count = 1000
            self.clear_trees()
            # Tạo danh sách giá trị ngẫu nhiên
            values = random.sample(range(1, count * 10), count)
            # Chèn vào cả hai cây
            start_time_bst = time.time()
            for value in values:
                self.bst.insert(value)
            bst_time = time.time() - start_time_bst
            start_time_avl = time.time()
            for value in values:
                self.avl.insert(value)
            avl_time = time.time() - start_time_avl
            # Hiển thị thông tin thời gian
            messagebox.showinfo("Thời gian chèn",
                               f"BST: {bst_time:.6f} giây\nAVL: {avl_time:.6f} giây")
            # Cập nhật giao diện
            self.update_info()
            self.draw_trees()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ.")
    def ordered_insert(self):
        try:
            count = int(self.count_entry.get())
            if count > 1000:
                messagebox.showwarning("Cảnh báo", "Số lượng lớn có thể làm chậm hệ thống. Sẽ giới hạn ở 1000.")
                count = 1000
            self.clear_trees()
            # Tạo danh sách các giá trị theo thứ tự
            values = list(range(1, count + 1))
            # Chèn vào cả hai cây
            start_time_bst = time.time()
            for value in values:
                self.bst.insert(value)
            bst_time = time.time() - start_time_bst
            start_time_avl = time.time()
            for value in values:
                self.avl.insert(value)
            avl_time = time.time() - start_time_avl
            # Hiển thị thông tin thời gian
            messagebox.showinfo("Thời gian chèn",
                               f"BST: {bst_time:.6f} giây\nAVL: {avl_time:.6f} giây")
            # Cập nhật giao diện
            self.update_info()
            self.draw_trees()
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ.")
    def clear_trees(self):
        self.bst = BST()
        self.avl = AVLTree()
        self.update_info()
        self.draw_trees()
    def update_info(self):
        bst_height = self.bst.height()
        avl_height = self.avl.height()
        self.bst_info.config(text=f"BST: Chiều cao = {bst_height}, Số phép so sánh = {self.bst.comparisons}")
        self.avl_info.config(text=f"AVL: Chiều cao = {avl_height}, Số phép so sánh = {self.avl.comparisons}, Số phép xoay = {self.avl.rotations}")
    def draw_trees(self):
        # Xóa các biểu đồ cũ
        self.ax_bst.clear()
        self.ax_avl.clear()
        # Vẽ các cây
        self._draw_tree(self.bst.root, self.ax_bst, 0, 0, 100, "BST")
        self._draw_tree(self.avl.root, self.ax_avl, 0, 0, 100, "AVL")
        # Thiết lập các thuộc tính của biểu đồ
        for ax, title in [(self.ax_bst, "Cây nhị phân tìm kiếm"), (self.ax_avl, "Cây AVL")]:
            ax.set_title(title)
            ax.set_xlim(-10, 110)
            ax.set_ylim(-10, 110)
            ax.axis('off')
        # Cập nhật canvas
        self.canvas_bst.draw()
        self.canvas_avl.draw()
    def _draw_tree(self, node, ax, x, y, width, tree_type, level=0):
        if not node:
            return
        # Tính toán vị trí
        node_size = max(5, 20 - level)  # Nút nhỏ dần theo độ sâu
        y_offset = 15  # Khoảng cách dọc giữa các nút
        # Vẽ các cạnh trước (để nút nằm trên cạnh)
        if node.left:
            next_x = x - width / 2
            next_y = y - y_offset
            ax.plot([x, next_x], [y, next_y], 'b-', linewidth=1)
            self._draw_tree(node.left, ax, next_x, next_y, width / 2, tree_type, level + 1)
        if node.right:
            next_x = x + width / 2
            next_y = y - y_offset
            ax.plot([x, next_x], [y, next_y], 'b-', linewidth=1)
            self._draw_tree(node.right, ax, next_x, next_y, width / 2, tree_type, level + 1)
        # Vẽ nút
        circle = plt.Circle((x, y), node_size / 2, fill=True, color='skyblue', edgecolor='blue')
        ax.add_patch(circle)
        # Thêm nhãn
        ax.text(x, y, str(node.key), ha='center', va='center', fontsize=max(7, 10 - level))
        # Thêm giá trị chiều cao cho AVL
        if tree_type == "AVL":
            ax.text(x, y - node_size / 2 - 1, f"h:{node.height}", ha='center', va='top', fontsize=6)
    def compare_performance(self):
        try:
            # Xóa biểu đồ cũ
            self.ax_perf.clear()
            # Chuẩn bị dữ liệu
            sizes = [10, 100, 1000]
            scenarios = ["Ngẫu nhiên", "Tăng dần"]
            # Tạo các cấu trúc dữ liệu để lưu kết quả
            bst_heights = [[], []]
            avl_heights = [[], []]
            bst_search_comps = [[], []]
            avl_search_comps = [[], []]
            bst_times = [[], []]
            avl_times = [[], []]
            for s_idx, scenario in enumerate(scenarios):
                for size in sizes:
                    # Tạo cây mới cho mỗi thử nghiệm
                    bst = BST()
                    avl = AVLTree()
                    # Chuẩn bị dữ liệu
                    if scenario == "Ngẫu nhiên":
                        values = random.sample(range(1, size * 10), size)
                    else:  # Tăng dần
                        values = list(range(1, size + 1))
                    # Đo thời gian chèn
                    start_time = time.time()
                    for val in values:
                        bst.insert(val)
                    bst_time = time.time() - start_time
                    start_time = time.time()
                    for val in values:
                        avl.insert(val)
                    avl_time = time.time() - start_time
                    # Ghi lại chiều cao và thời gian
                    bst_heights[s_idx].append(bst.height())
                    avl_heights[s_idx].append(avl.height())
                    bst_times[s_idx].append(bst_time)
                    avl_times[s_idx].append(avl_time)
                    # Đo hiệu suất tìm kiếm (sử dụng giá trị ở giữa khoảng làm mục tiêu)
                    search_target = size * 5
                    bst.search(search_target)
                    avl.search(search_target)
                    bst_search_comps[s_idx].append(bst.comparisons)
                    avl_search_comps[s_idx].append(avl.comparisons)
            
            # Hiển thị kết quả dưới dạng biểu đồ
            x = np.arange(len(sizes))
            width = 0.2
            self.ax_perf.set_title("So sánh hiệu suất BST và AVL")
            # Vẽ biểu đồ chiều cao cho dữ liệu ngẫu nhiên
            self.ax_perf.bar(x - 1.5*width, bst_heights[0], width, label='BST (Ngẫu nhiên)', color='blue')
            self.ax_perf.bar(x - 0.5*width, avl_heights[0], width, label='AVL (Ngẫu nhiên)', color='green')
            # Vẽ biểu đồ chiều cao cho dữ liệu tăng dần
            self.ax_perf.bar(x + 0.5*width, bst_heights[1], width, label='BST (Tăng dần)', color='darkblue')
            self.ax_perf.bar(x + 1.5*width, avl_heights[1], width, label='AVL (Tăng dần)', color='darkgreen')
            self.ax_perf.set_ylabel('Chiều cao cây')
            self.ax_perf.set_xlabel('Kích thước dữ liệu')
            self.ax_perf.set_xticks(x)
            self.ax_perf.set_xticklabels(sizes)
            self.ax_perf.legend()
            # Thêm giá trị lên các cột
            for i in range(len(sizes)):
                for j, heights in enumerate([bst_heights[0], avl_heights[0], bst_heights[1], avl_heights[1]]):
                    offset = (j - 1.5) * width
                    self.ax_perf.text(i + offset, heights[i] + 1, str(heights[i]),
                                     ha='center', va='bottom', fontsize=8)
            # Cập nhật canvas
            self.canvas_perf.draw()
            # Hiển thị thông tin chi tiết
            info_msg = "Kết quả so sánh chi tiết:\n\n" 
            for s_idx, scenario in enumerate(scenarios):
                info_msg += f"--- {scenario} ---\n"
                for i, size in enumerate(sizes):
                    info_msg += f"Kích thước {size}:\n"
                    info_msg += f"  BST: Chiều cao={bst_heights[s_idx][i]}, Thời gian={bst_times[s_idx][i]:.6f}s, So sánh tìm kiếm={bst_search_comps[s_idx][i]}\n"
                    info_msg += f"  AVL: Chiều cao={avl_heights[s_idx][i]}, Thời gian={avl_times[s_idx][i]:.6f}s, So sánh tìm kiếm={avl_search_comps[s_idx][i]}\n"
                info_msg += "\n"
            messagebox.showinfo("Kết quả so sánh chi tiết", info_msg)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")
if __name__ == "__main__":
    import numpy as np
    root = tk.Tk()
    app = TreeVisualizerApp(root)
    root.mainloop()
