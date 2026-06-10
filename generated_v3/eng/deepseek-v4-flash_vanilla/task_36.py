import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09  # initial guess for Ag lattice constant in Angstrom
percent = 0.05
a_list = np.linspace(a0*(1-percent), a0*(1+percent), 7)

volumes = []
energies = []

for a in a_list:
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(energy)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, B, Bp, E0 = eos.fit()
B_GPa = B * 160.21766208  # convert eV/A^3 to GPa
a_eq = v0**(1/3)  # for conventional cubic cell, volume = a^3

print(f"Equilibrium lattice constant: {a_eq:.4f} Angstrom")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
