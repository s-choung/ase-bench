from ase.build import bulk
from ase.calculators.emt import EMT
from ase.utils.eos import EquationOfState
import numpy as np

# Set up Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# Define volume range
volumes = [cu.get_volume() * (1 - 0.05*i) for i in range(11)]
energies = []

# Calculate energies for different volumes
for vol in volumes:
    cu.set_cell(vol ** (1/3) * cu.get_cell(), scale_atoms=True)
    energies.append(cu.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# Print results
print(f'Equilibrium volume: {v0:.4f} Å^3')
print(f'Bulk modulus: {B:.2f} eV/Å^3')
