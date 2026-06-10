import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

a0 = 4.09
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Ag', 'fcc', a=a0*x, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (v0 * 4) ** (1/3)
B_GPa = B / units.kJ * 1e24

print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Equilibrium energy: {e0:.4f} eV")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
