import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc')
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
a0 = v0 ** (1/3)

print(f"Lattice constant: {a0:.4f} A")
print(f"Equilibrium volume: {v0:.4f} A^3")
print(f"Bulk modulus: {B:.4f} eV/A^3")
