from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Calculate equilibrium lattice constant with EOS
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    atoms = cu_bulk.copy()
    atoms.set_cell(cu_bulk.get_cell() * scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, _, _ = eos.fit()
a0 = v0 ** (1/3)  # Cubic cell equilibrium lattice constant

# Create 4-layer Cu(111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=a0)
# Fix bottom 2 layers
slab.set_constraint(FixAtoms(mask=[atom.tag <= 2 for atom in slab]))
# Attach calculator and relax
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
final_energy = slab.get_potential_energy()
print(f"\nFinal total energy: {final_energy:.3f} eV")
for layer_tag in range(1, 5):
    z_coords = [atom.position[2] for atom in slab if atom.tag == layer_tag]
    avg_z = sum(z_coords) / len(z_coords)
    print(f"Layer {layer_tag} average z-coordinate: {avg_z:.3f} Å")
