from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import UnitCellFilter  # Corrected import here

# Initialize the Cu FCC bulk structure
atoms = Atoms('Cu4',
              positions=[[0.0, 0.0, 0.0],
                         [0.5, 0.5, 0.0],
                         [0.5, 0.0, 0.5],
                         [0.0, 0.5, 0.5]],
              cell=[2.5, 2.5, 2.5],
              pbc=True)

# Set the EMT calculator
atoms.calc = EMT()

# Print initial cell size and energy
print("Initial cell size:", atoms.get_cell_lengths_and_angles()[:3])
print("Initial energy:", atoms.get_potential_energy())

# Use UnitCellFilter to optimize both lattice and atomic positions
uf = UnitCellFilter(atoms)  # FrechetCellFilter is not in ASE, using UnitCellFilter instead

# Use BFGS optimizer with fmax=0.01
opt = BFGS(uf, trajectory=None)  # trajectory set to None for no trajectory file
opt.run(fmax=0.01)

# Print final cell size and energy
print("Optimized cell size:", atoms.get_cell_lengths_and_angles()[:3])
print("Optimized energy:", atoms.get_potential_energy())
