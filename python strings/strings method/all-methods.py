# --- String Method Demonstration Program ---

# String dasar yang digunakan untuk pengujian
s = "belajar python"
s_case = "iNi AdALaH CONTOH"
s_trim = "  spasi di kedua sisi  "
s_num = "12345"
s_alnum = "Python3"
s_split = "apel,pisang,ceri"
s_join = ["Halo", "Dunia", "Python"]
s_format = "Harga: {price:.2f} | Produk: {item}"
s_tab = "Kolom1\tKolom2"
s_translate = "aeiou"

print("## 🐍 Demonstrasi Semua Metode String Python 🐍 ##")
print("-" * 50)

# 1. capitalize(): Mengubah karakter pertama menjadi huruf besar
print(f"1. capitalize(): {'coding itu asik'.capitalize()}")

# 2. casefold(): Mengubah string menjadi huruf kecil, lebih agresif dari lower()
print(f"2. casefold():   {'GRÜSSE'.casefold()}")

# 3. center(): Mengembalikan string rata tengah dengan padding
print(f"3. center(20, '='): {'tengah'.center(20, '=')}")

# 4. count(): Menghitung jumlah kemunculan nilai tertentu
print(f"4. count('a'):   {'banana'.count('a')}")

# 5. encode(): Mengembalikan versi string yang dienkode sebagai objek bytes
print(f"5. encode():     {s.encode('utf-8')}")

# 6. endswith(): Mengembalikan True jika string diakhiri dengan nilai tertentu
print(f"6. endswith('on'): {s.endswith('on')}")

# 7. expandtabs(): Mengatur ukuran tab (\t) pada string
print(f"7. expandtabs(8): '{s_tab.expandtabs(8)}'")

# 8. find(): Mencari nilai, mengembalikan indeks pertama. Mengembalikan -1 jika tidak ada.
print(f"8. find('a'):    {s.find('a')}")

# 9. format(): Memformat nilai ke dalam placeholder string
print(f"9. format():     {s_format.format(price=15000, item='Laptop')}")

# 10. format_map(): Memformat string menggunakan dictionary
data = {'price': 20.50, 'item': 'Buku'}
print(f"10. format_map(): {s_format.format_map(data)}")

# 11. index(): Mirip find(), tapi raise ValueError jika tidak ditemukan
print(f"11. index('l'):   {s.index('l')}")

# --- Metode Pengujian Tipe (Is Methods) ---
print("\n--- Metode Pengujian (Is Methods) ---")
print(f"12. isalnum():    {s_alnum.isalnum()} ('{s_alnum}')") # Alphanumeric
print(f"13. isalpha():    {'ABC'.isalpha()}") # Alphabet
print(f"14. isascii():    {'ASCII'.isascii()}") # ASCII
print(f"15. isdecimal():  {s_num.isdecimal()}") # Decimal
print(f"16. isdigit():    {s_num.isdigit()}") # Digit
print(f"17. isidentifier(): {'var_1'.isidentifier()}") # Identifier valid
print(f"18. islower():    {'lowercase'.islower()}") # Lowercase
print(f"19. isnumeric():  {s_num.isnumeric()}") # Numeric
print(f"20. isprintable(): {'Printable!'.isprintable()}") # Printable
print(f"21. isspace():    {'  '.isspace()}") # Whitespace
print(f"22. istitle():    {'A Title Case'.istitle()}") # Title case
print(f"23. isupper():    {'UPPER'.isupper()}") # Uppercase
print("-" * 50)

# 24. join(): Menggabungkan elemen iterable (list) menjadi satu string
print(f"24. join():      {'-'.join(s_join)}")

# 25. ljust(): Mengembalikan string rata kiri dengan padding
print(f"25. ljust(15, '_'): {'kiri'.ljust(15, '_')}")

# 26. lower(): Mengubah string menjadi huruf kecil
print(f"26. lower():     {s_case.lower()}")

# 27. lstrip(): Menghilangkan spasi/karakter di sisi kiri
print(f"27. lstrip():    '{s_trim.lstrip()}'")

# 28. maketrans() & 43. translate(): Membuat tabel terjemahan dan menerapkannya
intab = "aeiou"
outtab = "12345"
trans_table = str.maketrans(intab, outtab)
print(f"28 & 43. translate(): {'Hello'.translate(trans_table)}")

# 29. partition(): Membagi string menjadi 3 tuple: (sebelum, pemisah, sesudah)
print(f"29. partition(' '): {s.partition(' ')}")

# 30. replace(): Mengganti kemunculan nilai lama dengan nilai baru
print(f"30. replace('b', 'B'): {s.replace('b', 'B')}")

# 31. rfind(): Mencari nilai dari kanan, mengembalikan indeks terakhir ditemukan. -1 jika tidak ada.
print(f"31. rfind('l'):  {s.rfind('l')}")

# 32. rindex(): Mirip rfind(), tapi raise ValueError jika tidak ditemukan
print(f"32. rindex('n'): {s.rindex('n')}")

# 33. rjust(): Mengembalikan string rata kanan dengan padding
print(f"33. rjust(15, '_'):  {'kanan'.rjust(15, '_')}")

# 34. rpartition(): Membagi string pada kemunculan terakhir pemisah
print(f"34. rpartition(' '): {s.rpartition(' ')}")

# 35. rsplit(): Membagi string menjadi list, dimulai dari kanan (rsplit(separator, maxsplit))
print(f"35. rsplit(',', 1): {s_split.rsplit(',', 1)}")

# 36. rstrip(): Menghilangkan spasi/karakter di sisi kanan
print(f"36. rstrip():    '{s_trim.rstrip()}'")

# 37. split(): Membagi string menjadi list berdasarkan pemisah
print(f"37. split(','):  {s_split.split(',')}")

# 38. splitlines(): Membagi string pada baris baru (\n)
print(f"38. splitlines(): {'line1\\nline2'.splitlines()}")

# 39. startswith(): Mengembalikan True jika string dimulai dengan nilai tertentu
print(f"39. startswith('b'): {s.startswith('b')}")

# 40. strip(): Menghilangkan spasi/karakter di kedua sisi
print(f"40. strip():     '{s_trim.strip()}'")

# 41. swapcase(): Menukar kasus (upper <-> lower)
print(f"41. swapcase():  {s_case.swapcase()}")

# 42. title(): Mengubah karakter pertama setiap kata menjadi huruf besar
print(f"42. title():     {'ini contoh judul'.title()}")

# 44. upper(): Mengubah string menjadi huruf besar
print(f"44. upper():     {s.upper()}")

# 45. zfill(): Mengisi string di sebelah kiri dengan nol (0) hingga panjang tertentu
print(f"45. zfill(10):   {'42'.zfill(10)}")

print("-" * 50)