import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create FCC silver bulk structure
ag_bulk = Atoms('Ag', cell=[[0, 2.89, 2.89],
                            [2.89, 0, 2.89],
                            [2.89, 2.89, 0]],
                pbc=True)

# Vary lattice constant over +/-5% around equilibrium
lattice_constants = np.linspace(0.95 * 2.89, 1.05 * 2.89, 7)
energies = []

for a in lattice_constants:
    # Rescale the cell while keeping it cubic
    ag_bulk.set_cell([[0, a, a], [a, 0, a], [a, a, 0]], scale_atoms=True)
    
    # Use EMT calculator
    calc = EMT()
    ag_bulk.set_calculator(calc)
    
    # Calculate energy
    energy = ag_bulk.get_potential_energy()
    energies.append(energy)

# Fit the Energies vs Volume data to Birch-Murnaghan EOS
eos = EquationOfState(volumes=[(a ** 3) for a in lattice_constants],  # Volume = a^3 for cubic
                      energies=energies)
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa (from eV/Å³)
B_gpa = B * 160.21766  # 1 eV/Å³ = 160.21766 GPa

# Output the equilibrium lattice constant and bulk modulus
print(f"Equilibrium lattice constant: {v0**(1/3):.4f} Å")
print(f"Bulk modulus: {B_gpa:.2f} GPa")
