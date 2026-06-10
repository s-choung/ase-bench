from ase.io import read
from ase.build import molecule
from ase.calculators import EMT
from ase.visualize import view

def analyze_methane():
    methane = read("g2/CH4.g2")
    print("Atomic Coordinates:")
    print(methane.get_positions())

    bond_lengths = []
    for atom1 in range(len(methane)):
        for atom2 in range(atom1 + 1, len(methane)):
            distance = methane.get_distance(atom1, atom2)
            if distance < 1.6:
                bond_lengths.append(distance)
    print("\nBond Lengths (approximate):")
    print(bond_lengths)

    print("\nChemical Formula:")
    print(methane.chemical)

if __name__ == "__main__":
    analyze_methane()
