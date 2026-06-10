from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Adsorb CO (molecule appended: C=12, O=13)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Constraints: fix bottom layer + fix C-O bond
bottom = FixAtoms(mask=[a.tag == 0 for a in slab])
co_bond = FixBondLength(12, 13)
slab.set_constraint([bottom, co_bond])

# Optimize
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Results
energy = slab.get_potential_energy()
positions = slab.get_positions()
co_dist = ((positions[12] - positions[13])**2).sum()**0.5
print(f'Final energy: {energy:.4f} eV')
print(f'C-O distance: {co_dist:.4f} Å')
