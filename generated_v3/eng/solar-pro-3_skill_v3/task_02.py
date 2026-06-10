from ase.build import fcc111
from ase.atom import Atom
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.data import atomic_numbers

# 1. Build a 4‑layer Pt(111) slab, 2×2 cell, vacuum 10 Å
atoms = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# 2. Split Pt lattice, add CO adsorbate on‑top
pt_atoms, co_atoms = atoms.split()
co = Atom('C', pt_atoms[0].position + [0, 0, 1.8] * units.Ang)
atoms = atoms + co

print(f"Total atoms before fixing: {len(atoms)}")

# Tag atoms belonging to the substrate so they are not fixed later
for i, atom in enumerate(atoms):
    atom.tag = 1 if atom.symbol == 'Pt' and atomic_numbers['Pt'] == i+1 else 0
print(f"Pt atoms tag = {np.array([a.tag for a in atoms if a.symbol == 'Pt'])[0]}")
