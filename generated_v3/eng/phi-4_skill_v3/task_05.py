from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create Cu bulk structure
cu_bulk = bulk('Cu', 'fcc', a=3.5)

# Initialize blank lists for volumes and energies
volumes = []
energies = []

# Calculate energy for a series of strained lattice parameters
for strain in np.linspace(0.9, 1.1, 7):
    cu_copy = cu_bulk.copy()
    cu_copy.set_cell(cu_copy.get_cell() * strain)
    cu_copy.set_pbc((True, True, True))
    cu_copy.calc = EMT()
    cu_copy.get_potential_energy()
    volumes.append(cu_copy.get_volume())
    energies.append(cu_copy.get_potential_energy())

# Fit data to Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert equilibrium volume to lattice constant
a0 = (v0 / cu_bulk.get_number_of_atoms())**(1/3)

# Print results
print(f"Equilibrium lattice constant: {a0:.6f} Å")
print(f"Equilibrium volume: {v0:.6f} Å³")
print(f"Bulk modulus: {B:.6f} GPa")
