import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.preconlbfgs import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.set_calculator(EMT(precon='auto'))
opt = PreconLBFGS(atoms, fmax=0.01)
opt.run()

print(f'Steps: {opt.get_number_of_steps()}')
print(f'Energy: {atoms.get_potential_energy()} eV')
print(f'Cell: {atoms.get_cell()}')
