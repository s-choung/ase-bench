"""Compute deterministic reference facts for ASE-Bench tasks by actually
building each structure with ASE (and running EMT where the observable is
deterministic). Output feeds judge_rubrics_50.json and correctness_check SPEC.

Per task entry:
  {"facts": {...} | "alts": [{...}, ...], "notes": "...", "sanity": "..."}
- "facts"/"alts": numbers computed HERE (not guessed). alts = defensible
  alternative builds (e.g. primitive vs conventional cell).
- "sanity": for tasks whose exact numbers depend on model choices (slab size,
  MD randomness) — the physically checkable boundary instead.
Tasks not listed at all have no deterministic component (pure-stochastic MD).

Run:  conda run -n base python reference_facts.py
Out:  results_v3/reference_facts.json
"""
import json
import os
import tempfile

import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "results_v3", "reference_facts.json")

# vib/opt caches go to a scratch dir, not the benchmark dir
os.chdir(tempfile.mkdtemp(prefix="asebench_ref_"))

from ase import Atoms
from ase.build import (bulk, surface, add_vacuum, molecule, fcc111, fcc100,
                       bcc110, mx2, nanotube, add_adsorbate)
from ase.cluster import Octahedron, Icosahedron
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units


def r(x, nd=4):
    return round(float(x), nd)


def eos_fit(sym, struct="fcc", a=None, npts=7, span=0.05, eos_type="birchmurnaghan"):
    at0 = bulk(sym, struct, a=a) if a else bulk(sym, struct)
    cell0 = at0.get_cell()
    vols, ens = [], []
    for s in np.linspace(1 - span, 1 + span, npts):
        at = at0.copy()
        at.set_cell(cell0 * s, scale_atoms=True)
        at.calc = EMT()
        vols.append(at.get_volume())
        ens.append(at.get_potential_energy())
    eos = EquationOfState(vols, ens, eos=eos_type)
    v0, e0, B = eos.fit()
    n = len(at0)
    a0 = (v0 / n * 4) ** (1 / 3)  # fcc conventional a from per-atom volume
    return {"v0_per_atom": r(v0 / n), "a0_fcc": r(a0), "B_GPa": r(B / units.GPa, 1),
            "e0": r(e0)}


def vib_freqs(at, name):
    at.calc = EMT()
    vib = Vibrations(at, name=name)
    vib.run()
    en = vib.get_energies()  # complex eV
    cm = [r(e.real / units.invcm, 1) for e in en if abs(e.imag) < 1e-8 and e.real / units.invcm > 50]
    vib.clean()
    return cm  # real frequencies above 50 cm^-1 (drops numeric-zero trans/rot)


F = {}

# ---------------- structures (exact counts / formulas / cells) ----------------
prim = bulk("Cu", "fcc", a=3.6).repeat((2, 2, 2))
conv = bulk("Cu", "fcc", a=3.6, cubic=True).repeat((2, 2, 2))
F["T01"] = {"alts": [{"n_atoms": len(prim), "formula": prim.get_chemical_formula()},
                     {"n_atoms": len(conv), "formula": conv.get_chemical_formula()}],
            "notes": "primitive 8 / conventional 32 both defensible; default a=3.61"}

F["T02"] = {"sanity": "slab (a x b x 4 layers) + CO(2) -> n_atoms = 4k+2 for integer k>=1; "
                      "must print n_atoms; vacuum 10 set",
            "notes": "size free -> count not unique; common: (2,2,4)+CO=18, (3,3,4)+CO=38"}

m = mx2("MoS2")
add_vacuum(m, 10.0)
F["T03"] = {"facts": {"n_atoms": len(m), "a": r(m.cell.lengths()[0], 3),
                      "c_min": 10.0},
            "notes": "mx2 default a=3.18; prompt asks CELL SIZE only (audit: don't require atom count); "
                     "c >= 10 after vacuum"}

h2o = molecule("H2O")
h2o.calc = EMT()
e_before = h2o.get_potential_energy()
BFGS(h2o, logfile=None).run(fmax=0.01)
F["T04"] = {"facts": {"e_before": r(e_before), "e_after": r(h2o.get_potential_energy())},
            "notes": "EMT H2O single-point then BFGS; e_after depends weakly on fmax "
                     "(0.01-0.05 all ~same to 0.01 eV); both energies must be printed, e_after <= e_before"}

F["T05"] = {"facts": eos_fit("Cu", "fcc"), "notes": "EOS Cu fcc EMT; eq volume per atom + B; "
            "any eos type ok -> B within ~10 GPa; prompt asks eq volume + bulk modulus"}

F["T06"] = {"sanity": "Langevin 300K 100 steps x 5fs on Cu 2x2x2; initial/final T and E printed; "
                      "final T in (50, 900) K plausible band; no nan"}
F["T07"] = {"sanity": "NVE 50 steps; initial/final TOTAL energy printed; |dE| < 0.1 eV "
                      "(EMT Cu NVE conserves ~1e-2)"}

F["T08"] = {"facts": {"freqs_cm": vib_freqs(molecule("N2"), "vib_n2")},
            "notes": "EMT N2 stretch; trans/rot near-zero or imaginary modes are NORMAL output "
                     "(audit lesson: do not penalize)"}

cu1 = bulk("Cu", "fcc")
F["T09"] = {"alts": [{"n_atoms": 1}, {"n_atoms": 4}],
            "facts": {"a_prim_len": r(cu1.cell.lengths()[0], 3)},
            "notes": "POSCAR roundtrip; prim 1 atom / cubic 4 atoms; cell params must survive roundtrip"}

F["T10"] = {"facts": {"n_atoms": len(Octahedron("Cu", 5)), "pos_shape": [85, 3]},
            "notes": "Octahedron(Cu, length=5) = 85 atoms; positions shape (85,3)"}

al = bulk("Al", "bcc", a=3.3, cubic=True)
F["T11"] = {"facts": {"n_atoms": len(al), "formula": al.get_chemical_formula(),
                      "cell_edge": 3.3},
            "notes": "Al bcc cubic = 2 atoms Al2, cell 3.3"}

ti = bulk("Ti", "hcp", a=2.95, c=2.95 * 1.59)
F["T12"] = {"facts": {"n_atoms": len(ti), "a": 2.95, "c": r(2.95 * 1.59, 4)},
            "notes": "Ti hcp a=2.95 c/a=1.59 -> c=4.6905; prompt asks cell vectors + positions "
                     "(audit: count not required, but 2 atoms if printed)"}

si_c = bulk("Si", "diamond", a=5.43, cubic=True).repeat((3, 3, 3))
si_p = bulk("Si", "diamond", a=5.43).repeat((3, 3, 3))
F["T13"] = {"alts": [{"n_atoms": len(si_c), "volume": r(si_c.get_volume(), 2)},
                     {"n_atoms": len(si_p), "volume": r(si_p.get_volume(), 2)}],
            "notes": "diamond 3x3x3: conv 216 atoms V=4322.78 / prim 54 atoms V=1080.70"}

from ase.spacegroup import crystal
nacl = crystal(["Na", "Cl"], [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225,
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
F["T14"] = {"facts": {"n_atoms": len(nacl), "formula": nacl.get_chemical_formula()},
            "notes": "sg225 NaCl = 8 atoms (Na4Cl4); symbols Na+Cl printed"}

s15 = fcc100("Cu", size=(3, 3, 3), vacuum=12.0)
F["T15"] = {"facts": {"n_atoms": len(s15)}, "notes": "fcc100 Cu (3,3,3) = 27 atoms"}

s16 = bcc110("Fe", size=(2, 2, 4), vacuum=10.0)
F["T16"] = {"alts": [{"n_atoms": len(s16)}, {"n_atoms": 2 * len(s16)}],
            "notes": "bcc110 Fe (2,2,4) = 16 atoms (32 if doubled cell variant)"}

# T17 probe (ase 3.27): surface("Cu",(2,1,1),3) string-lattice = 12 atoms and a
# ZERO third cell vector; add_vacuum() then yields a NAN cell row - that is ASE
# behavior under literal prompt compliance, NOT a model bug. surface(bulk(...))
# primitive form = 3 atoms with a clean cell; cubic bulk = 12 atoms clean.
s17a = surface("Cu", (2, 1, 1), 3)
s17b = surface(bulk("Cu", "fcc", a=3.6), (2, 1, 1), 3)
F["T17"] = {"alts": [{"n_atoms": len(s17a)}, {"n_atoms": len(s17b)}],
            "notes": "12 atoms (string lattice / cubic bulk) or 3 atoms (primitive bulk) both valid; "
                     "nan in printed cell can come from ASE itself (string form + add_vacuum) -> "
                     "do NOT auto-fail nan here; v1 judged 17 models 0 for nan = likely unfair"}

ch4 = molecule("CH4")
d_ch = r(ch4.get_distance(0, 1), 3)
F["T18"] = {"facts": {"formula": "CH4", "n_atoms": 5, "d_CH": d_ch},
            "notes": "G2 CH4; C-H = 1.087-1.094 depending on print; prompt asks coords+bonds+formula"}

F["T19"] = {"facts": {"d_CO": 1.16, "d_OO": 2.32},
            "notes": "manual CO2; get_distances must show 1.16 and 2.32 (tol 0.03)"}

cnt = nanotube(6, 6, length=4)
F["T20"] = {"alts": [{"n_atoms": len(cnt)}, {"n_atoms": 144}, {"n_atoms": 240}],
            "notes": "(6,6) CNT length=4 = 96 atoms; length convention varies in the wild"}

ico = Icosahedron("Au", noshells=3)
F["T21"] = {"facts": {"n_atoms": len(ico), "com": [r(x, 2) for x in ico.get_center_of_mass()]},
            "notes": "Icosahedron(Au,3) = 55 atoms; COM ~= geometric center"}

F["T22"] = {"sanity": "Al(111) a x b x 3 slab + N2(2) -> n_atoms = 3k+2; atom types Al and N printed",
            "notes": "common: (2,2,3)+2=14, (3,3,3)+2=29"}

F["T23"] = {"sanity": "three single-point EMT energies (ontop/bridge/fcc) printed + explicit "
                      "lowest-site statement; energies differ; no relaxation required by prompt",
            "notes": "site heights are model's choice -> winner not pinned; judge checks 3 energies + comparison"}

au = bulk("Au", "fcc")
au.calc = EMT()
e_au = au.get_potential_energy()
au4 = bulk("Au", "fcc", cubic=True)
au4.calc = EMT()
F["T24"] = {"alts": [{"e_final": r(e_au)}, {"e_final": r(au4.get_potential_energy())}],
            "notes": "bulk Au is already at symmetry minimum -> LBFGS converges in 0-2 steps; "
                     "e ~= single-point (prim vs cubic x4); steps + final energy printed"}

cu25 = bulk("Cu", "fcc")
cu25.calc = EMT()
opt = BFGS(FrechetCellFilter(cu25), logfile=None)
opt.run(fmax=0.01)
a_eq = r((cu25.get_volume() * 4) ** (1 / 3), 3)
F["T25"] = {"facts": {"a_eq_fcc": a_eq, "e_per_atom": r(cu25.get_potential_energy() / len(cu25))},
            "notes": "EMT Cu eq lattice ~3.589; cell+energy before/after printed; e_after <= e_before"}

ni = bulk("Ni", "fcc")
ni.calc = EMT()
BFGS(FrechetCellFilter(ni), logfile=None).run(fmax=0.01)
F["T26"] = {"facts": {"a_eq_fcc": r((ni.get_volume() * 4) ** (1 / 3), 3),
                      "e_per_atom": r(ni.get_potential_energy() / len(ni))},
            "notes": "PreconLBFGS on Ni; positions-only opt keeps a=3.52, cell-opt -> ~3.53 (EMT); "
                     "steps + energy + cell printed (reference computed with cell filter)"}

F["T27"] = {"sanity": "Bussi NVT 500K Ag 2x2x2, 200 steps; T printed every 50 steps (>=4 values); "
                      "T values in (100, 1200) K; no nan"}
F["T28"] = {"sanity": "Langevin ramp 300->600K; T printed every 50 steps; set_temperature used; "
                      "T trend upward overall (final window > initial window)"}
F["T29"] = {"sanity": "NVE Pd 2fs 200 steps; |E_end - E_start| printed and < 0.1 eV"}
F["T30"] = {"sanity": "NPTBerendsen 300K 1bar Cu 3x3x3; initial/final volume AND pressure printed; "
                      "volume change modest (<20%); no nan"}
F["T31"] = {"sanity": "NPTBerendsen 500K 10GPa Al; GPa->eV/A^3 conversion present in code; "
                      "final volume < initial volume (10 GPa compresses); both volumes printed"}

F["T32"] = {"facts": {"freqs_cm": vib_freqs(molecule("H2O"), "vib_h2o")},
            "notes": "EMT H2O real modes; cm^-1 AND eV both required by prompt; "
                     "near-zero/imag trans-rot modes are normal"}

ch4o = molecule("CH4")
ch4o.calc = EMT()
BFGS(ch4o, logfile=None).run(fmax=0.01)
F["T33"] = {"facts": {"freqs_cm": vib_freqs(ch4o, "vib_ch4")},
            "notes": "CH4: optimize THEN vibrations; only real freqs printed (filtering is the task)"}

F["T34"] = {"sanity": "NEB 5 images, IDPP; barrier = E_max - E_initial printed; "
                      "0 < barrier < 1.0 eV plausible for EMT Cu(111) adatom (typically ~0.02-0.2)",
            "notes": "exact barrier depends on slab size/relaxation -> band, not point"}
F["T35"] = {"sanity": "3-image NEB, manual Al endpoints, linear interpolation; "
                      "3 image energies printed; middle image energy >= endpoint energies (it's a barrier)"}

F["T36"] = {"facts": eos_fit("Ag", "fcc", eos_type="birchmurnaghan"),
            "notes": "Ag EOS 7pts +/-5% Birch-Murnaghan; eq lattice constant + B in GPa printed"}

n2 = molecule("N2")
n2.calc = EMT()
e_n2 = n2.get_potential_energy()
vib = Vibrations(n2, name="vib_n2_t37")
vib.run()
thermo = IdealGasThermo(vib_energies=vib.get_energies(), potentialenergy=e_n2,
                        atoms=n2, geometry="linear", symmetrynumber=2, spin=0)
g_with = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0, verbose=False)
thermo0 = IdealGasThermo(vib_energies=vib.get_energies(), potentialenergy=0.0,
                         atoms=n2, geometry="linear", symmetrynumber=2, spin=0)
g_zero = thermo0.get_gibbs_energy(temperature=298.15, pressure=101325.0, verbose=False)
vib.clean()
F["T37"] = {"alts": [{"G_eV": r(g_with)}, {"G_eV": r(g_zero)}],
            "notes": "IdealGasThermo N2 298.15K 1atm; with/without potentialenergy both defensible; "
                     "tol 0.05 eV (vib detail differences)"}

F["T38"] = {"sanity": "HarmonicThermo Helmholtz at 300K printed in eV; uses REAL vib energies of a "
                      "Cu bulk (setup size is model's choice); no crash on imaginary modes",
            "notes": "value depends on chosen cell -> not pinned"}

F["T39"] = {"alts": [{"n_atoms": 1}, {"n_atoms": 4}],
            "notes": "Au xyz roundtrip; symbols all Au; positions preserved (plain xyz drops cell - fine)"}

F["T40"] = {"alts": [{"n_atoms": 8}, {"n_atoms": 2}],
            "facts": {"spacegroup_sub": "225"},
            "notes": "NaCl CIF roundtrip: 8 atoms, but CIF read may return 2-atom primitive "
                     "(audit lesson); spacegroup info (225 / Fm-3m) printed"}

F["T41"] = {"sanity": "trajectory written during 10-step MD then read back; frame count printed and "
                      "consistent with save interval (10 or 11 typical); last-frame energy printed (finite)"}

ems = {}
for sym in ["Cu", "Ag", "Au"]:
    b = bulk(sym, "fcc")
    b.calc = EMT()
    ems[sym] = r(b.get_potential_energy())
F["T42"] = {"facts": {"e_singlepoint_prim": ems},
            "notes": "db with Cu/Ag/Au EMT energies; per-atom singlepoint at default a "
                     "(x4 if cubic, lower if optimized) - judge checks 3 formulas + 3 finite energies queried back"}

F["T43"] = {"sanity": "db stores 2/3/4-layer Cu slabs with layers key; select(layers=3) returns the "
                      "3-layer one; printed n_atoms divisible by 3 and consistent with that slab"}

F["T44"] = {"sanity": "FixAtoms via tags on bottom 2 of 4 layers; printed before/after coords of FIXED "
                      "atoms must be IDENTICAL (max delta ~0); moved-instead-of-fixed = 0",
            "notes": "v1 truncation case: full stdout now visible; tag direction errors flip which layers move"}

h2 = Atoms("H2", positions=[[0, 0, 0], [0, 0, 0.9]])
h2.calc = EMT()
F["T45"] = {"facts": {"d_fixed": 0.9, "e_at_0.9": r(h2.get_potential_energy())},
            "notes": "FixBondLength 0.9; bond stays 0.9 (tol 0.01) wherever opt/dynamics applied; "
                     "energy printed"}

F["T46"] = {"facts": {"d_CO_molecule": r(molecule("CO").get_distance(0, 1), 3)},
            "sanity": "both constraints applied; final C-O distance == initial CO bond (~1.13-1.15, "
                      "FixBondLength preserves it); final energy printed",
            "notes": "slab size free -> energy not pinned; d(C-O) is the anchor"}

F["T47"] = {"facts": {"avg_cn": 12.0},
            "notes": "Cu fcc 3x3x3 NeighborList natural_cutoffs -> avg CN 12 (tol 0.3)"}

cu2p = bulk("Cu", "fcc").repeat((2, 2, 2))
cu2c = bulk("Cu", "fcc", cubic=True).repeat((2, 2, 2))
def minmax_mic(at):
    d = at.get_all_distances(mic=True)[0][1:]
    return r(d.min(), 3), r(d.max(), 3)
p_min, p_max = minmax_mic(cu2p)
c_min, c_max = minmax_mic(cu2c)
F["T48"] = {"alts": [{"d_min": p_min, "d_max": p_max}, {"d_min": c_min, "d_max": c_max}],
            "notes": "Cu 2x2x2 mic distances from atom 0; prim vs cubic builds differ; tol 0.05"}

F["T49"] = {"facts": {"a_eq_fcc": a_eq},
            "sanity": "EOS eq lattice ~3.58-3.62 used for fcc111 4-layer slab; bottom 2 fixed; "
                      "final energy + per-layer avg z printed (4 distinct layer z values)",
            "notes": "slab energy depends on size -> a_eq is the anchor"}

F["T50"] = {"facts": {"Cu": eos_fit("Cu", "fcc"), "Ag": eos_fit("Ag", "fcc"),
                      "Au": eos_fit("Au", "fcc")},
            "notes": "three-metal EOS table: eq lattice + B per metal; B tol ~12 GPa "
                     "(point grid / eos-type differences)"}

with open(OUT, "w") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
print(f"wrote {OUT} ({len(F)} tasks)")
for tid in sorted(F, key=lambda t: int(t[1:])):
    e = F[tid]
    kind = "facts" if "facts" in e else ("alts" if "alts" in e else "sanity")
    print(f"{tid}: {kind:6s} {json.dumps(e.get('facts') or e.get('alts') or e.get('sanity'), ensure_ascii=False)[:110]}")
