import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(v0, B)
