import random

def generate_numbers():
    
    random.seed(40)
    return [random.randint(0, 100) for _ in range(50)]

def merge_sort(data):
    
    if len(data) > 1:
        mid = len(data) // 2
        kiri = data[:mid]
        kanan = data[mid:]

        # Rekursi untuk setiap bagian
        merge_sort(kiri)
        merge_sort(kanan)

        # Proses penggabungan
        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

if __name__ == "__main__":
    # Menghasilkan bilangan random
    data = generate_numbers()
    print("Sebelum Sorting (Conquer/Merge Sort):", data)

    # Proses sorting
    merge_sort(data)
    print("Sesudah Sorting (Conquer/Merge Sort):", data)
