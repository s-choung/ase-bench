from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Define isolated CH4 molecule
mol = Atoms('CH4',
            positions=[[0.0, 0.0, 0.0],
                      [0.0, 0.0, 1.097],
                      [0.0, 1.097, 0.5485],
                      [1.097, 0.0, 0.5485],
                      [0.5485, 1.097, 0.5485]],
            cell=[[2.0, 0.0, 0.0],
                  [0.0, 2.0, 0.0],
                  [0.0, 0.0, 2.0]],
            pbc=False)

mol.calc = EMT()

# Geometry optimization
opt = BFGS(mol, trajectory='ch4_opt.traj')
opt.run(fmax=0.01)

print('Optimized geometry:')
print(mol)
print('Forces:', mol.get_forces())

# Compute vibrational frequencies
mol.phonon_calc = EMT()
freqs = mol.get_phonon_frequencies(method='GV')

real = [f for f in freqs if f < 0.0]
print('Real vibrational frequencies (cm^-1):', real)
