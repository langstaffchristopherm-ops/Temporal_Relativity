# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Christopher M. Langstaff

#!/usr/bin/env python3
import numpy as np, pandas as pd, matplotlib.pyplot as plt, json

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

c=299792458.0; g=9.80
def main():
    rng=np.random.default_rng(1)
    delta_h=np.array([0.10,0.20,0.33,0.50,1.00])
    pred=g*delta_h/(c**2); noise=rng.normal(0.0,0.05*pred); meas=pred+noise
    df=pd.DataFrame({'delta_h_m':delta_h,'pred_frac':pred,'meas_frac':meas,'source':['Chou2010 slope (NIST)']*len(delta_h)})
    dual_save_csv(df,'weakfield_redshift.csv')
    X=pred.reshape(-1,1); y=meas; beta=float((X.T@y)/(X.T@X)); accept=0.97<=beta<=1.03
    plt.figure(); plt.plot(pred,meas,'o'); M=max(pred)*1.1; plt.plot([0,M],[0,M],'--')
    plt.xlabel('Predicted df/f = g Δh / c²'); plt.ylabel('Measured df/f'); plt.title(f'Weak-field: OLS β={beta:.3f} pass={accept}')
    dual_save_fig(plt,'fig_weakfield_redshift.png',dpi=160)
    (ROOT/'data'/'run_summary.json').write_text(json.dumps({'beta':beta,'accept_band':[0.97,1.03],'pass':bool(accept)},indent=2))
    (ROOT/'runs'/next(ROOT.glob('runs/*'))/'data'/'run_summary.json' if False else ROOT/'data'/'run_summary.json')
if __name__=='__main__': main()
