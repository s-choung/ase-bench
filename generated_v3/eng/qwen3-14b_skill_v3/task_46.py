from ase.build import fcc111, add_adsorbate, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

bottom_mask = [i < 4 for i in range(len(slab))]
slab.set_constraint([FixAtoms(mask=bottom_mask), FixBondLength(slab[-2], slab[-1])])

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
distance = slab.get_distance(-2, -1)
print(f"Final energy: {energy:.4f} eV")
print(f"C-O distance: {distance:.4f} Å")
