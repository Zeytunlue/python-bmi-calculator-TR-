# Kullanıcıdan aldığınız boy ve kilo değerlerine
# göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m
while True:
    boy = float(input("Lutfen boyunuzu girin(x.xx m): "))
    kilo = float(input("Lutfen kilonuzu girin(kg): "))

    vucut_kitle_indeksi = kilo / (boy * boy)
    print(f"Vucut kitle indeksiniz: {vucut_kitle_indeksi:.2f}")

    if vucut_kitle_indeksi < 18.5:
        print("Ideal kilonuzun altindasiniz.")
    elif 18.5 <= vucut_kitle_indeksi <= 24.99:
        print("Ideal kilonuzdasiniz.")
    elif 25 <= vucut_kitle_indeksi <= 29.99:
        print("Ideal kilonuzun ustundesiniz.")
    else:
        print("Obezsiniz.")

    tekrar = input("Tekrar hesaplamak ister misiniz? (Evet/Hayir): ").lower().strip()
    if tekrar != "evet":
        break

print("Gorusmek uzere!")

