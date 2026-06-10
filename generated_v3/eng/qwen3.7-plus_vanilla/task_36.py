import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a_guess = 4.05
a_vals = np.linspace(0.95 * a_guess, 1.05 * a_guess, 7)

volumes, energies = [], []
for a in a_vals:
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = v0 ** (1 / 3)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant: {a_eq:.4f} A")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
