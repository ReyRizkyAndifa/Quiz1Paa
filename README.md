Nama : Rey Rizky Andifa
Nim : F55123079


Analisis Quiz 2 :
## Analisis Best Case
### Naive Sort
- Kompleksitas: O(n log n)
- Meskipun data sudah terurut, fungsi `sorted()` tetap membandingkan setiap elemen.

### Merge Sort (Conquer Method)
- Kompleksitas: O(n log n)
- Penjelasan: Best case tetap O(n log n) karena rekursi dilakukan untuk membagi array hingga ukuran terkecil (1 elemen).

## Kesimpulan
Kedua metode memiliki kompleksitas waktu yang sama, namun Merge Sort lebih efisien untuk digunakan pada data yang lebih besar karena struktur divide and conquer-nya.
