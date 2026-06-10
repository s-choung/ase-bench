from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create a copper FCC bulk
a = 3.6  # Initial guess for lattice constant in angstrom
cu = Atoms('Cu', positions=[(0, 0, 0)], cell=(a, a, a), pbc=True)
cu.set_calculator(EMT())

# Calculate volume vs energy
volumes = []
energies = []
for i in range(15):
    cu.set_cell((a, a, a), scale_atoms=True)
    energies.append(cu.get_potential_energy())
    volumes.append(cu.get_volume())
    a += 0.1

# Fit equation of state
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} A^3")
print(f"Bulk modulus: {B:.1f} GPa")
