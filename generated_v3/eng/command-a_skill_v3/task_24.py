```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC bulk structure
atoms = Atoms('Au', cell=[[2, 0, 0], [0, 2, 0], [0, 0, 2]], pbc=True)
atoms.center()

# Attach EMT calculator
atoms.calc = EMT()

# Initialize LBFGS optimizer
opt = LBFGS(atoms, trajectory=None)

# Perform optimization
num_steps = 0
def print_step(optimizer):
    global num_steps
    num_steps += 1
opt.attach(print_step, interval=1)
opt.run(fmax=0.01
