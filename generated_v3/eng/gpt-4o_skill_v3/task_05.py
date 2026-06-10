from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import ExpCellFilter
import numpy as np
from ase.eos import EquationOfState

# Create Copper FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Optimize structure
BFGS(ExpCellFilter(atoms)).run(fmax=0.01)

# Collect volumes and energies by varying lattice constant
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# EOS fitting
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Output results
print(f"Equilibrium volume: {v0:.2f} Å³")
print(f"Bulk modulus: {B:.2f} GPa")
