from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create FCC Cu bulk
cu = bulk('Cu', 'fcc', a=3.6)

# Calculate energy at different lattice constants
cell = cu.get_cell()
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    atoms = cu.copy()
    atoms.set_cell(cell * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Get equilibrium lattice constant
a0 = (v0 * 4) ** (1/3)  # FCC: 4 atoms per cell

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Equilibrium volume per atom: {v0:.4f} Å³")
print(f"Equilibrium volume (4-atom cell): {v0:.4f} Å³")
print(f"Bulk modulus: {B:.1f} GPa")
print(f"Min energy: {e0:.4f} eV")
