```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6)
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    scaled = atoms.copy()
    scaled.set_cell(atoms.get_cell() * x, scale_atoms=True)
    scaled.calc = EMT()
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0 ** (1/3)
print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Equilibrium volume: {v0:.2f} Å³")
print(f"Bulk modulus: {B * 160.21766:.2f} GPa")
