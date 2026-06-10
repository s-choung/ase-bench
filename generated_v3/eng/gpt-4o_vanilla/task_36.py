from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Set up Ag FCC bulk.
a0 = 4.09  # Initial lattice constant guess for Ag.
bulk_ag = bulk('Ag', 'fcc', a=a0)

# Set calculator
bulk_ag.calc = EMT()

# Vary the lattice constant by +/-5% over 7 points
scale_factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for sf in scale_factors:
    bulk_ag.set_cell(bulk_ag.cell * sf, scale_atoms=True)
    volumes.append(bulk_ag.get_volume())
    energies.append(bulk_ag.get_potential_energy())

# Fit Equation of State
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# Print results
equilibrium_lattice_constant = (v0 / bulk_ag.get_number_of_atoms())**(1/3)
bulk_modulus_gpa = B / 1.60218e-19 * 1e24

print(f'Equilibrium lattice constant: {equilibrium_lattice_constant:.3f} Å')
print(f'Bulk modulus: {bulk_modulus_gpa:.2f} GPa')
