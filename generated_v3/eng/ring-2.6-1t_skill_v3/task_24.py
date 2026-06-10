from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

step_count = [0]
def counter(atoms=None):
    step_count[0] += 1

opt = LBFGS(atoms, callback=counter)
opt.run(fmax=0.01)

print(f'Steps: {step_count[0]}')
print(f'Final energy: {atoms.get_potential_energy():.4f} eV')
