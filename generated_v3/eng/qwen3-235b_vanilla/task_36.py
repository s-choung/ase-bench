from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Ag FCC bulk
ag = bulk('Ag', 'fcc')

# Calculator
ag.set_calculator(EMt())

# Lattice constant range: +/-5%
a0 = ag.get_cell()[0, 0]
factors = np.linspace(0.95, 1.05, 7)
energies = []
cells = []

for f in factors:
    ag_copy = ag.copy()
    ag_copy.set_cell(ag.get_cell() * f, scale_atoms=True)
    ag_copy.set_calculator(EMT())
    energy = ag_copy.get_potential_energy()
    energies.append(energy)
    cells.append(ag_copy.get_cell()[0, 0])

# Fit EOS
eos = EquationOfState(cells, energies)
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa (1 eV/Å³ = 160.217662 GPa)
a_eq = np.cbrt(v0)  # Assuming cubic symmetry, v0 = a^3
B_GPa = B * 160.217662

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
