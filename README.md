# Temporal Relativity (ΔS = Δτ)

The canonical archive is DOI: 10.5281/zenodo.17119049  
This release (version DOI): 10.5281/zenodo.17421413  
Git: https://github.com/langstaffchristopherm-ops/Temporal_Relativity (commit abc1234). Version: v2.0.2  

LaTeX sources for the Planck-Cell S/t framework article introducing the temporal–entropic postulate ΔS = Δτ and the one-hop-per-tick causal substrate from which metric relations, energy, and inertia emerge.

## Sections
Each paper follows a modular layout under other_tex/, assembled via main.tex:
- Abstract — concise summary of claims and results  
- Introduction — motivation, context, and relation to prior works  
- Notation — tick-based units, entropy conventions, and symbol list  
- Scope and Falsifiability — domain of applicability and pre-registered tests  
- Results / Derivations — main postulates, relations, and proofs  
- Discussion — interpretation and empirical correspondence  
- Zenodo Links — cross-references to companion papers and datasets  
- Acknowledgements — credits and institutional notes  

## Related Zenodo Records
- Temporal Relativity — https://doi.org/10.5281/zenodo.17119049  
- Planck-Cell Kinematics — https://doi.org/10.5281/zenodo.17168478  
- Planck-Cell Mass — https://doi.org/10.5281/zenodo.17209646  
- Planck-Cell Gravity — https://doi.org/10.5281/zenodo.17210232  
- Planck-Cell Thermodynamics — https://doi.org/10.5281/zenodo.17211721  
- Planck-Cell Electromagnetics — https://doi.org/10.5281/zenodo.17217107  
- Planck-Cell Expansion — https://doi.org/10.5281/zenodo.17216181  

## Build
To compile the PDF from source:
```bash
latexmk -pdf -interaction=nonstopmode main.tex
