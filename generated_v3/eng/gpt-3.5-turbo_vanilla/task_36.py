from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create Ag FCC bulk
a_vals = [1.05, 1.025, 1.0, 0.975, 0.95, 0.925, 0.9]  # lattice constants
energies = []
for a in a_vals:
    bulk = Atoms('Ag', scaled_positions=[(0, 0, 0)], cell=[a, a, a], pbc=True)
    bulk.set_calculator(EMT())
    energies.append(bulk.get_potential_energy())

# Fit the EOS
eos = EquationOfState(a_vals, energies)
v0, e0, B = eos.fit()[:3]

# Convert lattice constant to equilibrium volume and bulk modulus
a0 = (v0)**(1/3)
a0_GPa = B * a0 / (2 * (1 + B))
print('Equilibrium lattice constant: {:.3f} Angstrom'.format(a0))
print('Bulk modulus: {:.3f} GPa'.format(a0_GPa))
