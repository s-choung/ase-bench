from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms, trajectory='n2_opt.traj')
opt.run(fmax=0.001)

print(f"Optimized bond length: {atoms.get_distance(0, 1):.4f} Å")
print(f"Potential energy: {atoms.get_potential_energy():.6f} eV")

vib = Vibrations(atoms, name='n2_vib')
vib.run()
vib.summary()

freqs = vib.get_frequencies()
print(f"\nAll frequencies (cm⁻¹): {freqs}")

vib_energies = vib.get_energies()
print(f"All vib energies (eV): {vib_energies}")

real_vib_energies = vib_energies[np.isreal(vib_energies)].real
real_vib_energies = real_vib_energies[real_vib_energies > 0.01]
print(f"\nReal positive vib energies used for thermo (eV): {real_vib_energies}")

potentialenergy = atoms.get_potential_energy()

thermo = IdealGasThermo(
    vib_energies=real_vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0,
    potentialenergy=potentialenergy,
)

T = 298.15
P = 101325.0

print(f"\n{'='*50}")
print(f"Thermochemistry at T={T} K, P={P} Pa (1 atm)")
print(f"{'='*50}")

H = thermo.get_enthalpy(temperature=T)
S = thermo.get_entropy(temperature=T, pressure=P)
G = thermo.get_gibbs_energy(temperature=T, pressure=P)

print(f"Enthalpy H        : {H:.6f} eV")
print(f"Entropy S         : {S:.6f} eV/K")
print(f"T*S               : {T*S:.6f} eV")
print(f"Gibbs free energy : {G:.6f} eV")
print(f"Gibbs free energy : {G * 96.485:.4f} kJ/mol")

vib.clean()
