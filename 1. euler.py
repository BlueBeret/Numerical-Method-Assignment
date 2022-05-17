from math import e,log
# 2. Ulangi menyelesaikan model yang diperoleh dengan menggunakan metode euler dengan
# h=0.01. Bandingkan hasilnya dengan hasil dari penyelesaian analitis.

# Saya selesaikan menggunakan python karena di excel akan memakan banyak baris

# fungsi dqdt
# perubahan konstan
def dqdt(t,Q):
    return 0.75 - 0.03*Q


# batas maksimal error untuk Q
error = 0.0001

# solusi analitis
t_analitis = log(50,e)/0.03
r_analitis = log(50,e) * 100/45


# metode euler
def main():
    # soal pertama, cari T sehingga Q = 25.5
    t = 0
    h = 0.01
    Q0 = 50
    Q = Q0
    while abs(Q-25.5) > error:
        t += h
        Q += h*dqdt(t,Q)
    
    print('T saat Q=25.5 adalah: ')
    print('T \t\t= ', t)
    print('T_analitis \t= ', t_analitis)
    print('='*50)
    print('Error \t\t= ', abs(t-t_analitis)/t_analitis)

    print('\n'*2)

    # Soal kedua, cari r sehingga T = 45, Q0 = 50
    def dQdt(t,Q,r):
        return r/4 - r*Q/100



    h = 0.01
    r = 0
    q0 = 50
    q = q0
    qt = 25.5
    T = 45.0
    error_arr = []
    for _ in range(1000):
        q = q0
        r += h
        t = 0
        while(t < T):
            t += h
            q += h*dQdt(t,q,r)

        error_arr.append(abs(q-qt))

    r = error_arr.index(min(error_arr)) * h + h
    print('r saat T=45 adalah: ')
    print('r \t\t= ', r)
    print('r_analitis \t= ', r_analitis)
    print('='*50)
    print('Error \t\t= ', abs(r-r_analitis)/r_analitis)
    



main()