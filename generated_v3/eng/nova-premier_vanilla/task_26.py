from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = Atoms('Ni', cell=[3.52, 3.52, 3.52], pbc=True)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto', logfile=None)
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Energy: {atoms.get_potential_energy():.3f} eV")
print("Cell:", atoms.get_cell_lengths_and_angles())
