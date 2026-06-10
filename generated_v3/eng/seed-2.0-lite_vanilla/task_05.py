import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Generate range of lattice constants around initial guess
lattice_constants = np.linspace(3.4, 3.8, 15)
volumes = []
energies = []

for a in lattice_constants:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# Fit Equation of State
eos = EquationOfState(volumes, energies)
v0, _, B = eos.fit()

# Output results
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.2f} GPa")
