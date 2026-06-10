import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a_values = np.linspace(3.45, 3.75, 9)
volumes, energies = [], []

for a in a_values:
    atoms = bulk("Cu", "fcc", a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()

a0 = v0 ** (1 / 3)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant: {a0:.6f} Å")
print(f"Equilibrium volume: {v0:.6f} Å^3")
print(f"Bulk modulus: {B_GPa:.3f} GPa")
