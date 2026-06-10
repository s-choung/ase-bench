from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0_guess = 4.09
scales = np.linspace(0.95, 1.05, 7)

volumes = []
energies = []

for s in scales:
    a = a0_guess * s
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (4.0 * v0) ** (1.0 / 3.0)
B_GPa = B / 0.006241509074460763

print(f"Equilibrium lattice constant (Angstrom): {a_eq:.6f}")
print(f"Bulk modulus (GPa): {B_GPa:.3f}")
