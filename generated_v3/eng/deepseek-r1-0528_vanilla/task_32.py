from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('H2O', positions=[[0, 0, 0], [0.95, 0.3, 0], [-0.95, 0.3, 0]])
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
freqs_ev = vib.get_frequencies().real

factor = 8065.54429
for i, freq in enumerate(freqs_ev):
    if abs(freq) > 1e-4:
        freq_cm = freq * factor
        print(f"{freq_cm:.2f} cm^-1, {freq:.6f} eV")

vib.clean()
