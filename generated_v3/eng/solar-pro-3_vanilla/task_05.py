from ase.atomistics.dftb import generate_dftb_params
from ase.build import bulk
from ase.calculators.emt import EMT

# Build Cu FCC in a cell
cu = bulk('Cu', 'fcc', a=4.0, cubic=True)
cu.calc = EMT()

# Minimize the atoms
cu.get_potential_energy()

# Fit Birch-Murnaghan EOS
from ase.eos import BirchMurnaghan

volume, energy = BirchMurnaghan().run(cu)
print("Equilibrium volume:", volume)
print("Equilibrium energy:", energy)

# Compute lattice constant and bulk modulus
a_eq = cu.cell.cell[0][0]  # side length of cubic cell
b_eq = BirchMurnaghan().bulk_modulus(cu)

print("Equilibrium lattice constant:", a_eq)
print("Bulk modulus:", b_eq)
