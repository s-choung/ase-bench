from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

# Collect volumes and energies
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit EOS (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
print(f'Equilibrium volume: {v0:.3f} Å³')
print(f'Bulk modulus: {B:.1f} eV/Å³')
