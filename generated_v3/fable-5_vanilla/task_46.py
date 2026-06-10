from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.15)])
add_adsorbate(slab, co, height=2.0, position='ontop')

n_slab = 12
c_idx, o_idx = n_slab, n_slab + 1

bottom_layer = [a.index for a in slab if a.tag == 3]
constraints = [FixAtoms(indices=bottom_layer), FixBondLength(c_idx, o_idx)]
slab.set_constraint(constraints)

slab.calc = EMT()
opt = BFGS(slab, logfile='-')
opt.run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(c_idx, o_idx):.4f} A")
