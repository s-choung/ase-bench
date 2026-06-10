from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.utils.eos import EquationOfState
import numpy as np

# Find equilibrium lattice constant using EOS
lattice_constants = np.linspace(3.4, 3.8, 10)
energies = []
for a in lattice_constants:
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    energies.append(cu.get_potential_energy())
eos = EquationOfState(lattice_constants, energies)
a_eq = eos.fit()[0]

# Create (111) 4-layer slab
slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
constraint = FixAtoms(mask=[atom.tag <= 2 for atom in slab])
slab.set_constraint(constraint)

# BFGS relaxation
dyn = BFGS(slab, trajectory=None)
dyn.run(fmax=0.01)

# Print final energy and average z-coordinates
e_final = slab.get_potential_energy()
z_coords = slab.positions[:, 2]
z_avg = [np.mean(z_coords[i*len(slab)//4:(i+1)*len(slab)//4]) for i in range(4)]
print(f"Final energy: {e_final:.6f} eV")
print("Average z-coordinates per layer:", z_avg)
