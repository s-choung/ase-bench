from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# 3‑layer Al(111) slab with 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# N₂ molecule
n2 = molecule('N2')

# Bridge site: halfway along the first surface lattice vector
bridge_x = slab.get_cell()[0][0] / 2.0
add_adsorbate(slab, n2, height=2.0, position=(bridge_x, 0.0))

# Simple calculator (optional)
slab.set_calculator(EMT())

print('Number of atoms:', len(slab))
print('Atom types:', sorted(set(slab.get_chemical_symbols())))
