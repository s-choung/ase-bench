from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
atoms = bulk('Ni', 'fcc')
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)
print(opt.nsteps, atoms.get_potential_energy(), atoms.cell.cellpar())
