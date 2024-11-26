import random

def generate_numbers():
    
    random.seed(40)
    return [random.randint(0, 100) for _ in range(50)]

def naive_sort(data):
   
    return sorted(data)

if __name__ == "__main__":
    # Menghasilkan bilangan random
    data = generate_numbers()
    print("Sebelum Sorting (Naive):", data)

    # Proses sorting
    hasil_sorting = naive_sort(data)
    print("Sesudah Sorting (Naive):", hasil_sorting)
