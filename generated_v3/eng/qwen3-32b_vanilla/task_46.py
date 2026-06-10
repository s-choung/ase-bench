from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=4.0)
slab.calc = EMT()

co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.1)])
add_adsorbate(slab, co, height=1.5, position=(0, 0))

c_index = len(slab) - 2
o_index = len(slab) - 1

fixed = FixAtoms(indices=[i for i, t in enumerate(slab.get_tags()) if t == 0])
slab.set_constraints([fixed, FixBondLength(c_index, o_index)])

BFGS(slab).run(fmax=0.05)

print(f'Final energy: {slab.get_potential_energy():.3f} eV')
print(f'C-O distance: {slab.get_distance(c_index, o_index):.3f} Å')
