from ase.build import bulk
from ase.optimize import PreconLBFGS
from ase.calculators.emt import EMT

calculator = EMT(precon='auto')
atoms = bulk('Ni', 'fcc', size=(2, 2, 2))

dyn = PreconLBFGS(atoms, calculator, fmax=0.01)
dyn.run(fmax=0.01)

print(dyn.steps)
print(atoms.get_potential_energy())
print(atoms.get_cell())
