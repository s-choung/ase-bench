import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create bulk Cu with initial lattice parameter
a0 = 3.6  # initial guess in Angstrom
atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()

# Generate volumes by scaling the unit cell
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 9):
    a_scaled = a0 * x
    a = bulk('Cu', 'fcc', a=a_scaled)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results (convert B to GPa)
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B / 160.21766208:.3f} GPa")
