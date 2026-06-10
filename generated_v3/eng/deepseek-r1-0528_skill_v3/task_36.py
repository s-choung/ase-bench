from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Base structure: FCC Ag
a0 = 4.09  # Å - experimental lattice constant
atoms = Atoms('Ag', positions=[[0,0,0]], cell=([a0,0,0],[0,a0,0],[0,0,a0]), pbc=True)
atoms *= (2, 2, 2)  # Create 8-atom supercell

# Define strain range: ±5% in 7 steps
strains = np.linspace(-0.05, 0.05, 7)
volumes, energies = [], []

# Calculate energies at different volumes
for s in strains:
    a = a0 * (1 + s)
    scaled_atoms = atoms.copy()
    scaled_atoms.set_cell([a, a, a], scale_atoms=True)
    scaled_atoms.calc = EMT()
    volumes.append(scaled_atoms.get_volume())
    energies.append(scaled_atoms.get_potential_energy())

# Fit EOS and extract parameters
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B_eV = eos.fit()
B_GPa = B_eV * 160.217733  # Convert eV/Å³ to GPa
a_eq = (4 * v0 / len(atoms))**(1/3)  # FCC volume formula: V = a³ * (N/4)

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
