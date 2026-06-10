import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

a_ref = 4.09
scales = np.linspace(0.95, 1.05, 7)

volumes = []
energies = []

for s in scales:
    a = a_ref * s
    atoms = bulk("Ag", "fcc", a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()

a0 = v0 ** (1.0 / 3.0)
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a0:.6f} Å")
print(f"Bulk modulus: {B_GPa:.6f} GPa")
