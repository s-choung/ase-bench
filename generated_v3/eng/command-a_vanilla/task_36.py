from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Ag FCC bulk structure
a = 4.09  # Experimental lattice constant for Ag
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          size=(1, 1, 1), symbol='Ag', pbc=True, latticeconstant=a)
atoms.calc = EMT()

# Define lattice constant range
volumes = []
energies = []
for ratio in np.linspace(0.95, 1.05, 7):
    atoms.set_cell(atoms.cell * ratio, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birch_murnaghan')
v0, e0, B = eos.fit()

# Calculate bulk modulus in GPa
B_GPa = B / 1e9

# Print results
print(f'Equilibrium lattice constant: {v0**(1/3) / a:.4f} * a0')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
