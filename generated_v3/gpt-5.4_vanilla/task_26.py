from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', cubic=True)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto', logfile=None)
opt.run(fmax=0.01)

e = atoms.get_potential_energy()
a = atoms.cell.lengths()[0]

print(opt.nsteps)
print(e)
print(a)
