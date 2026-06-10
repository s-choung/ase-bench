from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.preconlbfgs import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
nsteps = opt.run(fmax=0.01)
energy = atoms.get_potential_energy()
print(f"Steps: {nsteps}, Energy: {energy:.4f} eV, Cell: {atoms.cell.lengths()}")
