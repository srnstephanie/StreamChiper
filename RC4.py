# Memodifikasi RC4 dan menggabungkannya dengan Extended Vigenere Cipher/Play 
# Cipher berarti memodifikasi prosedur KSA atau PRGA di dalam RC4 dan 
# mengabungkannya dengan konsep Extended Vgenere Cipher. Anda dapat membuat 
# fungsi permutasi yang lebih kompleks, menambahkan LFSR, dll.


# RC4
# KSA
# Inisialisasi Larik S  


def KSA(Key):
    S = []
    for i in range (0, 256):
        S.append(i)

    # pengacakan (permutasi) nilai-nilai di dalam larik S berdasarkan kunci rahasia K
    j = 0
    for i in range(0, 256):
        j =(j + S[i] + Key[i% len(Key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

# PRGA
def PGRA(S, P):
    i = 0
    j = 0
    C = ''
    for idx, m in enumerate(P):
        i = (i+1)%256
        j = (j+S[i])%256
        S[i], S[j] = S[j], S[i]
        t = (S[i]+S[j])%256
        u = S[t]
        x = LSFR(S, u)
        c = m ^ x
        C += chr(c)
    return C

def LSFR(S, u):
    x = S.pop()
    out = x^u
    S.append(S[254])
    for i in range(254, 0):
        S[i] = S[i-1]
    S[0] = out
    return x
    
def enkrip(P, Key):
    C = enkripdekrip(P, Key)
    finaloutput = ''
    for i in range(len(C)):
        Key += Key[i]
    for i in range(len(C)):
        finaloutput += chr((ord(C[i])+ord(Key[i]))%256 )
    return finaloutput

def dekrip(P, Key):
    finalinput = ''
    SKey = Key
    for i in range(len(P)):
        Key += Key[i]
    for i in range(len(P)):
        finalinput += chr((ord(P[i])-ord(Key[i]))%256 )
    C = enkripdekrip(finalinput, SKey)
    return C

def enkripdekrip(P, Key):
    P = [ord(char) for char in P]
    SKey = [ord(char) for char in Key]
    S = KSA(SKey)
    C = PGRA(S, P)
    return C





