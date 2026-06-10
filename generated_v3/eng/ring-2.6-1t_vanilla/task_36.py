import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09                     # initial lattice constant (Å)
strains = np.linspace(-0.05, 0.05, 7)
volumes, energies = [], []

for s in strains:
    a = a0 * (1 + s)
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies, 'birchmurnaghan')
v_eq, e_eq, B = eos.fit()          # B in eV/Å³
a_eq = v_eq ** (1/3)
B_GPa = B * 160.21766208           # convert to GPa

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
