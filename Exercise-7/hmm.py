
from math import log
from collections import defaultdict

class S:
    def __init__(self, prob, prev, out):
        self.prob = prob
        self.prev = prev
        self.out = out

class HMM:
    def __init__(self, femit, ftrans):
        self._femit = femit
        self._femit_totals = {key : sum(value.values()) for key, value in femit.items()}
        self._ftrans = ftrans
        self._ftrans_totals = {key : sum(value.values()) for key, value in ftrans.items()}
        self._lexicon = { word for words in femit.values() for word in words }
        
        self._n = sum(self._femit_totals.values())
        self._v = len(self._lexicon)

        # Count of each tag
        self._ct = defaultdict(int)
        self._sing_tt = defaultdict(int)
        for t1, values in ftrans.items():
            for t2, count in values.items():
                if count == 1:
                    self._sing_tt[t1] += 1
                self._ct[t2] += count
        self._t_unsmoothed = {t : count/self._n for t, count in self._ct.items()}
        
        # Count of each word
        self._cw = defaultdict(int)
        self._sing_tw = defaultdict(int)
        for t, values in femit.items():
            for w, count in values.items():
                if count == 1:
                    self._sing_tw[t] += 1
                self._cw[w] += count
        self._w_addone = {w : (count+1)/(self._n + self._v) for w, count in self._cw.items()}
    
    @property
    def states(self):
        return (state for state in self._femit if state not in ('START', 'END'))
    
    def P_emit(self, y, o):
        lam = 1 + self._sing_tw[y]
        return (self._femit[y][o] + lam*self._w_addone.get(o, 1/(self._n + self._v)))/(self._ct[y] + lam)
        # return self._femit[y][o]/self._femit_totals[y]
    
    def P_trans(self, x, y):
        lam = 1 + self._sing_tt[x]
        return (self._ftrans[x][y] + lam*self._t_unsmoothed[y])/(self._ct[x] + lam)
        # return self._ftrans[x][y]/self._ftrans_totals[x]
    
    def maxprob(self, D, state, obs):
        def prob(prev, pemit = self.P_emit(state, obs)):
            return D[prev].prob * self.P_trans(prev, state) * pemit
        prev = max(D, key=prob)
        return S(prob(prev), prev, obs)
    
    def decode(self, observations):
        V = [ { 'START': S(1.0, None, '') } ]
        
        for obs in observations:
            V.append({ state : self.maxprob(V[-1], state, obs) for state in self.states })
        
        last = self.maxprob(V[-1], 'END', '')
        
        state = last.prev
        path = []
        
        for D in reversed(V[1:]):
            path.append((D[state].out, state))
            state = D[state].prev
        
        return (last.prob, path[::-1])
