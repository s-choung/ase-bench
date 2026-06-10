from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import ExpCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

opt = PreconLBFGS(ExpCellFilter(atoms), precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.get_number_of_steps()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell:\n{atoms.cell}")
