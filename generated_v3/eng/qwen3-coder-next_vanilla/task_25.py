from ase import Atoms
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

# Initial Cu FCC unit cell
a0 = 3.6  # approximate lattice constant in Angstrom
cu = Atoms('Cu4', positions=[
    [0, 0, 0],
    [0.5*a0, 0.5*a0, 0],
    [0.5*a0, 0, 0.5*a0],
    [0, 0.5*a0, 0.5*a0]
], cell=[a0, a0, a0], pbc=True)

cu.calc = EMT()

# Print initial energy and lattice constant
print(f"Initial energy: {cu.get_potential_energy():.6f} eV")
print(f"Initial lattice constant: {cu.cell[0, 0]:.6f} Angstrom")

# Optimize with FrechetCellFilter and BFGS
cu_cell = FrechetCellFilter(cu)
opt = BFGS(cu_cell, trajectory=None)
opt.run(fmax=0.01)

# Print final energy and lattice constant
print(f"Final energy: {cu.get_potential_energy():.6f} eV")
print(f"Final lattice constant: {cu.cell[0, 0]:.6f} Angstrom")
