```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

metals = ['Cu', 'Ag', 'Au']
results = []

for symbol in metals:
    # 1. Create a conventional FCC unit cell
    # An initial guess for 'a' is needed, but it will be optimized.
    atoms = bulk(symbol, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()

    # 2. Create a range of scaled structures to calculate E-V curve
    cell = atoms.get_cell()
    volumes = []
    energies = []
    for x in np.linspace(0.95, 1.05, 11):
        atoms_scaled = atoms.copy()
        atoms_scaled.set_cell(cell * x, scale_atoms=True)
        atoms_scaled.calc = EMT()
        volumes.append(atoms_scaled.get_volume())
        energies.append(atoms_scaled.get_potential_energy())

    # 3. Fit the E-V data to an equation of state
