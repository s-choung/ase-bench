from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
import numpy as np

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab.set_constraint(FixAtoms(indices=[atom.index for atom in slab if atom.tag > 1]))
oh = molecule('OH')
oh.rotate(180, 'x')

positions = ['ontop', 'bridge', 'fcc']
systems = []
for pos in positions:
    atoms = slab.copy()
    add_adsorbate(atoms, oh.copy(), height=1.8, position=pos)
    atoms.calc = EMT()
    systems.append((pos, atoms))

energies = []
for pos, atoms in systems:
    energies.append((pos, atoms.get_potential_energy()))

energies.sort(key=lambda x: x[1])
print("Adsorption energies (eV):")
for pos, e in energies:
    print(f"{pos:10s}: {e:.6f}")
print(f"\nMost stable site: {energies[0][0]}")
