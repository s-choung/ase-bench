import ase
from ase.build import bulk, slab
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# Find equilibrium lattice constant
lattice_consts = [3.4 + 0.1 * i for i in range(5)]
volumes, energies = [], []

for a in lattice_consts:
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_energy())

eos = EquationOfState(volumes, energies)
v0, e0 = eos.fit()
a_eq = v0 ** (1/3)

# Create (111) slab with equilibrium lattice constant
slab_atoms = slab('Cu', 'fcc', a=a_eq, Miller=(1,1,1), layers=4, vacuum=10.0)
slab_atoms.calc = EMT()

# Fix bottom 2 layers
z_coords = [atom.z for atom in slab_atoms]
sorted_indices = sorted(range(len(z_coords)), key=lambda i: z_coords[i])
constraint = FixAtoms(indices=sorted_indices[:2])
slab_atoms.set_constraint(constraint)

# Run BFGS optimization
dyn = BFGS(slab_atoms)
dyn.run(fmax=0.01)

# Print results
print(f"Final energy: {slab_atoms.get_energy()}")
z = [atom.z for atom in slab_atoms]
layer_avg = [sum(z[i::4])/len(z[i::4]) for i in range(4)]
print("Layer avg z-coordinates:", layer_avg)
