# 2. Ulangi menyelesaikan model yang diperoleh dengan menggunakan metode euler dengan
# h=0.01. Bandingkan hasilnya dengan hasil dari penyelesaian analitis.

# Saya selesaikan menggunakan python karena di excel akan memakan banyak baris

# fungsi dqdt
# perubahan konstan

def dqdt(t,Q):
    return 0.75 - 0.03*Q


def main():
    t = 0
    h = 0.01
    Q0 = 50
    Q = Q0
    while abs(Q-25.5) > 1e-3:
        t += h
        Q += h*dqdt(t,Q)
    print(t)

main()