from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Ag FCC bulk with initial lattice constant
initial_a = 4.09  # Approximate equilibrium for Ag
atoms = bulk('Ag', 'fcc', a=initial_a)

# Calculate energies for different lattice constants
volumes = []
energies = []

for scale in np.linspace(0.95, 1.05, 7):
    a_scaled = atoms.copy()
    a_scaled.set_cell(atoms.cell * scale, scale_atoms=True)
    a_scaled.calc = EMT()
    e = a_scaled.get_potential_energy()
    volumes.append(a_scaled.get_volume())
    energies.append(e)

# Fit with Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa (ASE returns in eV/Å³)
B_GPa = B * 160.217662  # 1 eV/Å³ = 160.217662 GPa

# Calculate equilibrium lattice constant
atoms_eq = atoms.copy()
atoms_eq.set_cell(np.diag([v0**(1/3)]*3), scale_atoms=True)  # Approximate cubic cell
a0 = atoms_eq.cell[0, 0]  # Since FCC, all lattice params equal

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
