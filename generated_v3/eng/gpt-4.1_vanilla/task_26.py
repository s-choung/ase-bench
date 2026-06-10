from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT(precon='auto')

opt = PreconLBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print("Steps:", len(opt.log))
print("Energy:", atoms.get_potential_energy())
print("Cell:\n", atoms.cell)
