from ase import bulk
from ase.calculators.emt import EMT
from ase.constraints import ExpCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', cubic=True)
atoms.calc = EMT()
ecf = ExpCellFilter(atoms)
opt = PreconLBFGS(ecf, precon='auto')
opt.run(fmax=0.01)
steps = opt.nsteps
energy = atoms.get_potential_energy()
a = atoms.get_cell_lengths_and_angles()[0]
print(f"Steps: {steps}")
print(f"Energy: {energy:.6f}")
print(f"Lattice constant: {a:.6f}")
