from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Define CH4 molecule (tetrahedral geometry)
d = 1.09
atoms = Atoms('CH4',
              positions=[(0, 0, 0),
                         (d, d, d), (d, -d, -d),
                         (-d, d, -d), (-d, -d, d)],
              calculator=EMT())

# Optimize geometry
BFGS(atoms).run(fmax=0.05)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()

# Filter and print real frequencies
for freq in vib.get_frequencies():
    if freq.imag == 0:
        print(freq.real)
