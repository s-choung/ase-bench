import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a_ref = bulk('Ag', 'fcc', cubic=True).cell[0, 0]
volumes, energies = [], []

for a in np.linspace(0.95, 1.05, 7) * a_ref:
    atoms = bulk('Ag', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B0 = eos.fit()

print(f"Equilibrium lattice constant: {v0**(1/3):.4f} Å")
print(f"Bulk modulus: {B0 * 160.21766208:.2f} GPa")
