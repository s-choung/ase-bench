from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()

filt = FrechetCellFilter(atoms)
opt = PreconLBFGS(filt, precon='auto')
opt.run(fmax=0.01)

energy = atoms.get_potential_energy()
a = atoms.cell.cellpar()[0]

print(opt.nsteps)
print(energy)
print(a)
