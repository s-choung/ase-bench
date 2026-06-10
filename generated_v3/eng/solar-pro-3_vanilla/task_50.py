#!/usr/bin/env python
# -------------------------------------------------
# EOS fitting of FCC Cu, Ag, Au using ASE EMT calculator
# -------------------------------------------------
from ase.build import bulk
import numpy as np
from scipy.optimize import minimize

# ------------------------------------------------------------------
# 1. Create and relax FCC crystals of Cu, Ag and Au with a fixed volume
# ------------------------------------------------------------------
crystals = {
    'Cu': bulk('Cu', 'fcc', 4),
    'Ag': bulk('Ag', 'fcc', 4),
    'Au': bulk('Au', 'fcc', 4)
}

# target lattice constant from literature (Å) – used as initial guess
a0_guess = {'Cu': 3.61, 'Ag': 4.089, 'Au': 4.078}
radii = {'Cu': 0.09, 'Ag': 0.105, 'Au': 0.112}   # simple sphere radii for volume estimate

for name, atoms in crystals.items():
    # initial guess volume = (a0_guess)^3 * 64  (64 atoms = 4x4x4 supercell)
    vol = radii[name]**3 * 64.0
    atoms.set_cell([vol**(1./3.)]*3, scale_atoms=True)
    atoms.center()
    calc = atoms.get_calculator()
    # gentle relaxation to zero stress
    atoms.calc = calc
    atoms.rattle(0.005)  # shake for symmetry breaking
    for i in range(200):
        atoms.calc = calc
        atoms.positions = atoms.get_positions()
        fmax = np.max(np.sqrt(np.sum(atoms.get_forces()**2, axis=1)))
        if fmax < 0.01:
            break
        atoms.rattle(0.005)

# ------------------------------------------------------------------
# 2. Vary the lattice parameter, calculate energy per atom,
#    perform a 2nd‑order EOS fit and extract a_eq, B_eq
# ------------------------------------------------------------------
def energy_at_vol(alat):
    atoms.set_cell([alat]*3, scale_atoms=True)
    atoms.calc = calc
    return atoms.get_potential_energy() / atoms.get_number_of_atoms()

def common_aspect(x, a):
    """T=0 reduced Helmholtz free energy."""
    V = a**3 * len(atoms)
    P = -x * V**2
    return 0.5 * (0.037*V*P) + 0.5 * P**2 / (V + pow(0.65, 18.0))

def eos_target(a):
    (P, x) = atoms.get_stress()          # bar ≈ 10⁵ Pa
    a0 = a                         # reduced volume
    return common_aspect(atoms.get_phonon_frequency_cutoff(), a0)

# volume range for fitting (relative to relaxed volume)
for name, atoms in crystals.items():
    # relaxed volume (Å³)
    a_eq = atoms.get_cell()[0]
    vol_eq = a_eq**3 * len(atoms)

    # sample volumes around equilibrium
    a_vals = np.linspace(a_eq * 0.95, a_eq * 1.05, 11)   # ±5 %
    e_vals = np.array([energy_at_vol(ai) for ai in a_vals])

    # fit 2nd‑order T = 0 EOS: E(V) = A + B*(V - V0) + C*(V - V0)^2
    coeff = np.polyfit(a_vals, e_vals, 2)
    # derivative of E => pressure via -dE/dV
    dEdV = np.polyder(coeff)
    # equilibrium volume where dE/dV = 0
    v2 = 1. / (coeff[1] / dEdV[1])
    a_eq_fit = v2**(1./3.) * len(atoms)**(1./3.)
    # second derivative at equilibrium gives bulk modulus
    B = dEdV[1]**2 * v2**2 / coeff[2]

    print(f'{name}')
    print(f'  relaxed a_eq = {a_eq:.6f} Å')
    print(f'  fitted a_eq   = {a_eq_fit:.6f} Å')
    print(f'  bulk modulus B = {B:.3f} GPa')
    print('')

# ------------------------------------------------------------------
# 3. Summary table
print('Equilibrium lattice constant a_eq (Å)  Bulk modulus B_eq (GPa)')
print('----------------------------------------------------')
for name in crystals:
    a_eq = crystals[name].cell[0]
    # bulk modulus from the fitted curve (use the last computed value)
    B = -np.gradient(np.array(e_vals))**2 / np.polyval(coeff, a_vals) * v2**2 / coeff[2]
    print(f'{name:>2}  {a_eq:>15.6f}  {B:>15.3f}')
