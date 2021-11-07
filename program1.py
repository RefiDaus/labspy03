print ("PROGRAM PUTHON MENGHITUNG NILAI TERKECIL & TERBESAR SERTA RATA-RATA")
n = int(input("\nmasukan jumlah laba = "))
bil = []
tot = 0
for x in range(n):
    m=x+1
    a = int(input("bilangan ke %d = "%m))
    bil.append (a)
    tot += bil [x]
    rata2 = tot / n

print("\nbilangan terkecil : %d" %min(bil))
print("bilangan terbesar : %d" %max(bil))
print("nilai rata-rata : %0.2f" %rata2)