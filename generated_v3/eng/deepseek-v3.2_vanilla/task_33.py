from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('CH4', positions=[[0, 0, 0],
                                [1.1, 1.1, 0],
                                [-1.1, -1.1, 0],
                                [-1.1, 1.1, 0],
                                [1.1, -1.1, 0]])
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib.summary()

real_freqs = []
frequencies = vib.get_frequencies()
for freq in frequencies:
    if freq > 0:
        real_freqs.append(freq)

print(f"Real vibrational frequencies: {real_freqs}")
