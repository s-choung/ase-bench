from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("Initial cell a: {:.3f} Ang".format(atoms.get_cell()[0, 0]))
print("Initial energy: {:.6f} eV".format(atoms.get_potential_energy()))

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("Final cell a: {:.3f} Ang".format(atoms.get_cell()[0, 0]))
print("Final energy: {:.6f} eV".format(atoms.get_potential_energy()))
