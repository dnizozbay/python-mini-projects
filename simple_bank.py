balance = 10000 
history = []
pin = "1234"
access_granted = False
for attempt in range (1,4):
    attempted_pin = input("PIN giriniz: ")
    if attempted_pin == pin:
        print("Giriş yaptınız.")
        access_granted = True
        break
    else:
        print(f"PIN yanlış. Kalan deneme: {3 - attempt}")
if access_granted:
    print("Menü:")
    while True:
        print("1 - Bakiye göster")
        print("2 - Para yatır")
        print("3 - Para çek")
        print("4 - Çıkış")
        print("5 - İşlem geçmişi")

        choice = input("Seçim: ")
        if choice == "1":
            print(f"Bakiyeniz: {balance} TL")
        elif choice == "2":
            added = int(input("Yatıracağınız miktarı giriniz: "))
            if added <= 0:
                print("Geçersiz miktar, yeniden deneyin.")
            else:
                balance += added
                print(f"Yeni bakiyeniz: {balance} TL")
                history.append(f"+{added} TL | Bakiye: {balance} TL")
        elif choice == "3":
            reduced = int(input("Çekeceğiniz miktarı giriniz: "))
            if reduced <= 0:
                print("Geçersiz miktar, yeniden deneyin.")
            elif reduced <= balance:
                balance -= reduced
                print(f"İşlem başarılı! Mevcut bakiye: {balance} TL")
                history.append(f"-{reduced} TL | Bakiye: {balance} TL")
            else:
                print("Bakiye yetersiz!")
        elif choice == "4":
            print("Çıkış yaptınız.")
            break
        elif choice == "5":
            if len(history) == 0:
                print("Henüz işlem yok.")
            else:
                for transaction in history:
                    print(transaction)
        else:
            print("Geçersiz işlem numarası.")
else:
    print("3 yanlış giriş. Oturum sonlandı.")


