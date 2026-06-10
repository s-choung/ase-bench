import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# Create Ag FCC bulk with initial lattice constant
a0 = 4.09  # Initial guess for Ag lattice constant (Å)
ag = bulk('Ag', 'fcc', a=a0, cubic=True)

# Set calculator
ag.calc = EMT()

# Vary lattice constant by ±5% (7 points)
scale_factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for s in scale_factors:
    ag_scaled = ag.copy()
    ag_scaled.set_cell(ag.cell * s, scale_atoms=True)
    volumes.append(ag_scaled.get_volume())
    energies.append(ag_scaled.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()  # v0: Å³, e0: eV, B: eV/Å³

# Calculate equilibrium lattice constant from equilibrium volume
# For FCC, conventional cell volume V = a³ (4 atoms)
a_eq = v0**(1/3)

# Convert bulk modulus from eV/Å³ to GPa (1 eV/Å³ = 160.21766 GPa)
B_GPa = B * 160.21766

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
