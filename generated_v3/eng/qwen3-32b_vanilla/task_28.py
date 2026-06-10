from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

def target_temp(t):
    return 300.0 + 300 * t / 1e-12

atoms = fcc('Cu', size=(2, 2, 2))
atoms.calc = EMT()

dyn = Langevin(atoms, 5 * units.fs, target_temp, 0.05, loginterval=0)

for step in range(0, 200, 50):
    dyn.run(50)
    ke = atoms.get_kinetic_energy()
    temp = (2 * ke) / (3 * len(atoms) * units.kB)
    print(f'Step {step + 50}: Temperature = {temp} K')
