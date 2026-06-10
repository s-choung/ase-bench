from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT(precon='auto')
opt = PreconLBFGS(atoms)
opt.run(fmax=0.01)
print('Steps:', opt.nsteps)
print('Energy:', atoms.get_potential_energy())
print('Cell:\n', atoms.get_cell())
