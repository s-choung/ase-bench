import ase
from ase import build, optimize, phonons
from ase.calculators.emt import EMT

atoms = build.molecule('CH4')
atoms.set_cell([20., 20., 20.])
atoms.center()

calc = EMT()
atoms.set_calculator(calc)

optimize.BFGS(atoms).run(fmax=0.01)

phonon = phonons.Phonon(atoms, calc)
phonon.run()

frequencies = phonon.get_frequencies()
real_freqs = [f.real for f in frequencies if abs(f.imag) < 1e-3]

print('Real frequencies:', real_freqs)
