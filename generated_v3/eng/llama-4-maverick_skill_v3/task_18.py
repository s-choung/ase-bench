from ase import Atoms
from ase.build import molecule
from ase.geometry import get_distances

def main():
    ch4 = molecule('CH4')
    print("Atomic Coordinates:")
    print(ch4.positions)

    numbers = ch4.get_atomic_numbers()
    distances = get_distances(ch4.positions, cell=ch4.cell, pbc=ch4.pbc)[1]
    print("\nBond Lengths (Å):")
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if distances[i, j] < 2.0:  # rough estimate for bond length
                print(f"{ch4.symbols[i]}-{ch4.symbols[j]}: {distances[i, j]:.3f}")

    print(f"\nChemical Formula: {ch4.get_chemical_formula()}")

if __name__ == "__main__":
    main()
