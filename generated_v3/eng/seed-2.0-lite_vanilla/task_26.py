from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Initialize FCC Ni bulk with initial lattice parameter
atoms = bulk('Ni', 'fcc', a=3.55)
atoms.calc = EMT()

# Set up and run PreconLBFGS optimization
dyn = PreconLBFGS(atoms, precon='auto')
dyn.run(fmax=0.01)

# Output required results
print(f"Optimization steps: {dyn.get_number_of_steps()}")
print(f"Final total energy (eV): {atoms.get_potential_energy():.4f}")
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f"Final cell parameters: a={a:.4f} Å, b={b:.4f} Å, c={c:.4f} Å, α={alpha:.1f}°, β={beta:.1f}°, γ={gamma:.1f}°")
