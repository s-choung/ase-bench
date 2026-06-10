from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Initial setup
a_values = [3.4, 3.5, 3.6, 3.7, 3.8]  # trial lattice constants
energies = []

# Equilibrium lattice constant search
for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(a_values, energies)
a_eq = eos.fit()[0]

# Create (111) slab
slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)

# Attach EMT calculator
slab.calc = EMT()

# Fix the bottom 2 layers
c = FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < slab.positions[:, 2].mean()])
slab.set_constraint(c)

# Relaxation
relax = BFGS(slab)
relax.run(fmax=0.01)

# Print final energy and average z-coordinate for each layer
print("Final energy:", slab.get_potential_energy())
z_layers = slab.positions[:, 2].reshape((4, -1)).mean(axis=1)
for i, z in enumerate(z_layers):
    print(f"Layer {i+1} average z-coordinate: {z}")
