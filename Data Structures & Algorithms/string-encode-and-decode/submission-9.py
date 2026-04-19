class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_s=""
        for s in strs:
            enc_s+=str(len(s))+"#"+s
        return enc_s

    def decode(self, s: str) -> List[str]:
        dec_ls=[]
        i=0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            dec_ls.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return dec_ls
            