from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.constraints import FixCom
from ase.filters import FrechetCellFilter

# Create FCC Ni bulk
atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)

# Apply calculator and filter for cell+position optimization
atoms.calc = EMT()
filter = FrechetCellFilter(atoms)  # Or ExpCellFilter/UnitCellFilter

# Constrain center of mass (optional but recommended for bulk)
atoms.set_constraint(FixCom())

# Preconditioned optimizer
opt = PreconLBFGS(filter, precon='auto')  # 'auto' chooses preconditioner smartly

# Run optimization
opt.run(fmax=0.01)

# Output results
print(f"Optimization steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final cell parameters (Å, degrees): {atoms.get_cell_lengths_and_angles()}")
