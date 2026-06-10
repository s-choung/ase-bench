from ase import Atoms, io
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# -------------- initial configuration -----------------
cell = (4.0, 4.0, 20.0)          # a0, b0, c0 (fits a 4‑atom unit cell)
# positions: x, y in [0,4), z in [0,2.0)
init_pos = [
    [0.0, 0.0, 0.0],
    [1.732/2.0, 0.0, 0.0],      # Cu(111) nearest‑neighbor offset
    [0.0, 1.732/2.0, 0.0],
    [1.732/2.0, 1.732/2.0, 0.0]
]
atoms = Atoms('Cu4', positions=init_pos, cell=cell, pbc=[1,1,0])
atoms.set_cell(cell, scale_atoms=True)

em = EMT()
atoms.set_calculator(em)

# tags for atoms that must stay fixed (bottom two layers)
for i, fixed in enumerate(atoms):
    if i < 2:
        atoms.constraints = FixAtoms(tag=1)

# -------------- BFGS optimization --------------------
optimizer = BFGS(atoms, trajectory="cu111_opt.traj")
optimizer.run(fmax=0.05)          # inhibit motion of fixed atoms

# -------------- verify fixed atoms ------------------
print("Fixed atoms before:")
for i in range(4):
    if len(atoms.constraints.atoms) == 1 and i in atoms.constraints.atoms:
        print(f"  atom {i}: {init_pos[i]}")
print("\nFixed atoms after:")
for i in range(4):
    if len(atoms.constraints.atoms) == 1 and i in atoms.constraints.atoms:
        print(f"  atom {i}: {atoms.get_positions()[i]}")

# optional sanity check
before = np.array([atoms.get_initial_positions()[i]] * atoms.constraints.nfix
                  if len(atoms.constraints.atoms) == 1 else init_pos[:atoms.constraints.nfix])
after  = atoms.get_positions()[atoms.constraints.atoms] if atoms.constraints else atoms.get_positions()[:4]
print("\nDifference (should be zero within 1e‑6):")
print(np.linalg.norm(before - after))
