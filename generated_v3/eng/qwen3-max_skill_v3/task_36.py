from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Ag FCC bulk structure
atoms = bulk('Ag', 'fcc', a=4.09)
atoms.calc = EMT()

# Generate lattice constants in ±5% range
a0 = 4.09
factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

# Calculate energies for each volume
for f in factors:
    a_scaled = atoms.copy()
    a_scaled.set_cell(atoms.get_cell() * f, scale_atoms=True)
    volumes.append(a_scaled.get_volume())
    energies.append(a_scaled.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa (1 eV/Å³ = 160.21766208 GPa)
B_GPa = B * 160.21766208

# Calculate equilibrium lattice constant for FCC (V = a³/4 → a = (4V)^(1/3))
a_eq = (4 * v0) ** (1/3)

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
