from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0_ref = 4.09  # approximate EMT equilibrium lattice constant for Ag
a_vals = np.linspace(0.95 * a0_ref, 1.05 * a0_ref, 7)
volumes = []
energies = []
for a in a_vals:
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())
volumes = np.array(volumes)
energies = np.array(energies)
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
B_GPa = B * 160.21766208  # eV/Å³ → GPa
a_eq = (4 * v0) ** (1 / 3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
