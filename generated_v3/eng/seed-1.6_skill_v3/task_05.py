from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Generate Cu FCC bulk and scaled cells
cu = bulk('Cu', 'fcc', a=3.6)
cell = cu.get_cell()
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    scaled = cu.copy()
    scaled.set_cell(cell * scale, scale_atoms=True)
    scaled.calc = EMT()
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())

# EOS fitting (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, _, B_ev_ang3 = eos.fit()

# Convert bulk modulus to GPa (1 eV/Å³ = 160.21766208 GPa)
B_gpa = B_ev_ang3 * 160.21766208
# FCC cubic lattice constant (V = a³)
a0 = v0 ** (1/3)

# Print results
print(f'Equilibrium lattice constant: {a0:.3f} Å')
print(f'Equilibrium volume: {v0:.3f} Å³')
print(f'Bulk modulus: {B_gpa:.2f} GPa')
