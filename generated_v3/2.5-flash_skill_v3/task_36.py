```python
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units
import numpy as np

initial_a = 4.08  # Ag의 대략적인 격자상수 (Å)
num_points = 7
variation_range = 0.05

volumes = []
energies = []

lattice_constants = np.linspace(initial_a * (1 - variation_range), initial_a * (1 + variation_range), num_points)

for a in lattice_constants:
    atoms = bulk('Ag', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    
    volume = atoms.get_volume()
    energy = atoms.get_potential_energy()
    
    volumes.append(volume)
    energies.append(energy)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = v0**(1/3)
B_GPa = B / units.GPa

print(f"평형 격자상수 (a0): {a0:.3f} Å")
print(f"
