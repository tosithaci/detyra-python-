def lexo_objektivat():
    ditet = ["Hene", "Marte", "Merkure", "Enjte", "Premte", "Shtune", "Diel"]
    obj_hene = obj_marte = obj_merkure = obj_enjte = obj_premte = obj_shtune = obj_diel = 0

    print("--- Vendos objektivat ditor (Hene–Diel) ---")
    for dita in ditet:
        while True:
            try:
                objektivi = int(input(f"Objektivi per {dita} (hapa): "))
                if objektivi < 0:
                    print("✘ Objektivi duhet te jet numer pozitiv.")
                else:
                    break
            except ValueError:
                print("✘ Ju lutem jepni nje numer te vlefshem.")
        if dita == "Hene": obj_hene = objektivi
        elif dita == "Marte": obj_marte = objektivi
        elif dita == "Merkure": obj_merkure = objektivi
        elif dita == "Enjte": obj_enjte = objektivi
        elif dita == "Premte": obj_premte = objektivi
        elif dita == "Shtune": obj_shtune = objektivi
        elif dita == "Diel": obj_diel = objektivi

    return obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel

def lexo_hapat_dhe_vlereso(obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel):
    ditet = ["Hene", "Marte", "Merkure", "Enjte", "Premte", "Shtune", "Diel"]
    objektivat = [obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel]
    hap_hene = hap_marte = hap_merkure = hap_enjte = hap_premte = hap_shtune = hap_diel = 0
    arritura = 0
    total_hapa = 0
    total_obj = sum(objektivat)

    print("--- Shkruaj hapat e realizuar (Hene–Diel) ---")
    for i in range(7):
        dita = ditet[i]
        objektivi = objektivat[i]
        while True:
            try:
                hapa = int(input(f"Hapat ne {dita}: "))
                if hapa < 0:
                    print("✘ Hapat duhet të jenë numër pozitiv.")
                else:
                    break
            except ValueError:
                print("✘ Ju lutem jepni një numër të vlefshëm.")
        if dita == "Hene": hap_hene = hapa
        elif dita == "Marte": hap_marte = hapa
        elif dita == "Merkure": hap_merkure = hapa
        elif dita == "Enjte": hap_enjte = hapa
        elif dita == "Premte": hap_premte = hapa
        elif dita == "Shtune": hap_shtune = hapa
        elif dita == "Diel": hap_diel = hapa

        if hapa >= objektivi:
            print("  ✔ Arritur")
            arritura += 1
        else:
            print(f"  ✘ Jo e arritur (mungojne {objektivi - hapa} hapa)")
        total_hapa += hapa

    return hap_hene, hap_marte, hap_merkure, hap_enjte, hap_premte, hap_shtune, hap_diel, arritura, total_hapa, total_obj


def shfaq_raportin(objektivat, hapat, arritura, total_hapa, total_obj):
    ditet = ["Hene", "Marte", "Merkure", "Enjte", "Premte", "Shtune", "Diel"]
    print("\n--- RAPORTI JAVOR ---")
    print("Dita          Objektivi   Realizimi    Statusi")
    print("----------------------------------------------")
    for i in range(7):
        status = "✔" if hapat[i] >= objektivat[i] else "✘"
        print(f"{ditet[i]:<14}{objektivat[i]:<12}{hapat[i]:<13}{status}")
    print("----------------------------------------------")
    print(f"Objective achieved: {arritura}/7 dite")
    print(f"Total steps taken / Total objective: {total_hapa} / {total_obj}")
    perqindja = (total_hapa / total_obj) * 100 if total_obj > 0 else 0
    print(f"Perqindja ndaj objektivit javor: {perqindja:.2f}%\n")


while True:
    obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel = lexo_objektivat()
    hap_hene, hap_marte, hap_merkure, hap_enjte, hap_premte, hap_shtune, hap_diel, arritura, total_hapa, total_obj = lexo_hapat_dhe_vlereso(
        obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel)

    while True:
        print("====== MENU ======")
        print("1) Shfaq raportin javor")
        print("2) Ndrysho objektivat dhe rifillo Hapin 2")
        print("3) Dil")
        zgjedhja = input("Zgjidh (1-3): ")

        match zgjedhja:
            case "1":
                objektivat = [obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel]
                hapat = [hap_hene, hap_marte, hap_merkure, hap_enjte, hap_premte, hap_shtune, hap_diel]
                shfaq_raportin(objektivat, hapat, arritura, total_hapa, total_obj)
            case "2":
                break 
            case "3":
                print("Programi u mbyll. 👋")
                exit()
            case _:
                print("✘ Zgjedhje e pavlefshme. Provo përsëri.")
