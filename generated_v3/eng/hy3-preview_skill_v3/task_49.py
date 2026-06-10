import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# 1. Find equilibrium lattice constant using EOS
def find_equilibrium_lattice():
    # Test range around typical Cu lattice constant
    a0 = 3.6  # Initial guess for Cu
    cell = bulk('Cu', 'fcc', a=a0).get_cell()
    
    volumes = []
    energies = []
    
    # Vary lattice constant by scaling
    for scale in np.linspace(0.95, 1.05, 11):
        atoms = bulk('Cu', 'fcc', a=a0 * scale)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    # Fit Equation of State
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    # Calculate lattice constant from equilibrium volume
    # For FCC: volume = a^3 / 4 (conventional cell has 4 atoms)
    a_eq = (v0 * 4)**(1/3)
    return a_eq

# Get equilibrium lattice constant
a_eq = find_equilibrium_lattice()
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")

# 2. Create (111) 4-layer slab
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)

# 3. Set up calculator
slab.calc = EMT()

# 4. Fix bottom 2 layers
# Identify layers by z-coordinate
z_positions = slab.get_positions()[:, 2]
unique_z = np.unique(np.round(z_positions, decimals=4))
unique_z = sorted(unique_z)

# Fix atoms in the two lowest layers
constraint = FixAtoms(indices=[i for i, z in enumerate(z_positions) 
                              if z < unique_z[1] + 0.1])  # Small tolerance
slab.set_constraint(constraint)

# 5. Run BFGS relaxation
opt = BFGS(slab, trajectory='slab_relaxation.traj')
opt.run(fmax=0.05)

# 6. Print results
print(f"\nFinal energy: {slab.get_potential_energy():.4f} eV")

# Calculate average z-coordinate for each layer
z_positions = slab.get_positions()[:, 2]
unique_z = np.unique(np.round(z_positions, decimals=4))
unique_z = sorted(unique_z)

print("\nAverage z-coordinate for each layer:")
for i, z_layer in enumerate(unique_z):
    # Find atoms in this layer (with tolerance)
    mask = np.abs(z_positions - z_layer) < 0.1
    layer_atoms = slab[mask]
    avg_z = np.mean(layer_atoms.get_positions()[:, 2])
    print(f"Layer {i+1}: {avg_z:.4f} Å ({len(layer_atoms)} atoms)")
