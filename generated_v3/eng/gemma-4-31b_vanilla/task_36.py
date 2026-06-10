import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Setup system
symbol = 'Ag'
a_init = 4.089  # Initial guess for Ag lattice constant
lattice_constants = np.linspace(a_init * 0.95, a_init * 1.05, 7)
energies = []
volumes = []

for a in lattice_constants:
    atoms = bulk(symbol, 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies)
v0, e0, b0 = eos.fit()

# Convert volume back to lattice constant for FCC
a0 = (v0)**(1/3)
# Convert Bulk Modulus from eV/Ang^3 to GPa
# 1 eV/Ang^3 = 160.21766 GPa
b0_gpa = b0 * 160.21766

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {b0_gpa:.2f} GPa")
