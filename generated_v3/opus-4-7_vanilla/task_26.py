from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import UnitCellFilter

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

ucf = UnitCellFilter(atoms)
opt = PreconLBFGS(ucf, precon='auto')
opt.run(fmax=0.01)

print("Steps:", opt.nsteps)
print("Final energy:", atoms.get_potential_energy())
print("Cell parameters:", atoms.cell.cellpar())
