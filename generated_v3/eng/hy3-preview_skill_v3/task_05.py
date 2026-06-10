from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Cu FCC bulk with initial lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)

# Calculate energies for different volumes
cell = atoms.get_cell()
volumes = []
energies = []

for scale in np.linspace(0.95, 1.05, 11):
    a = atoms.copy()
    a.set_cell(cell * scale, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit Equation of State
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.2f} eV/Å³ ({B*160.2:.1f} GPa)")
