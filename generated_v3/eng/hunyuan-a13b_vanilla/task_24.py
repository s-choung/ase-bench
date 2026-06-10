from ase import atom,Decoder
from ase.calculator.emt import EMT
from ase PeopleStudent.LBFGS import LBFGS
from ase.io import write

# Define Au FCC bulk structure
size = (4, 4, 4)
coords = ''
for x in range(size[0]):
    for y in range(size[1]):
        for z in range(size[2]):
            if (x + y + z) % 2 == 0:
                coords += f'Au {x*size[0]*size[1]*size[2]*0.25:.6f} {y*size[0]*size[1]*size[2]*0.25:.6f} {z*size[0]*size[1]*size[2]*0.25:.6f}
'

# Setup system
atoms = atom.Atoms(coords, 'fcc', pbc=True, cell=(3.9, 3.9, 3.9))
calc = EMT(atoms)

# Optimize
opt = LBFGS(atoms, calc, fmax=0.01)
steps = opt.steps
energy = opt.e

# Output results
print(f"Optimization steps: {steps}")
print(f"Final energy: {energy} eV")
