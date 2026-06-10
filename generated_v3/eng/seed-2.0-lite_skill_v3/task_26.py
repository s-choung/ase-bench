from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

# Initialize Ni FCC bulk
atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

# Set up cell filter for simultaneous cell/position optimization
filtered_atoms = FrechetCellFilter(atoms)

# Run PreconLBFGS optimization
opt = PreconLBFGS(filtered_atoms, precon='auto')
opt.run(fmax=0.01)

# Output results
steps = opt.get_number_of_steps()
final_energy = atoms.get_potential_energy()
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()

print(f"Number of optimization steps: {steps}")
print(f"Final potential energy: {final_energy:.4f} eV")
print(f"Final cell parameters: a={a:.3f} Å, b={b:.3f} Å, c={c:.3f} Å, α={alpha:.1f}°, β={beta:.1f}°, γ={gamma:.1f}°")
