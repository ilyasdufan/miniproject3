class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def merge_sort(self, key, ascending=True):
        if not self.head or not self.head.next:
            return

        def merge(left, right):
            result = LinkedList()
            while left and right:
                if (left.data[key] < right.data[key]) if ascending else (left.data[key] > right.data[key]):
                    result.insert_at_end(left.data)
                    left = left.next
                else:
                    result.insert_at_end(right.data)
                    right = right.next

            while left:
                result.insert_at_end(left.data)
                left = left.next

            while right:
                result.insert_at_end(right.data)
                right = right.next

            return result

        def split(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        if self.head.next:
            left, right = split(self.head)
            left_list = LinkedList()
            left_list.head = left
            right_list = LinkedList()
            right_list.head = right

            left_list.merge_sort(key, ascending)
            right_list.merge_sort(key, ascending)

            self.head = merge(left_list.head, right_list.head)


# Data user dan admin menggunakan linked list
class UserDataLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add_user(self, username, password, saldo):
        self.insert_at_end({"username": username, "password": password, "saldo": saldo})

    def sort_users(self, key, ascending=True):
        self.merge_sort(key, ascending)


# Data Miniatur menggunakan linked list
class MiniaturDataLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add_miniatur(self, nama, harga, deskripsi):
        self.insert_at_end({"nama": nama, "harga": harga, "deskripsi": deskripsi})

    def sort_miniatures(self, key, ascending=True):
        self.merge_sort(key, ascending)


# Fungsi login user
def user_login(user_list):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    current = user_list.head
    while current:
        if current.data["username"] == username and current.data["password"] == password:
            return username
        current = current.next
    print("Login gagal. Username atau password salah.")
    return None

# Fungsi login admin
def admin_login(admin_list):
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    current = admin_list.head
    while current:
        if current.data["username"] == username and current.data["password"] == password:
            return username
        current = current.next
    print("Login admin gagal. Username atau password salah.")
    return None

# Fungsi top up saldo
def top_up_balance(username, user_list):
    amount = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
    current = user_list.head
    while current:
        if current.data["username"] == username:
            current.data["saldo"] += amount
            print(f"Saldo Anda sekarang: {current.data['saldo']}")
            return
        current = current.next
    print("Username tidak ditemukan.")

# Fungsi tampilan menu untuk admin
def admin_menu():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            break
        else:
            print("Pilihan tidak valid.")

# Program utama
user_list = UserDataLinkedList()
admin_list = UserDataLinkedList()
miniatur_list = MiniaturDataLinkedList()

while True:
    print("\nSelamat datang di Toko miniatur")
    print("1. Login User")
    print("2. Login Admin")
    print("3. Keluar")
    choice = input("Pilih menu: ")
    if choice == "1":
        username = user_login(user_list)
        if username:
            top_up_balance(username, user_list)
    elif choice == "2":
        admin_username = admin_login(admin_list)
        if admin_username:
            admin_menu()
    elif choice == "3":
        break
    else:
        print("Pilihan tidak valid.")
