from ase import Atoms
from ase.optimize.precon import PreconLBFGS
from ase.calculators.emt import EMT

a = 3.52
ni = Atoms('Ni', positions=[[0, 0, 0]], cell=[[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]], pbc=True)
ni *= (4, 4, 4)
ni.calc = EMT()

opt = PreconLBFGS(ni, precon='auto')
opt.run(fmax=0.01)

print(f'Steps: {opt.get_number_of_steps()}')
print(f'Energy: {ni.get_potential_energy()} eV')
print(f'Cell: {ni.cell[:]}')
