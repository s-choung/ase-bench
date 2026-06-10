from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
import numpy as np

# 1. Calculate Equilibrium Lattice Constant using EOS
a_values = np.linspace(3.0, 4.0, 10)
energies = []
volumes = []
for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    energies.append(energy)
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
a_eq, _, B = eos.fit()
print(f"Equilibrium lattice constant: {a_eq:.4f} Angstroms")

# 2. Create (111) Slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=a_eq)

# 3. Attach EMT and Constraints
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag < 3 for a in slab]))  # Fix bottom 2 layers

# 4. Surface Relaxation
dyn = BFGS(slab, trajectory='Cu_slab_relaxation.traj')
dyn.run(fmax=0.02)

# 5. Print Final Energy and Average Z-Coordinate for Each Layer
print(f"Final Energy: {slab.get_potential_energy():.6f} eV")
num_layers = 4
z_coords = []
for i in range(num_layers):
    layer_indices = [atom.tag == i + 1 for atom in slab]
    layer_z = [atom.z for atom in slab if layer_indices[slab.atoms.index(atom)]]
    avg_z = np.mean(layer_z)
    z_coords.append(avg_z)
    print(f"Layer {i + 1} Average Z: {avg_z:.4f} Angstroms")
