from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermo import IdealGasThermo

# N2 molecule
mol = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.0977)], calculator=EMT())

# Vibrational frequencies
vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()
vib.clean()

# Gibbs free energy (298.15 K, 1 atm)
ig = IdealGasThermo(vib_energies=freqs,
                    geometry='linear',
                    symmetrynumber=2,
                    atom_numbers=mol.get_atomic_numbers())
G_eV = ig.get_gibbs_energy(T=298.15, P=1e5)

print(f'Gibbs free energy at 298.15 K, 1 atm: {G_eV:.6f} eV')
