from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT

# Al(111) slab, 3 layers, 2x2 surface cell
slab = fcc111('Al', size=(2, 2, 3), vacuum=0.0)
# N2 molecule
n2 = molecule('N2')
# adsorb N2 at bridge site, 2.0 Å above the surface
add_adsorbate(slab, n2, height=2.0, position='bridge')
# add 10 Å vacuum in the z‑direction
add_vacuum(slab, 10.0)

# optional: assign a calculator (e.g., EMT) if further calculations are needed
slab.calc = EMT()

# output
symbols = slab.get_chemical_symbols()
print('Number of atoms:', len(symbols))
print('Atom types:', sorted(set(symbols)))
