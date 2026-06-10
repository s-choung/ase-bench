from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk("Ni", "fcc", a=3.52, cubic=True)
atoms.calc = EMT()

opt_atoms = FrechetCellFilter(atoms)
opt = PreconLBFGS(opt_atoms, precon="auto", logfile=None)
opt.run(fmax=0.01)

a = atoms.cell.cellpar()[0]

print(f"steps: {opt.nsteps}")
print(f"final_energy_eV: {atoms.get_potential_energy():.10f}")
print(f"cell_parameter_A: {a:.10f}")
