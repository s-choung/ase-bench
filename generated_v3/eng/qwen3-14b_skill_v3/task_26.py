from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc')
atoms.calc = EMT()
atoms = FrechetCellFilter(atoms)
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy()} eV")
cell = atoms.get_cell_lengths_and_angles()
print(f"Cell: a={cell[0]:.2f} b={cell[1]:.2f} c={cell[2]:.2f} α={cell[3]:.2f} β={cell[4]:.2f} γ={cell[5]:.2f}")
