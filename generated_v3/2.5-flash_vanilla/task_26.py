from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# 1. Create Ni FCC bulk structure
atoms = bulk('Ni', 'fcc', a=3.52)

# 2. Set EMT calculator
atoms.calc = EMT()

# 3. Initialize PreconLBFGS optimizer with precon='auto'
optimizer = PreconLBFGS(atoms, precon='auto')

# 4. Run optimization until fmax < 0.01
optimizer.run(fmax=0.01)

# 5. Print results
print(f"Optimization finished in {optimizer.get_number_of_steps()} steps.")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final cell parameter (a): {atoms.get_cell()[0, 0]:.4f} Angstrom")
