import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell = atoms.get_cell()
volumes, energies = [], []

for s in np.linspace(0.94, 1.06, 7):
    a = atoms.copy()
    a.set_cell(cell * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f'Equilibrium volume: {v0:.4f} Å³')
print(f'Bulk modulus: {B * 160.2177:.2f} GPa')
print(f'Lattice constant: {v0**(1/3):.4f} Å')
