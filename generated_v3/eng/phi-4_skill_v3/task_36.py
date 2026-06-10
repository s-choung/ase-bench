from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create a bulk Ag FCC structure
atoms = bulk('Ag', 'fcc', a=4.09)
atoms.set_calculator(EMT())

# Arrays to store volumes and energies
volumes = []
energies = []

# Loop over 7 points in the range of +5% to -5% of the initial lattice constant
for x in np.linspace(0.95, 1.05, 7):
    # Scale cell by factor x
    a = atoms.copy()
    a.set_cell(a.get_cell() * x, scale_atoms=True)
    a.calc = EMT()  # Ensure that each copy's calculator is set
    
    # Compute volume and energy
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit the volumes and energies using the Birch-Murnaghan equation of state
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')

# Perform the fit
v0, e0, B = eos.fit()

# Convert B from eV/Å^3 to GPa (1 eV/Å^3 = 160.21766208 GPa)
B_GPa = B * 160.21766208

# Calculate the equilibrium lattice constant
a_eq = (v0 / atoms.get_volume())**(1/3) * atoms.get_cell_lengths_and_angles()[0]

# Print the results
print(f"Equilibrium lattice constant (a0): {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
