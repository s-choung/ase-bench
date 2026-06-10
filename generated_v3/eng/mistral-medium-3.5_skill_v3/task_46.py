from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
slab.set_constraint([FixAtoms(mask=[a.tag == 1 for a in slab]), FixBondLength(0, 1)])
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
print(f"Energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(0, 1):.4f} Å")
