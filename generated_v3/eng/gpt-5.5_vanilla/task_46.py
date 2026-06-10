from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111("Pt", size=(3, 3, 3), vacuum=10.0)
n_slab = len(slab)

co = Atoms("CO", positions=[(0.0, 0.0, 0.0), (0.0, 0.0, 1.15)])
add_adsorbate(slab, co, height=1.85, position="ontop")

c_idx, o_idx = n_slab, n_slab + 1

zmin = min(a.position[2] for a in slab if a.symbol == "Pt")
bottom = [a.index for a in slab if a.symbol == "Pt" and a.position[2] < zmin + 0.1]

slab.set_constraint([FixAtoms(indices=bottom), FixBondLength(c_idx, o_idx)])
slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.6f} eV")
print(f"C-O distance: {slab.get_distance(c_idx, o_idx):.6f} Å")
