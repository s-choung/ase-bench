import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState

# Create initial FCC Cu structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Optimize structure first (cell + positions)
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Get optimized cell
cell = atoms.get_cell()

# Collect data for EOS fitting
volumes, energies = [], []
for x in np.linspace(0.90, 1.10, 11):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit EOS (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus from eV/Å³ to GPa
# 1 eV/Å³ = 160.21766208 GPa
B_GPa = B * 160.21766208

# Calculate equilibrium lattice constant
# For FCC: volume = a³/4 → a = (4V)^(1/3)
a_eq = (4 * v0) ** (1/3)

print(f"Equilibrium volume: {v0:.4f} Å³")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
