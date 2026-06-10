import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Generate Ag FCC structure with reference lattice constant
ag = bulk('fcc', a=4.09, cubic=True)
ag.calc = EMT()

# Vary lattice constant ±5% over 7 points
lattice_constants = np.linspace(0.95, 1.05, 7) * 4.09
volumes = []
energies = []

for a in lattice_constants:
    ag.cell = [a, a, a]
    ag.get_potential_energy()
    volumes.append(ag.get_volume())
    energies.append(ag.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert lattice constant and bulk modulus
a0 = (v0) ** (1.0/3.0)
B_GPa = B / 1.602176634  # eV/Å³ to GPa

print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
