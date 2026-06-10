from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS

# Define Cu FCC bulk structure
a = 3.615  # equilibrium lattice constant at room temperature (Å)
cells = [2, 2, 2]
atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=[a, a, a] * cells)

# Set calculator
atoms.calc = EMT()

# Initial relaxation to remove immediate forces
atoms.set_calculator(atoms.calc)
dyn = BFGS(atoms)
dyn.run(fmax=0.0001)

# Generate volumes for EOS fitting
volumes = [v for v in [atoms.cell volume * (1 - i / 10.0) for i in range(3)] +
           [atoms.cell volume] +
           [atoms.cell volume * (1 + i / 10.0) for i in range(3)]]

energy_vs_volume = [(atoms.set_cell([v] * cells, scale_atoms=True).energy, v) for v in volumes]

# Fit EOS
eos = EquationOfState(energy_vs_volume)

# Find equilibrium volume and bulk modulus
v0, b = eos.fit()

print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Equilibrium lattice constant: {v0**(1/3):.3f} Å")
print(f"Bulk modulus: {b:.2f} GPa")
