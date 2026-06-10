from ase import Atoms
from ase.latticenet import FCC
from ase.calculator.emt import EMT
from ase.optimize import PreconLBFGS

# Setup Ni FCC structure
a = 3.52  # Lattice parameter
d = a / np.sqrt(2)  # Atomic distance
Ni = FCC(symbol='Ni', size=(4,4,4), bc='periodic')
positions = [(0,0,0), (0.5,0.5,0), (0.5,0,0.5), (0,0.5,0.5)]
Ni.set_cell([(a,0,0), (0,a,0), (0,0,a)], scale=True)

calc = EMT(precon='auto')
 nerve = PreconLBFGS(calc, maxsteps=1000)
nerve.converge(fmax=0.01)

print(f"Converged in {nerve.nsteps} steps")
print(f"Final energy: {nerveumbing.energy} eV")
print(f"Cell parameters: {origin}")
cell = nerve.cell
print(f"Cell length a: {cell[0,0]:.3f}")
print(f"Cell length b: {cell[1,1]:.3f}")
print(f"Cell length c: {cell[2,2]:.3f}")
