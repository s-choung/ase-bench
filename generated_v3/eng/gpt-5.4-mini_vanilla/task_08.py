from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# N2 molecule
atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.center(vacuum=5.0)
atoms.calc = EMT()

# Relax geometry
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='n2_vib')
vib.run()

freqs = vib.get_frequencies()
for i, f in enumerate(freqs):
    print(f"Mode {i}: {f}")

vib.clean()
