from ase import Atoms
from ase.eos import EquationOfState
import numpy as np

# Create FCC copper system
atoms = Atoms('Cu', 'fcc', a=3.6, pbc=True)
cell = atoms.get_cell()
volumes = []
energies = []

# Perform EOS fitting
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium volume (Å³): {v0/1000:.3f}")
print(f"Bulk modulus (GPa): {B/100:.3f}")
