import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

# 1. Create the initial Ag FCC structure
atoms = bulk('Ag', 'fcc', a=4.09)
atoms.calc = EMT()

# 2. Calculate energies for a range of lattice constants
cell = atoms.get_cell()
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 7):
    atoms_scaled = atoms.copy()
    atoms_scaled.set_cell(cell * x, scale_atoms=True)
    atoms_scaled.calc = EMT()
    volumes.append(atoms_scaled.get_volume())
    energies.append(atoms_scaled.get_potential_energy())

# 3. Fit the data to the Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 4. Calculate and print the results
# For a conventional FCC cell, V = a^3, so a = V^(1/3)
eq_lattice_const = v0**(1/3)
bulk_modulus_gpa = B * GPa

print(f"Equilibrium lattice constant (a0): {eq_lattice_const:.4f} Å")
print(f"Bulk modulus (B): {bulk_modulus_gpa:.2f} GPa")
