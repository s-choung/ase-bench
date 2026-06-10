from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.units import invcm, h, c, eV

# N2 molecule (approx. bond length 1.10 Å)
n2 = Atoms("N2", positions=[[0, 0, 0], [0, 0, 1.10]])
n2.set_calculator(EMT())

# Vibrational analysis
vib = Vibrations(n2, name="n2")
vib.run()                     # displacements, forces, frequencies
freqs_cm = vib.get_frequencies()          # cm⁻¹
vib_energies = freqs_cm * invcm * h * c / eV   # convert to eV per mode
vib.clean()                    # remove temporary files

# Ideal‑gas thermochemistry (linear, symmetry number 2)
thermo = IdealGasThermo(vib_energies=vib_energies,
                       symmetrynumber=2,
                       geometry="linear")
G_J_mol = thermo.get_gibbs_energy(temperature=298.15,
                                  pressure=101325)   # J mol⁻¹

print(f"Gibbs free energy at 298.15 K, 1 atm: {G_J_mol/1000:.3f} kJ mol⁻¹")
