import numpy as np
from common import *

def run():
    x,y,cx,cy,tx,ty=classification(29)
    w=fit(x,y);scores=np.where(cy==1,1-probability(cx,w),probability(cx,w));alpha=.1
    rank=min(len(scores),int(np.ceil((len(scores)+1)*(1-alpha))));q=float(np.sort(scores)[rank-1])
    def assess(z,labels):
        p=probability(z,w);sets=np.c_[p<=q,1-p<=q];covered=sets[np.arange(len(labels)),labels.astype(int)]
        return {'coverage':float(covered.mean()),'mean_set_size':float(sets.sum(axis=1).mean()),'empty_sets':int(sum(sets.sum(axis=1)==0)),'cases':len(z)}
    # Shift the label-generating mechanism while keeping observed features fixed.
    shifted=(tx[:,0]-.9*tx[:,1]+1.8>0).astype(float)
    return {'alpha':alpha,'calibration_quantile':q,'iid':assess(tx,ty),'concept_shift':assess(tx,shifted),
            'checks':[check(len(scores)==200,'Disjoint calibration records'),check(0<=q<=1,'Valid finite-sample quantile')],
            'scope':'Synthetic split-conformal binary prediction sets. Exchangeability assumptions do not hold for the concept-shift slice.'}
