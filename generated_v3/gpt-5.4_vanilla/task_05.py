from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 3.6
scales = np.linspace(0.94, 1.06, 9)

volumes = []
energies = []

for s in scales:
    atoms = bulk('Cu', 'fcc', a=a0 * s)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

a_eq = (4 * v0) ** (1 / 3)
B_GPa = B / 1e9 * 1.602176634e-19 / 1e-30

print(f"Equilibrium lattice constant a0 = {a_eq:.6f} Å")
print(f"Equilibrium volume V0 = {v0:.6f} Å^3")
print(f"Bulk modulus B = {B_GPa:.3f} GPa")
