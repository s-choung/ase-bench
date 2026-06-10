from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixScaled
from ase.optimize import BFGS
from ase.eos import Eos
import numpy as np

# Define FCC lattice parameters for silver
a0 = 4.09  # Equilibrium lattice constant of Ag (FCC) in Å
a_range = np.linspace(a0 * 0.95, a0 * 1.05, 7)  # Vary lattice constant ±5%

# Create a function to set up and calculate energy for a given lattice constant
def calculate_energy(a):
    # Create Ag FCC bulk structure with lattice constant a
    atoms = Atoms('Ag', positions=[[0, 0, 0], [0.5, 0.5, 0]], pbc=True, cell=[a, a, a])
    # Use EMT calculator
    atoms.calc = EMT()
    # Relax the cell to get the energy at lattice constant a
    relax = BFGS(atoms)
    relax.run(fmax=0)
    return atoms.get_potential_energy()

# Calculate energies for the varying lattice constants
energies = [calculate_energy(a) for a in a_range]

# Fit the Equation of State with Birch-Murnaghan EOS
eos = Eos(atoms=Atoms('Ag', positions=[[0, 0, 0], [0.5, 0.5, 0]], pbc=True, cell=[a_range[0], a_range[0], a_range[0]]),
          energies=energies, sulf=False)

# Extract equilibrium lattice constant and bulk modulus
aeos = eos.fit(method='birch_murnaghan')
a_eq = eos.a_eq
B0 = eos.B0 * 1e-21  # Convert from m²/N to GPa

# Print results
print(f"Equilibrium lattice constant: {a_eq:.3f} Å")
print(f"Bulk modulus: {B0:.2f} GPa")
