from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.0)
atoms.calc = EMT()

class StepCounter:
    def __init__(self):
        self.nsteps = 0
    def __call__(self, atoms=None):
        self.nsteps += 1

counter = StepCounter()
opt = LBFGS(atoms, logfile=None)
opt.attach(counter)
opt.run(fmax=0.01)

print(f"Steps: {counter.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
