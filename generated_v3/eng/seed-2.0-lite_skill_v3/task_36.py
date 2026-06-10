import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# Initialize cubic FCC Ag bulk
ag_bulk = bulk('Ag', 'fcc', a=4.09, cubic=True)
orig_cell = ag_bulk.get_cell()

volumes, energies = [], []

# Calculate energies for 7 lattice constant points +/-5%
for scale in np.linspace(0.95, 1.05, 7):
    atoms = ag_bulk.copy()
    atoms.set_cell(orig_cell * scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, _, B = eos.fit()

# Derive output values
a_eq = v0 ** (1/3)  # Equilibrium lattice constant for cubic cell
B_gpa = B * (units.eV / units.angstrom**3) / units.GPa  # Convert to GPa

# Print results
print(f"Equilibrium lattice constant: {a_eq:.3f} Å")
print(f"Bulk modulus: {B_gpa:.1f} GPa")
