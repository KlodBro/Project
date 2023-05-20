
q0 = 0.001
rH = 0.05
rb = 0.01
h = 1
vi = 0.006
ro = 900
rom = 1500
g = 9.81
w = 2000
n = 5
sy = 99
s3 = 87

cy = []
x = []
ri1 = []

dro = 1

c1 = [15, 5, 35, 40, 5]
d = []
d3 = []
s1 = sum(c1)
for i in range(1, n + 1):
    d2 = 35e-06 + 5e-06 * (i-1)
    d1 = (0.8e-06) * i
    dmk = (1e+06) * d1
    d.append(round(d2*1000000))
    d3.append(dmk)
#     print(d2)
# print()
# # print(s1)
# print(d3)
# print(dmk)


c = []
cpr = []
for i in range(n):
    c2 = round((c1[i] / s1)*100)
    cpr1 = 100 * c2
    c.append(c2)
    cpr.append(cpr1)
# print(c)
# print(cpr)

rec = 0


def op_en(sy, cy, x, ri1, rec, h, d3):
    qob = q0 * (1 + rec)
    # print('qob', qob)
    vc = round(qob / (3.14 * (rH ** 2 - rb ** 2)), 8)
    # print(vc)
    sq = 0.001
    a = -0.25 * (rH ** 2 - rb ** 2) / ((rH ** 4 - rb ** 4) / 8 - rH ** 2 * (rH ** 2 - rb ** 2) / 4 - rb * (rH ** 3 - rb ** 3) / 3 + rH * rb * (rH ** 2 - rb ** 2) / 2)  # 1124.999999999999
    print(a)
    vb = round(a*vc*(rH ** 2 - rb ** 2 + 2 * rb * (rb - rH)), 8)
    print(vb)
    vqc = 0
    vbo = round(vb / vc, 8)
    print(vbo)
    drq = (rH - rb) / (1000 * rH)
    print(drq)
    for i in range(1, 1001):
        roq = round(1 - drq * (i-1) - drq / 2, 4)
        print(roq)
        rq = round(roq * rH, 5)
        print(rq)
        vq = a * vc * (1 - roq ** 2 + 2 * (rb / rH) * (roq - 1)) * rH ** 2
        print(vq)
        sq = sq + 6.28 * rq * vq * drq * rH
        print('sq',sq)
        print('q0',q0)
        if sq > q0:
            vqc = sq / (3.14 * (rH ** 2 - rq ** 2))
            print(vqc)
            print()
            print("zashel")
        print(sq)
        print(q0) #norm
        print()

    tqc = round(h / vqc)
    tc = h / vc
    ktc = round(tqc / tc)
    krc = (rH - rq)/(rH - rb)

    vH = q0 / (3.14 * (rH + rq) * h)
    Frq = w ** 2 * (rH + rq) / (2 * g)
    LaH = vH ** 3 * ro ** 2 / (g * Frq * vi * abs(rom - ro))
    a0 = 1000
    b0 = 0

    La = 0
    j1 = 0

    while True:
        Ar = (a0 + b0)/2
        # print(Ar)
        j1 += 1
        # print(j1)
        La = Ar ** 2 / (18 + 0.61 * Ar ** 0.5) ** 3
        # print(La)
        dLa = La - LaH
        # print(dLa)
        dot = dLa / LaH
        dot1 = abs(dot)
        if dot1 < 0.0001:
            ArH = Ar
            # print(ArH)
            break
        elif La < LaH:
            b0 = Ar
        else:
            a0 = Ar

    ArH = round(ArH, 10)
    # print(ArH)
    ReH = ArH / (18 + 0.61 * ArH ** 0.5)
    dH = ReH * vi / (ro * vH)
    # print(dH)
    # print()
    dHmk = 1e06 * dH
    # print(dHmk)

    for i in range(len(cpr)):
        for j in range(1, n+1):
            if any(k > dH for k in d):
                xi = 1
                ri = rq
                cyi = cpr[i]
                sy += cyi
                cy.append(cyi)
                x.append(xi)
                # print(1)
            else:
                Ari = ArH * (d[i] / dH)**3
                Rei = Ari / (18 + 0.61 * Ari ** 0.5)
                voi = (Rei * vi) / (d[i] * ro)
                ri = rH - voi * (rH - rq)/vH
                xi = (rH - ri)/(rH-rq)
                cyi = cpr[i] * xi
                sy += cyi
                cy.append(cyi)
                x.append(xi)
                # print(0)
    cyi //= 100

    # x.append(xi)
    ri1.append(round(ri, 5))

    print(vb)
    print(tqc)  
    print(tc)
    print(ktc)  # верно
    # print('cy,%',cy)
    print()
    print('ReH', ReH)
    print('dH', dH)
    qr = qob - q0
    Re = 2 * qob * ro / (3.14 * rH * vi)

    # global a

    return a, vc, ri, cy, x, dH


'''
Заполнение данными первой таблицы
'''

if sy > s3:
    dro = (rH-rb)/(10*rH)
else:
    rec += 0.5
if rec > 5.1:
    dro = (rH-rb)/(10*rH)
else:
    op_en(sy, cy, x, ri1, rec, h, d3)

a = 1
vc = 1
for i in range(1, 12):
    rot = 1 - (i-1) * dro
    rt = rot * rH
    vot = a * (1 - rot ** 2 + 2 * (rb/rH) * (rot - 1)) * rH ** 2
    vt = vc * vot
    # print('rot', rot)
    # print('rt', rt)
    # print('vot', vot)
    # print('vt', vt)
    # print()


'''
Заполнение данными второй таблицы
'''
print('d,mk =', d)  # верно
print('c,% =', c)  # верно
print('cy,%',cy)
print('xi',x)
print('sy',sy)
# print('cy,% =', cy)
# print('x =', x)
# print('ri,m =', ri1)
# print()
# print(sy)
# print(rec)
# # print(gr)
# # print(rg)
# # print(Re)
# print()

# print(rt)
# print(vt)
# print(rot)
# print(vot)
# print()
