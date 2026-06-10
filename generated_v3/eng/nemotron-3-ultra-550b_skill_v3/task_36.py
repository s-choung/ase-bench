import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# Create Ag FCC bulk
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
calc = EMT()
atoms.calc = calc

# Reference cell and volume
cell0 = atoms.get_cell()
vol0 = atoms.get_volume()

# Volume range +/-5%, 7 points
volumes = []
energies = []
for scale in np.linspace(0.95, 1.05, 7):
    atoms_scaled = atoms.copy()
    atoms_scaled.set_cell(cell0 * scale**(1/3), scale_atoms=True)
    atoms_scaled.calc = calc
    volumes.append(atoms_scaled.get_volume())
    energies.append(atoms_scaled.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Equilibrium lattice constant from equilibrium volume
a0 = (v0 / 4) ** (1/3) * 4  # FCC: 4 atoms per cubic cell, v0 = a0^3 / 4 * 4? Wait.
# FCC conventional cell has 4 atoms. Volume per atom = a^3/4. Total volume = a^3.
# ASE bulk('Ag', 'fcc', cubic=True) creates conventional cubic cell with 4 atoms.
# So v0 = a0^3.
a0 = v0 ** (1/3)

# Bulk modulus in GPa (ASE returns eV/A^3)
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
