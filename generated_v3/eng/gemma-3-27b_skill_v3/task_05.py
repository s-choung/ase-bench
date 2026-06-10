from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0s = np.linspace(3.4, 3.8, 7)
volumes = []
energies = []

for a0 in a0s:
    atoms = bulk('Cu', 'fcc', a=a0)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(energy)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0_eq = v0**(1/3)

print(f"Equilibrium Volume: {v0:.6f} Angstrom^3")
print(f"Bulk Modulus: {B:.2f} GPa")
print(f"Equilibrium lattice constant: {a0_eq:.3f} Angstrom")
