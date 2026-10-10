from node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    # Menambah data
    def tambah(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node_baru

    # Menampilkan data
    def tampil(self):
        if self.head is None:
            print("Linked List kosong")
            return

        current = self.head

        while current is not None:
            print(
                current.data[0],
                "-",
                current.data[1],
                "- Rp",
                current.data[2],
                "- Stok:",
                current.data[3]
            )

            current = current.next

    # Menghapus data
    def hapus(self, kode):
        if self.head is None:
            return False

        # Jika data yang dihapus adalah data pertama
        if self.head.data[0] == kode:
            self.head = self.head.next
            return True

        current = self.head

        while current.next is not None:
            if current.next.data[0] == kode:
                current.next = current.next.next
                return True

            current = current.next

        return False