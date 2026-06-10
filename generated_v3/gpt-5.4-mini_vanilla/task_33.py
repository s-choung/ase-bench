from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('CH4', positions=[
    (0.0000, 0.0000, 0.0000),
    (0.6291, 0.6291, 0.6291),
    (-0.6291, -0.6291, 0.6291),
    (-0.6291, 0.6291, -0.6291),
    (0.6291, -0.6291, -0.6291),
], cell=[15, 15, 15], pbc=False)

atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='ch4_emt_vib')
vib.run()

freqs = vib.get_frequencies()
real_freqs = [f.real for f in freqs if abs(f.imag) < 1e-8]

print(real_freqs)

vib.clean()
