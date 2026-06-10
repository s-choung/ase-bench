from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase import Atom
from ase.io import write
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
add_adsorbate(slab, Atom('C'), height=1.85, position='ontop')
slab += Atom('O', position=slab[-1].position + np.array([0.0, 0.0, 1.15]))

z = slab.positions[:, 2]
zmin = z.min()
fixed = [i for i, zi in enumerate(z) if zi < zmin + 1.0]
slab.set_constraint([FixAtoms(indices=fixed), FixBondLength(len(slab)-2, len(slab)-1)])

slab.calc = EMT()
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(len(slab)-2, len(slab)-1)

print(f"Final energy: {energy:.6f} eV")
print(f"C-O distance: {co_dist:.6f} Å")
