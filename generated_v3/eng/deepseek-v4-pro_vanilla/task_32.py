from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import invcm

def main():
    # Build water molecule and assign EMT calculator
    atoms = molecule('H2O')
    atoms.calc = EMT()

    # Relax the structure
    opt = BFGS(atoms)
    opt.run(fmax=0.01)

    # Compute vibrational frequencies using finite differences
    vib = Vibrations(atoms, delta=0.01)
    vib.run()
    frequencies = vib.get_frequencies()  # harmonic energies in eV

    # Output results
    print("Vibrational mode frequencies for H2O (EMT):")
    for i, energy in enumerate(frequencies):
        freq_cm = energy / invcm  # convert eV to cm^-1
        if energy > 1e-3:
            print(f"Mode {i+1}: {energy:.6f} eV, {freq_cm:.2f} cm^-1")
        else:
            print(f"Mode {i+1} (translation/rotation): {energy:.6f} eV, {freq_cm:.2f} cm^-1")

if __name__ == "__main__":
    main()
