from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0s = [3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
energies = []

for a0 in a0s:
    atoms = fcc111('Cu', size=(2, 2, 2), latticeconstant=a0)
    calc = EMT()
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    energies.append(energy)

volumes = [a0**3 for a0 in a0s]
eos = EquationOfState(volumes, energies)
v0, k, _ = eos.fit()
print(f"Equilibrium volume: {v0:.6f} Angstrom^3")
print(f"Bulk modulus: {k:.2f} eV/Angstrom^3")
