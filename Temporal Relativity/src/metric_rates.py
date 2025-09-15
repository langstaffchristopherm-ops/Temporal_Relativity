#!/usr/bin/env python3
import numpy as np, pandas as pd, matplotlib.pyplot as plt, networkx as nx
from scipy.spatial import cKDTree

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

rng = np.random.default_rng(42)
def sample_points(N): return rng.random((N,3))
def knn_graph(X,k=12):
    tree=cKDTree(X); G=nx.Graph(); G.add_nodes_from(range(len(X)))
    for i in range(len(X)):
        d,idx=tree.query(X[i],k+1)
        for j in idx[1:]:
            w=np.linalg.norm(X[i]-X[j]); G.add_edge(i,j,weight=w)
    return G
def interior_mask(X,margin=0.1):
    import numpy as np; return np.all((X>margin)&(X<1-margin),axis=1)
def est_dist(X,G,n_pairs=400,margin=0.1):
    import numpy as np
    mask=interior_mask(X,margin); idx=np.where(mask)[0]
    if len(idx)<2: return float('nan')
    pairs=rng.choice(idx,size=(n_pairs,2),replace=True); vals=[]
    for a,b in pairs:
        if a==b: continue
        try: dG=nx.shortest_path_length(G,a,b,weight='weight')
        except nx.NetworkXNoPath: continue
        dE=np.linalg.norm(X[a]-X[b]); 
        if dE==0: continue
        vals.append(abs(dG-dE)/dE)
    return float(np.mean(vals)) if vals else float('nan')
def main():
    Ns=[400,800,1600]; rows=[]
    for N in Ns:
        X=sample_points(N); G=knn_graph(X,k=12); md=est_dist(X,G)
        rows.append({'N':N,'mean_distortion':md})
    df=pd.DataFrame(rows); dual_save_csv(df,'metric_rates.csv')
    plt.figure(); plt.loglog(df['N'],df['mean_distortion'],marker='o')
    N0, d0 = df['N'].iloc[0], df['mean_distortion'].iloc[0]
    ref = d0*(df['N']/N0)**(-1/3); plt.loglog(df['N'],ref,'--')
    plt.xlabel('N'); plt.ylabel('mean rel. distortion'); plt.title('Metric recovery vs N')
    dual_save_fig(plt,'fig_metric_rates.png',dpi=160)
if __name__=='__main__': main()
