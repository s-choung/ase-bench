from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('H2O',
              positions=[(0.0, 0.0, 0.0),
                         (0.96, 0.0, 0.0),
                         (-0.24, 0.93, 0.0)])

atoms.calc = EMT()
try:
    atoms.get_potential_energy()
except NotImplementedError:
    atoms.calc = LennardJones()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

print('{:>4s} {:>12s} {:>12s}'.format('Mode', 'Freq(cm-1)', 'Energy(eV)'))
for i, freq in enumerate(vib.get_frequencies()):
    energy = freq * units.invcm
    print(f'{i:4d} {freq:12.4f} {energy:12.6f}')
