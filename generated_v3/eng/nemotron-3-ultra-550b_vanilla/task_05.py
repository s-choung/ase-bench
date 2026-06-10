from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Setup Cu FCC bulk with EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Generate volumes around initial guess
volumes = []
energies = []
initial_volume = atoms.get_volume()

for scale in np.linspace(0.95, 1.05, 7):
    atoms.set_cell(atoms.cell * scale**(1/3), scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit Equation of State (Birch-Murnaghan)
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# Convert bulk modulus from eV/A^3 to GPa (1 eV/A^3 = 160.21766208 GPa)
B_GPa = B * 160.21766208

# Equilibrium lattice constant from equilibrium volume (FCC: 4 atoms/cell)
a0 = (v0 / 4 * 4)**(1/3)  # v0 is volume per atom? No, eos.fit returns total volume for the cell.
# atoms object has 1 atom in primitive cell? bulk('Cu', 'fcc') creates conventional cell (4 atoms).
# ASE bulk('Cu', 'fcc') creates a conventional cubic cell with 4 atoms.
# EquationOfState expects volumes/energies for the *entire* atoms object.
# So v0 is the equilibrium volume of the 4-atom conventional cell.
a0 = (v0 / 4)**(1/3) * 4**(1/3) # V = a^3 for conventional cell. V_conventional = a^3.
# Wait: bulk('Cu', 'fcc') returns conventional cell (4 atoms). Volume = a^3.
# So a0 = v0**(1/3).

a0 = v0**(1/3)

print(f"Equilibrium volume (conventional cell): {v0:.4f} Å³")
print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
