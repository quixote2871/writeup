from output import *
from Crypto.Util.number import inverse, long_to_bytes

class RSA:
    def __init__(self, N, e, p):
        self.N = N
        self.e = e
        self.p = p
        self.q = self.N//p
    
    def decrypto(self, FLAG_enc):
        self._d = inverse(self.e, (self.p-1)*(self.q-1))
        return long_to_bytes(pow(FLAG_enc, self._d, self.N))

p1 = 122925338396977892377812264658939951801210314312238212067059595148447406166769716855936119104014353481162826500622396956338370238037713303129667973570418205129792800094492802512333202767609745542480301632710243676880179931490273979269048908687034938065216226244568368994455058377505090061149006930577060428653

rsa1 = RSA(N1, e, p1)
rsa2 = RSA(N2, e, 2*p1+1)

FLAG_origin = rsa1.decrypto(FLAG1_enc)+rsa2.decrypto(FLAG2_enc)

print(FLAG_origin.decode())
