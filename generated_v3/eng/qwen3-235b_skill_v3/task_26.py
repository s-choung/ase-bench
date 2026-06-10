from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = bulk('Ni', 'fcc')
atoms.calc = EMT()
opt = PreconLBFGS(atoms, trajectory='opt.traj', precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {len(opt) - 1}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters: {atoms.get_cell_lengths_and_angles()}")
