from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('N2', positions=[[0, 0, 0], [1.1, 0, 0]])
atoms.calc = EMT()
BFGS(atoms).run(fmax=1e-2)
vib = Vibrations(atoms)
vib.run()
for f in vib.get_frequencies():
    if f > 1:
        print(f"{f:.1f} cm⁻¹")
