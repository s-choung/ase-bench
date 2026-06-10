import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

a_values = np.linspace(3.45, 3.75, 11)
volumes, energies = [], []

for a in a_values:
    atoms = bulk("Cu", "fcc", a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

print(f"Equilibrium lattice constant: {a0:.6f} Å")
print(f"Equilibrium volume: {v0:.6f} Å^3/atom")
print(f"Bulk modulus: {B / kJ * 1.0e24:.6f} GPa")
