from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.set_calculator(EMT())
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
real_freqs = [f.real for f in freqs if abs(f.imag) < 1e-3]
print("Real vibrational frequencies (eV):")
for f in real_freqs:
    print(f)
