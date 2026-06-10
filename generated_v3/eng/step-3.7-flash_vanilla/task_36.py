import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import eV, Angstrom, GPa

a_vals = np.linspace(4.09 * 0.95, 4.09 * 1.05, 7)
volumes, energies = [], []
for a in a_vals:
    atoms = bulk('Ag', 'fcc', a=a, orthorhombic=True)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, _, B, _ = eos.get_equilibrium_parameters()
a0 = v0 ** (1/3)
B_GPa = B * eV / Angstrom**3 / GPa

print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Bulk modulus: {B_GPa:.1f} GPa")
