from ase.build import molecule
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = molecule("CH4")

print("Atomic coordinates (Angstrom):")
for i, atom in enumerate(atoms):
    x, y, z = atom.position
    print(f"{i:2d} {atom.symbol:2s} {x:12.6f} {y:12.6f} {z:12.6f}")

print("\nBond lengths (Angstrom):")
cutoffs = natural_cutoffs(atoms, mult=1.2)
nl = NeighborList(cutoffs, self_interaction=False, bothways=False)
nl.update(atoms)

for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    for j, offset in zip(indices, offsets):
        d = atoms.get_distance(i, j, mic=True)
        print(f"{atoms[i].symbol}{i}-{atoms[j].symbol}{j}: {d:.6f}")

print("\nChemical formula:")
print(atoms.get_chemical_formula())
