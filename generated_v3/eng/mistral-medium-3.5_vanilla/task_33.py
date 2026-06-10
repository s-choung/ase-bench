from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations

atoms = Atoms('CH4', positions=[[0, 0, 0], [1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]])
atoms.calc = EMT()
dyn = QuasiNewton(atoms)
dyn.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib.clean()

freqs = [f for f in vib.get_frequencies() if f.imag == 0]
print([f.real for f in freqs])
