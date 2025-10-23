Temporal Relativity (ΔS = Δτ)

The canonical archive is DOI: 10.5281/zenodo.17119049
This release (version DOI): 10.5281/zenodo.17420538
Git: https://github.com/langstaffchristopherm-ops/Temporal_Relativity Version: v2.0.0

LaTeX sources for the Planck-Cell S/t Framework papers — a series of manuscripts exploring the discrete-tick construction of space, time, and physical law.

Sections

Each paper follows a modular layout under other_tex/, assembled via main.tex:
Abstract — concise summary of claims and results.
Introduction — motivation, context, and relation to prior works.
Notation — tick-based units, entropy conventions, and symbol list.
Scope and Falsifiers — domain of applicability and up-front tests.
Results / Derivations — main theorems, relations, and proofs.
Discussion — physical interpretation and comparison to conventional theory.
Zenodo Links — cross-references to companion papers and datasets.
Acknowledgements — credits and institutional notes.

Related Zenodo Records

Temporal Relativity — The Entropy Clock — https://doi.org/10.5281/zenodo.17119049  
Planck-Cell Kinematics — https://doi.org/10.5281/zenodo.17168478  
Planck-Cell Mass — https://doi.org/10.5281/zenodo.17209646  
Planck-Cell Gravity — https://doi.org/10.5281/zenodo.17210232  
Planck-Cell Thermodynamics — https://doi.org/10.5281/zenodo.17211721  
Planck-Cell Electromagnetics — https://doi.org/10.5281/zenodo.17217107  
Planck-Cell Expansion — https://doi.org/10.5281/zenodo.17216181

Build

To compile the PDF from source:
latexmk -pdf -interaction=nonstopmode main.tex

Requires a standard TeX Live or MiKTeX installation with latexmk enabled.

License
Creative Commons CC BY 4.0 (see LICENSE).  
© 2025 Christopher M. Langstaff
