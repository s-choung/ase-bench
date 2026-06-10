from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# N2 molecule, initial bond ~1.1 Å
mol = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)], calculator=EMT())

# Geometry optimization
BFGS(mol).run(fmax=0.001)

# Vibrational analysis
vib = Vibrations(mol, delta=0.01, name='n2_vib')
vib.run()
freqs_cm = vib.get_frequencies()          # cm⁻¹
freqs_thz = vib.get_frequencies(unit='THz')  # THz

print('Vibrational frequencies (cm⁻¹):', freqs_cm)
print('Vibrational frequencies (THz):', freqs_thz)
