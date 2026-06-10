from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

slab.set_constraint([
    FixAtoms(mask=[a.tag >= 2 for a in slab]),
    FixBondLength(slab.index(co[0]), slab.index(co[1]))
])

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

e = slab.get_potential_energy()
d = slab.get_distance(slab.index(co[0]), slab.index(co[1]))

print(f"Final energy: {e:.3f} eV")
print(f"C-O distance: {d:.3f} Å")
