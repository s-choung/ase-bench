from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

c_idx = len(slab) - 2
o_idx = len(slab) - 1

slab.set_constraint([
    FixAtoms(mask=slab.get_tags() == 1),
    FixBondLength(c_idx, o_idx)
])

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.3f} eV")
print(f"C-O distance: {slab.get_distance(c_idx, o_idx):.3f} Angstrom")
