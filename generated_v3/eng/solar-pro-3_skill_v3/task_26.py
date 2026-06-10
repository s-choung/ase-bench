from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS, PreconLBFGS, FrechetCellFilter

# build Ni FCC bulk (a≈3.52 Å gives ~40 atoms)
atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

# use FrechetCellFilter so cell can be optimized together with positions
opt = BFGS(FrechetCellFilter(atoms))

print("Optimization running...")
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell (Å): {atoms.get_cell().tolist()}")   # a, b, c, α, β, γ in Angstrom
