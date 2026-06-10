from ase.build import molecule
from ase.data import chemical_symbols
from ase.neighborlist import NeighborList

# Retrieve CH4 from G2 database
atoms = molecule('CH4')

# Print atomic coordinates
print("Atomic coordinates:")
for atom in atoms:
    print(f"{chemical_symbols[atom.number]}: {atom.position[:]}")  # [:] to convert FixedArray to list

# Calculate and print bond lengths
nl = NeighborList([1.2] * len(atoms), self_interaction=False)  # Cutoff ~1.2Å for C-H
nl.update(atoms)

print("\nBond lengths:")
bonds = []
for i in range(len(atoms)):
    for j in nl.get_neighbors(i)[0]:
        if i < j:  # Avoid duplicate pairs
            bond_length = atoms.get_distance(i, j)
            bonds.append((i, j, bond_length))
            print(f"{chemical_symbols[atoms[i].number]}-{chemical_symbols[atoms[j].number]}: {bond_length:.3f} Å")

# Print chemical formula
from ase.utils.formula import ChemicalFormula
formula = ChemicalFormula(atoms.get_chemical_formula())
print("\nChemical formula:", formula.format('hill'))
