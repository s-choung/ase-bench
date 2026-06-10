from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

ecf = FrechetCellFilter(atoms)
opt = PreconLBFGS(ecf, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Final Energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters:\n{atoms.get_cell()}")
