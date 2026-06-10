from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.units import Å

# Surface setup
slab = fcc111('Pt', size=(3,3,3), vacuum=10)
co = molecule('CO', vacuum=3)
add_adsorbate(slab, co, 1.8, 'ontop')

# Constraints
slab.set_constraint([
    FixAtoms(mask=[a.z < 3.5 for a in slab]),
    FixBondLength(slab.positions[-2], slab.positions[-1])
])

# Run EMT optimization
slab.calc = EMT()
dyn = BFGS(slab); dyn.run(fmax=0.05)

# Results
print("Final energy: {:.3f} eV".format(slab.get_potential_energy()))
print("C-O distance: {:.2f} Å".format(co.get_distance(-1, -2, mic=True)))
