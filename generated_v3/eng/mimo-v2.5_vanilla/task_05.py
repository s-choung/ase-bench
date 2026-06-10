import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create Cu FCC unit cell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Volumes to test (±10% of initial)
volumes = np.linspace(0.9, 1.1, 15) * atoms.get_volume()
energies = []

# Calculate energy for each volume
for vol in volumes:
    scaled = atoms.copy()
    scaled.set_cell(scaled.cell * (vol / scaled.get_volume())**(1/3), scale_atoms=True)
    energies.append(scaled.get_potential_energy())

# Fit equation of state
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.2f} Å³")
print(f"Bulk modulus: {B:.2f} eV/Å³")
