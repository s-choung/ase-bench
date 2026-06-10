from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import sys

# 4‑layer Cu(111) slab, vacuum above the surface
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 4)   # 2×2 unit cells, 4 layers in c
fcc111(atoms, layers=4, vacuum=10.0)                       # set correct slab geometry
atoms.set_pbc(True)                                        # periodic in xy

# EMT calculator
atoms.calc = EMT()

# ---- tag the bottom 2 layers (z = -half vacuum / 2) ----
slab_height = atoms.cell[2] / 2.0 / 4.0
zlim_low = -slab_height + 1.2
zlim_high = -slab_height - 0.8                 # a small margin for padding
mask = [a.z < zlim_low for a in atoms]

# tag atoms in selected layers and obtain a list of fixed indices
fc = FixAtoms(mask=mask)
atoms.set_constraint(fc)                     # constraint vs FixAtoms is fine

# ---- positions before optimization ----
coord_before = [a.get_array('xyz')[0].copy() for a in atoms if mask[a.tag]]
# build a simple comparison string
fixed_str = ", ".join([f"{a.tag}:{arr.item():.6f}" for a, arr in zip(atoms, coord_before)])
print("Fixed atoms (tags 0‑9) before optimization:", fixed_str)
print("Positions stored in 'xyz' property; check if they change outside")

# BFGS relaxation (cell + positions using FrechetCellFilter)
from ase.filters import FrechetCellFilter
opt = BFGS(FrechetCellFilter(atoms))         # optimizer that respects bulk‑like cell changes
opt.run(fmax=0.05)                           # force convergence, max steps = 1000

# ---- coordinates after optimization ----
coord_after = [a.get_array('xyz')[0].copy() for a in atoms if mask[a.tag]]
after_str = ", ".join([f"{a.tag}:{arr.item():.6f}" for a, arr in zip(atoms, coord_after)])
print("Fixed atoms after optimization:        ", after_str)

# Direct visual check (use ASE view if script is run interactively)
# from ase.visualize import view
# if sys.flags.interactive:
#     view(atoms, show=False)
