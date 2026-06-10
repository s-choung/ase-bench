```python
from ase import Atoms
from ase.cell import Cell
from ase import units
from ase.md.langevin import Langevin
from ase.optimize import BFGS

# Build Cu FCC 2x2x2 supercell
atoms = Atoms('Cu', cell=Cell(3.55, 3.55, 3.55), pbc=True)
for atom in atoms:
    atom.tag = 0

# Initial temperature
initial_temp = 300

# MD parameters
steps = 200
dt = 5 * units.fs
temperature_ramp = [initial_temp + (600 - initial_temp) * i / (steps / 50) for i in range(steps // 50 + 1)]

# Langevin MD setup
atoms.calc = Langevin {
    'temperature_K': temperature_ramp,
    'friction': 0.01 / units.fs,
}
MaxwellBoltzmannDistribution(atoms, temperature_K=initial_temp)
Stationary(atoms)

# Run MD
atoms.run(t
