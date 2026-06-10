from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Setup FCC Ag with EMT calculator
atoms = bulk('Ag', 'fcc', a=4.1, cubic=True)
atoms.calc = EMT()

# Reference volume
v0 = atoms.get_volume()

# Generate 7 volumes within +/- 5%
volumes = np.linspace(v0 * 0.95, v0 * 1.05, 7)
energies = []

for v in volumes:
    atoms.set_cell(atoms.cell * (v / atoms.get_volume()) ** (1/3), scale_atoms=True)
    energies.append(atoms.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v_eq, e_eq, B = eos.fit()

# Convert bulk modulus from eV/A^3 to GPa (1 eV/A^3 = 160.21766208 GPa)
B_GPa = B * 160.21766208
a_eq = v_eq ** (1/3) * 4 / (4 ** 0.5)  # FCC: V = a^3/4 -> a = (4V)^(1/3)
# Correct formula for cubic: V = a^3, but bulk() with cubic=True gives conventional cell (4 atoms).
# Volume per atom = a^3/4. Total volume = a^3.
# atoms.get_volume() returns total volume of the cell.
# So a = V^(1/3)
a_eq = v_eq ** (1/3)

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
