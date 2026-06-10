from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np
atoms = bulk('Cu', 'fcc', a=3.6)
calc = EMT()
cell = atoms.get_cell()
V, E = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms.set_cell(cell * x, scale_atoms=True)
    atoms.calc = calc
    V.append(atoms.get_volume())
    E.append(atoms.get_potential_energy())
eos = EquationOfState(V, E)
v0, e0, B = eos.fit()
print(v0, B)
