from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters [a,b,c,α,β,γ]: {atoms.cell.cellpar()}")
