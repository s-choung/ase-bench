from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.geometry import get_distances

# Setup H2 molecule
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])
atoms.calc = EMT()

def report(label, atoms):
    d = get_distances(atoms.positions, atoms.positions, mic=True)[0, 1]
    e = atoms.get_potential_energy()
    print(f"{label} -> Bond Length: {d:.4f} Å, Energy: {e:.4f} eV")

# Before constraint
report("Before", atoms)

# Apply constraint (fix bond between atom 0 and 1 at 0.9 A)
atoms.set_constraint(FixBondLength(0, 1, 0.9))

# Since constraints don't change geometry, we must relax to see the effect
from ase.optimize import BFGS
opt = BFGS(atoms)
opt.run(fmax=1e-5)

# After constraint
report("After ", atoms)
