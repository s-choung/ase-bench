import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Initial guess for Cu FCC lattice constant
a0 = 3.6
atoms0 = bulk('Cu', 'fcc', a=a0)

# Calculate EOS curve: scale cell and compute energy
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    atoms = atoms0.copy()
    atoms.set_cell(atoms0.cell * scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Equilibrium lattice constant (FCC: a = V^(1/3))
a_eq = v0 ** (1/3)

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Equilibrium volume: {v0:.4f} Å^3")
print(f"Bulk modulus: {B * 1e-3:.2f} GPa")  # Convert eV/Å^3 to GPa (1 eV/Å^3 = 160.217 GPa)
