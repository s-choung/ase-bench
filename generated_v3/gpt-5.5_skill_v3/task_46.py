from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111("Pt", size=(2, 2, 3), vacuum=10.0)
co = Atoms("CO", positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.15]])

add_adsorbate(slab, co, height=1.8, position="ontop")

c_idx = len(slab) - 2
o_idx = len(slab) - 1

fix_bottom = FixAtoms(mask=[atom.tag == 3 for atom in slab])
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bottom, fix_co])

slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

print("Final energy (eV):", slab.get_potential_energy())
print("C-O distance (A):", slab.get_distance(c_idx, o_idx))
