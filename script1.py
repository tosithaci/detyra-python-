def lexo_objektivat():
    ditet = ["Hene", "Marte", "Merkure", "Enjte", "Premte", "Shtune", "Diel"]
    objektivat = []
    print("--- Vendos objektivat ditor (Hene–Diel) ---")
    for dita in ditet:
        while True:
            try:
                obj = int(input(f"Objektivi per {dita} (hapa): "))
                if obj >= 0:
                    objektivat.append(obj)
                    break
                else:
                    print("✘ Objektivi duhet te jet numer pozitiv.")
            except ValueError:
                print("✘ Ju lutem jepni nje numer te vlefshem.")
    return objektivat

def lexo_hapat_dhe_vlereso(objektivat):
    ditet = ["Hene", "Marte", "Merkure", "Enjte", "Premte", "Shtune", "Diel"]
    hapat = []
    arritura = total_hapa = 0
    print("--- Shkruaj hapat e realizuar (Hene–Diel) ---")
    for i, dita in enumerate(ditet):
        while True:
            try:
                hapa = int(input(f"Hapat ne {dita}: "))
                if hapa >= 0:
                    hapat.append(hapa)
                    break
                else:
                    print("✘ Hapat duhet të jenë numër pozitiv.")
            except ValueError:
                print("✘ Ju lutem jepni një numër të vlefshëm.")
        if hapa >= objektivat[i]:
            print("  ✔ Arritur")
            arritura += 1
        else:
            print(f"  ✘ Jo e arritur (mungojne {objektivat[i] - hapa} hapa)")
        total_hapa += hapa
    return hapat, arritura, total_hapa

def shfaq_raportin(objektivat, hapat, arritura, total_hapa):
    ditet = ["Hene", "Marte", "Merkure", "Enjte", "Premte", "Shtune", "Diel"]
    total_obj = sum(objektivat)
    print("\n--- RAPORTI JAVOR ---")
    print("Dita          Objektivi   Realizimi    Statusi")
    print("----------------------------------------------")
    for i in range(7):
        status = "✔" if hapat[i] >= objektivat[i] else "✘"
        print(f"{ditet[i]:<14}{objektivat[i]:<12}{hapat[i]:<13}{status}")
    print("----------------------------------------------")
    print(f"Objective achieved: {arritura}/7 dite")
    print(f"Total steps taken / Total objective: {total_hapa} / {total_obj}")
    print(f"Perqindja ndaj objektivit javor: {(total_hapa / total_obj) * 100:.2f}%\n" if total_obj else "Perqindja: 0%\n")

while True:
    objektivat = lexo_objektivat()
    hapat, arritura, total_hapa = lexo_hapat_dhe_vlereso(objektivat)
    while True:
        print("====== MENU ======")
        print("1) Shfaq raportin javor\n2) Ndrysho objektivat\n3) Dil")
        zgjedhja = input("Zgjidh (1-3): ")
        match zgjedhja:
            case "1": shfaq_raportin(objektivat, hapat, arritura, total_hapa)
            case "2": break
            case "3": print("Programi u mbyll. 👋"); exit()
            case _: print("✘ Zgjedhje e pavlefshme. Provo përsëri.")