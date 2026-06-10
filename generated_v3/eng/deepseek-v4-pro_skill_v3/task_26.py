from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()
filtered = FrechetCellFilter(atoms)
opt = PreconLBFGS(filtered, precon='auto')
opt.run(fmax=0.01)

print(f"Number of steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print("Cell parameters:")
print(atoms.get_cell())
