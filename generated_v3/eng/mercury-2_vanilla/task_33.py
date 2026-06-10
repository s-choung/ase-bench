from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build CH4 and attach EMT calculator
atoms = molecule('CH4')
atoms.set_calculator(EMT())

# Geometry optimization
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, delta=0.01)
vib.run()
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f > 0]

print('Real frequencies (cm⁻¹):')
for f in real_freqs:
    print(f)

vib.clean()
