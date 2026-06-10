from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# FCC bulk Ni
atoms = Atoms('Ni', positions=[[0, 0, 0]], cell=[[3.5, 0, 0], [0, 3.5, 0], [0, 0, 3.5]], pbc=True)
atoms.calc = EMT()

# Optimization
opt = PreconLBFGS(atoms, precon="auto")
opt.run(fmax=0.01)

# Output
print(f"Steps: {opt.nsteps}")
print(f"Energy: {atoms.get_potential_energy():.3f} eV")
print("Cell:", atoms.get_cell_lengths_and_angles())
