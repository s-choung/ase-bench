from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Define H2O molecule
d_OH = 0.97  # Å
angle_HOH = 104.45  # degrees
import math
theta = math.radians(angle_HOH / 2)
x = d_OH * math.sin(theta)
y = d_OH * math.cos(theta)

atoms = Atoms('H2O', positions=[(0,0,0), (x, y, 0), (-x, y, 0)])

atoms.calc = EMT()

print(f"Initial energy: {atoms.get_potential_energy():.6f} eV")

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print(f"Final energy:   {atoms.get_potential_energy():.6f} eV")
