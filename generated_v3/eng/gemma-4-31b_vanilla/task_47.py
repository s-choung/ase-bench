from ase.build import fcc111
from ase.lattice import FCC
from ase.neighborlist import NeighborList
from ase.calculators.emt import EMT

# Build 3x3x3 Cu FCC supercell
atoms = FCC('Cu', scale=3.61, size=(3, 3, 3))
atoms.set_calculator(EMT())

# NeighborList using natural_cutoffs (based on covalent radii)
nl = NeighborList(atoms, natural_cutoffs=True)

# Calculate coordination number for each atom
coords = [len(nl.get_neighbors(i)) for i in range(len(atoms))]
avg_coord = sum(coords) / len(coords)

print(f"Average coordination number: {avg_coord:.2f}")
