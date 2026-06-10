from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create initial Cu FCC structure
a0 = 3.6  # initial guess
atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()

# Generate volumes and energies
volumes = []
energies = []
cell = atoms.get_cell()
for x in np.linspace(0.95, 1.05, 7):
    scaled_atoms = atoms.copy()
    scaled_atoms.set_cell(cell * x, scale_atoms=True)
    volumes.append(scaled_atoms.get_volume())
    energies.append(scaled_atoms.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium volume: {v0:.4f} Å³")
print(f"Bulk modulus: {B:.4f} eV/Å³")
