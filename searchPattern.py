class Solution:
    def search(self, pat, txt):
        n, m = len(txt), len(pat)
        if m > n:
            return []
            
        d = 256
        q = 101
        
        h = pow(d, m-1, q)
        
        p_hash, t_hash = 0, 0 
        
        for i in range(m):
            p_hash = (d * p_hash + ord(pat[i])) % q
            t_hash = (d * t_hash + ord(txt[i])) % q
            
        res = []
        
        for i in range(n - m + 1):
            if p_hash == t_hash:
                if txt[i:i+m] == pat:
                    res.append(i)
                    
            if i < n - m:
                t_hash = (d * (t_hash - ord(txt[i]) * h) + ord(txt[i+m])) % q
                if t_hash < 0:
                    t_hash += q
                    
        return res if res else []
