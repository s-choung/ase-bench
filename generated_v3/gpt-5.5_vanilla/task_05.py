import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a_guess = 3.6
scales = np.linspace(0.94, 1.06,  nine := 9)

volumes = []
energies = []

for s in scales:
    atoms = bulk("Cu", "fcc", a=a_guess * s, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

a0 = v0 ** (1 / 3)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant a0 = {a0:.6f} Angstrom")
print(f"Equilibrium volume V0 = {v0:.6f} Angstrom^3/cell")
print(f"Equilibrium volume per atom = {v0 / 4:.6f} Angstrom^3/atom")
print(f"Bulk modulus = {B:.6f} eV/Angstrom^3 = {B_GPa:.3f} GPa")
