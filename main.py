import os


def insertion_sort(arr: list[int]) -> list[int]:
    """Sorteaza lista crescator folosind Insertion Sort."""
    rezultat = arr.copy()
    for i in range(1, len(rezultat)):
        cheie = rezultat[i]
        j = i - 1
        while j >= 0 and rezultat[j] > cheie:
            rezultat[j + 1] = rezultat[j]
            j -= 1
        rezultat[j + 1] = cheie
    return rezultat


def merge_sort(arr: list[int]) -> list[int]:
    """Sorteaza lista crescator folosind Merge Sort."""
    if len(arr) <= 1:
        return arr.copy()

    mijloc = len(arr) // 2
    stanga = merge_sort(arr[:mijloc])
    dreapta = merge_sort(arr[mijloc:])

    return _interclasare(stanga, dreapta)


def _interclasare(stanga: list[int], dreapta: list[int]) -> list[int]:
    rezultat = []
    i = j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])
    return rezultat


def main():
    nume_fisier = "date.txt"

    # 1. Verificare existenta fisier
    if not os.path.exists(nume_fisier):
        print(f"Eroare: Fisierul '{nume_fisier}' nu exista.")
        return

    with open(nume_fisier, "r", encoding="utf-8") as f:
        linii = f.read().splitlines()

    # 2. Verificare numar minim de linii
    if len(linii) < 2:
        print("Eroare: Fisierul trebuie sa contina cel putin 2 linii (numerele si algoritmul).")
        return

    linie_numere = linii[0].strip()
    algoritm = linii[1].strip()

    if not linie_numere:
        print("Eroare: Prima linie (lista de numere) este goala.")
        return

    # 3. Validare numere intregi
    try:
        numere = [int(x) for x in linie_numere.split()]
    except ValueError:
        print("Eroare: Prima linie trebuie sa contina doar numere intregi separate prin spatii.")
        return

    # 4. Selectare si validare algoritm
    algoritmi_disponibili = {
        "Insertion": insertion_sort,
        "Merge": merge_sort,
    }

    if algoritm not in algoritmi_disponibili:
        print(
            f"Eroare: Algoritmul '{algoritm}' nu este suportat. "
            f"Alegeti dintre: {', '.join(algoritmi_disponibili.keys())}."
        )
        return

    # 5. Executie sortare si scriere in acelasi fisier pastrand datele initiale
    numere_sortate = algoritmi_disponibili[algoritm](numere)
    linie_rezultat = f"{algoritm}: {' '.join(map(str, numere_sortate))}"

    continut_actualizat = f"{linii[0]}\n{linii[1]}\n{linie_rezultat}\n"
    with open(nume_fisier, "w", encoding="utf-8") as f:
        f.write(continut_actualizat)

    print(f"Sortare realizata cu succes! Rezultat scris in '{nume_fisier}': {linie_rezultat}")


if __name__ == "__main__":
    main()