import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
a0 = 4.09
scales = np.linspace(0.95, 1.05, 7)
vols, energies = [], []
for s in scales:
    atoms = bulk('Ag', 'fcc', a=a0*s)
    atoms.calc = EMT()
    vols.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(vols, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0**(1/3)
B_GPa = B * 160.21766208
print(a_eq, B_GPa)
