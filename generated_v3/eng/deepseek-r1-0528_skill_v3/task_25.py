from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create FCC Cu with initial lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)

# Attach calculator
atoms.calc = EMT()

# Calculate initial lattice constant and energy using FCC relationship
def get_lattice_constant(atoms):
    n_atoms = len(atoms)
    vol_per_atom = atoms.get_volume() / n_atoms
    return (4 * vol_per_atom) ** (1/3)

a_initial = get_lattice_constant(atoms)
energy_initial = atoms.get_potential_energy()

# Optimize structure with constant volume filter
filtered_atoms = FrechetCellFilter(atoms)
opt = BFGS(filtered_atoms)
opt.run(fmax=0.01)

# Extract final lattice constant and energy
a_final = get_lattice_constant(atoms)
energy_final = atoms.get_potential_energy()

# Print results
print(f"Before: Lattice constant = {a_initial:.4f} Å, Energy = {energy_initial:.6f} eV")
print(f"After:  Lattice constant = {a_final:.4f} Å, Energy = {energy_final:.6f} eV")
