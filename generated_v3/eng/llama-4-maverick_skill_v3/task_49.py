import numpy as np
from ase import Atoms, units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS

# EOS fitting to find equilibrium lattice constant
atoms = bulk('Cu', 'fcc', a=3.5)
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 * 4) ** (1/3)  # lattice constant for FCC

# Create (111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(1,1,4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
mask = [atom.tag >= 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Run BFGS relaxation
opt = BFGS(slab, trajectory='relax.traj')
opt.run(fmax=0.01)

# Print final energy and average z-coordinate for each layer
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
for layer in range(4):
    z_avg = np.mean([atom.z for atom in slab if atom.tag == layer + 1])
    print(f"Layer {layer+1}: z_avg = {z_avg:.4f} Å")
