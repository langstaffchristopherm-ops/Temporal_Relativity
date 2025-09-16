# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Christopher M. Langstaff

#!/usr/bin/env python3
import numpy as np, pandas as pd, matplotlib.pyplot as plt

import json, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA, FIGS, RUNS = ROOT/'data', ROOT/'figs', ROOT/'runs'
for p in (DATA, FIGS, RUNS): p.mkdir(exist_ok=True, parents=True)
STAMP=datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%SZ')
RUN_DIR=RUNS/STAMP; RUN_DATA=RUN_DIR/'data'; RUN_FIGS=RUN_DIR/'figs'
RUN_DATA.mkdir(parents=True, exist_ok=True); RUN_FIGS.mkdir(parents=True, exist_ok=True)
def dual_save_csv(df,name): df.to_csv(DATA/name,index=False); df.to_csv(RUN_DATA/name,index=False)
def dual_save_fig(plt,name,dpi=160): plt.tight_layout(); plt.savefig(FIGS/name,dpi=dpi); plt.savefig(RUN_FIGS/name,dpi=dpi)

materials=[
    ('Copper',397.48,116.0,385.0,8940.0,'Thermtest + Wikipedia α'),
    ('Aluminum',225.94,97.0,897.0,2700.0,'Thermtest + Wikipedia α'),
    ('Stainless304',14.644,3.68,502.0,7920.0,'Thermtest'),
    ('Ice',2.092,0.54,2050.0,917.0,'Thermtest'),
]
def main():
    rows=[]
    for name,k,alpha_mm2_s,cp,rho,src in materials:
        alpha=alpha_mm2_s*1e-6; k_pred=rho*cp*alpha; rel=(k_pred-k)/k
        rows.append({'material':name,'k_W_mK':k,'alpha_mm2_s':alpha_mm2_s,'cp_J_kgK':cp,'rho_kg_m3':rho,'k_pred_W_mK':k_pred,'rel_error':rel,'source':src})
    df=pd.DataFrame(rows); dual_save_csv(df,'materials_thermo.csv')
    plt.figure(); plt.scatter(df['k_W_mK'],df['k_pred_W_mK'])
    mx=1.1*max(df['k_W_mK'].max(),df['k_pred_W_mK'].max()); plt.plot([0,mx],[0,mx],'--')
    for _,r in df.iterrows(): plt.annotate(r['material'],(r['k_W_mK'],r['k_pred_W_mK']),xytext=(5,5),textcoords='offset points',fontsize=8)
    plt.xlabel('Tabulated k (W/m·K)'); plt.ylabel('Predicted k = ρ c_p α (W/m·K)'); plt.title('Thermal consistency')
    dual_save_fig(plt,'fig_k_vs_pred.png',dpi=160)
if __name__=='__main__': main()
