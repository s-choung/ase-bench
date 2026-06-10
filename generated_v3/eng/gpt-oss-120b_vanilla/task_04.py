from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# H2O geometry (Angstrom)
mol = Atoms('OH2',
            positions=[[0, 0, 0],
                       [0.9572, 0, 0],
                       [-0.2399872, 0.927297, 0]],
            calculator=EMT())

# Energy before optimization
e_initial = mol.get_potential_energy()
print(f'Initial energy: {e_initial:.6f} eV')

# Optimize geometry
opt = BFGS(mol, logfile=None)
opt.run(fmax=0.01)

# Energy after optimization
e_final = mol.get_potential_energy()
print(f'Final energy:   {e_final:.6f} eV')
