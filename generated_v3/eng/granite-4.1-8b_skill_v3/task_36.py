from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.thermochemistry import EquationOfState
import numpy as np

# Define FCC Ag bulk structure with initial lattice constant
a0 = 4.09  # FCC Ag lattice constant in Å
atoms = bulk('Ag', 'fcc', a=a0)
atoms.calc = EMT()

# Collect volumes and energies for varying lattice constants
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = a0 * x
    atoms_copy = atoms.copy()
    atoms_copy.set_cell(atoms_copy.cell * x, scale_atoms=True)
    volumes.append(atoms_copy.get_volume())
    energies.append(atoms_copy.get_potential_energy())

# Perform Birch-Murnaghan EOS fitting
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa
bulk_modulus_GPa = B / (6 * 0.06)  # 0.06 = 6% strain difference in this context

print(f"Equilibrium lattice constant: {v0**(1/3)/0.529177:>.3f} Å")
print(f"Equilibrium energy: {e0:.6f} eV")
print(f"V0 (volume): {v0:.4f} Å³")
print(f"Bulk modulus: {bulk_modulus_GPa:.2f} GPa")
