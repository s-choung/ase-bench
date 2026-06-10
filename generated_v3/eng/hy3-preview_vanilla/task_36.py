import numpy as np
from ase.io import read
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import BirchMurnaghan

# Create Ag FCC bulk
ag = bulk('Ag', 'fcc', a=4.09, cubic=True)

# Set calculator
ag.calc = EMT()

# Generate lattice constants (±5% range, 7 points)
a0 = 4.09
lattice_constants = np.linspace(a0*0.95, a0*1.05, 7)

# Calculate energies
energies = []
volumes = []

for a in lattice_constants:
    ag = bulk('Ag', 'fcc', a=a, cubic=True)
    ag.calc = EMT()
    energies.append(ag.get_potential_energy())
    volumes.append(ag.get_volume())

# Fit Birch-Murnaghan EOS
eos = BirchMurnaghan(volumes, energies)
v0, e0, B0, B0p = eos.fit()

# Convert bulk modulus to GPa (ASE returns in eV/Å³)
B0_GPa = B0 * 160.21766208  # eV/Å³ to GPa

# Calculate equilibrium lattice constant from equilibrium volume
# For FCC, volume = a³ for conventional cell (4 atoms)
a_eq = v0**(1/3)

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B0_GPa:.2f} GPa")
