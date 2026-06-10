import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Initialize Cu FCC bulk with conventional cubic unit cell
atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
original_cell = atoms.get_cell().copy()

volumes, energies = [], []
# Scan scaled cell volumes around initial guess
for scale in np.linspace(0.95, 1.05, 7):
    scaled = atoms.copy()
    scaled.set_cell(original_cell * scale, scale_atoms=True)
    scaled.calc = EMT()
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())

# Fit Birch-Murnaghan EOS to extract equilibrium properties
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, _, B = eos.fit()
a0 = v0 ** (1/3)
B_gpa = B * 160.218  # Convert bulk modulus from eV/Å³ to GPa

# Output results
print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B_gpa:.1f} GPa")
