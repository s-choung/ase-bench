import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 11):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4 * v0) ** (1/3)

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Equilibrium volume:           {v0:.4f} Å³")
print(f"Bulk modulus:                 {B / units.kB * 1e-24:.3f} GPa")
eos.plot('Cu_eos.png')
