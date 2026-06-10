import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.build import surface
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# 1. Calculate equilibrium lattice constant via EOS
calc = EMT()
atoms = bulk('Cu', 'fcc', a=3.6, crystalstructure=None)
atoms.calc = calc

# Generate lattice constants and energies for EOS
lattices = np.linspace(3.5, 3.8, 10)
energies = []
for a in lattices:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = calc
    energies.append(atoms.get_energy())

# Fit EOS and get equilibrium lattice constant
eos = EquationOfState(lattices, energies)
v0, e0, B = eos.fit()
a0 = (v0) ** (1.0/3.0)
print(f"Equilibrium lattice constant: {a0:.3f} Å")

# 2. Create (111) 4-layer slab
slab = surface('Cu', (1,1,1), layers=4, vacuum=10.0, a=a0, periodic=True)
slab.calc = calc

# 3. Fix bottom 2 layers (atoms with z < median z)
z_coords = slab.get_positions()[:, 2]
z_median = np.median(z_coords)
constraint = FixAtoms(indices=[i for i, z in enumerate(z_coords) if z < z_median])
slab.set_constraint(constraint)

# 4. BFGS relaxation
dyn = BFGS(slab, logfile=None)
dyn.run(fmax=0.05)

# 5. Print results
print(f"\nFinal energy: {slab.get_energy():.4f} eV")
layer_indices = np.round(slab.get_positions()[:, 2] / a0 * np.sqrt(6)/3).astype(int)
for layer in np.unique(layer_indices):
    mask = layer_indices == layer
    avg_z = np.mean(z_coords[mask])
    print(f"Layer {layer}: average z = {avg_z:.3f} Å")
