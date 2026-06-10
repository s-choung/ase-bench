from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Create FCC Ni bulk
atoms = bulk('Ni', 'fcc', a=3.52)

# Set calculator
atoms.calc = EMT()

# Optimize with PreconLBFGS
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

# Output results
print(f"Steps: {opt.get_number_of_steps()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
print("Cell parameters:")
for i, vec in enumerate(atoms.get_cell()):
    print(f"  a{i+1}: {vec}")
