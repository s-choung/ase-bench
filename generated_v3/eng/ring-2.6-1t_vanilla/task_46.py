from ase import Atoms
from ase.build import molecule, surface
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Pt(111) three‑layer slab
slab = surface('Pt', (111), 3, vacuum=5.0)
slab.center(vacuum=5, axis=2)          # put bottom at z≈0

# CO molecule, bond aligned along z
co = molecule('CO')
co.set_positions([[0.0, 0.0, 0.0],
                  [0.0, 0.0, 1.14]])   # ~1.14 Å bond length
# place above the slab top
top_z = slab.positions[:, 2].max()
co.translate([slab.cell[0, 0] / 2,
              slab.cell[1, 1] / 2,
              top_z + 2.0])

# combine slab and CO
atoms = slab + co
atoms.calc = EMT()

# constraints -------------------------------------------------
# 1) fix the bottom layer (z close to the minimum)
z_min = atoms.positions[:, 2].min()
bottom_idx = [i for i, p in enumerate(atoms.positions)
              if abs(p[2] - z_min) < 0.1]

# 2) fix the C–O bond length
c_idx = len(slab)          # first atom of the added CO
o_idx = len(slab) + 1      # second atom of the added CO
fix_bond = FixBondLength(c_idx, o_idx)

atoms.set_constraint([FixAtoms(indices=bottom_idx), fix_bond])

# optimisation -------------------------------------------------
dyn = BFGS(atoms)
dyn.run(fmax=0.05)

# output -------------------------------------------------------
e = atoms.get_potential_energy()
d = atoms.get_distance(c_idx, o_idx, mic=False)
print(f'Final energy = {e:.4f} eV')
print(f'C–O distance  = {d:.4f} Å')
