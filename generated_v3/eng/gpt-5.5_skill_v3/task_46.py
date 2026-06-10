from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111("Pt", size=(3, 3, 3), vacuum=10.0)

co = Atoms("CO", positions=[(0, 0, 0), (0, 0, 1.15)])
add_adsorbate(slab, co, height=1.85, position="ontop", mol_index=0)

zmin = min(a.position[2] for a in slab if a.symbol == "Pt")
bottom_mask = [a.symbol == "Pt" and abs(a.position[2] - zmin) < 1e-3 for a in slab]

c_idx = next(i for i, a in enumerate(slab) if a.symbol == "C")
o_idx = next(i for i, a in enumerate(slab) if a.symbol == "O")

slab.set_constraint([FixAtoms(mask=bottom_mask), FixBondLength(c_idx, o_idx)])
slab.calc = EMT()

BFGS(slab, logfile=None).run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.6f} eV")
print(f"C-O distance: {slab.get_distance(c_idx, o_idx):.6f} Å")
