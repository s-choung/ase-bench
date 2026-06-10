from ase import molecule, BFGS, Vibrations
from ase.calculators.emt import EMT

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms, name='n2_vib')
vib.run()
print(vib.get_frequencies())
