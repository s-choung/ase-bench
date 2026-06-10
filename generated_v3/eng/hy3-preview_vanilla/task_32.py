from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create H2O molecule with experimental geometry
d = 0.9575  # OH bond length (Å)
a = 104.51  # HOH angle (degrees)
import math
pos = [(0, 0, 0),
       (d, 0, 0),
       (d * math.cos(math.radians(a)), d * math.sin(math.radians(a)), 0)]
water = Atoms('OH2', positions=pos)

# Set calculator
water.calc = EMT()

# Compute vibrational modes
vib = Vibrations(water, name='vib', delta=0.01)
vib.run()

# Print results
for mode in vib.get_modes():
    freq = mode.get_frequency()  # cm^-1
    energy = mode.get_energy()   # eV
    print(f"Mode: {freq:.1f} cm^-1, {energy:.6f} eV")
