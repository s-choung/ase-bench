from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.constraints import ExpCellFilter

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()
ecf = ExpCellFilter(atoms)
opt = PreconLBFGS(ecf, precon='auto')
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
print("Cell:")
print(atoms.get_cell()[:])
