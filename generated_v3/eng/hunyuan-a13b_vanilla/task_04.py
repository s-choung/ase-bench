from ase import Atom, Molecule
from ase.calculator.emt import EMT
from ase.optimize import BFGS

# Initialize H2O molecule
mol = Molecule('H2O', positions=[['O', (0., 0., 0.)],
                           ['H', (0.757, 0.586, 0.)],
                           ['H', (-0.757, 0.586, 0.)]], unit='Angstrom')

# Set up EMT calculator
calc = EMT()

# Add calculator to molecule
mol.calc = calc

# Print energy before optimization
print("Energy before optimization:", mol.get_electronic_energy())

# Perform geometry optimization
opt = BFGS(mol)
opt.kernel()

# Print energy after optimization
print("Energy after optimization:", mol.get_electronic_energy())
