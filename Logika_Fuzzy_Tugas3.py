import numpy as np
import math
import matplotlib.pyplot as plt


def linear_naik(a, b, x):
    if x < a:
        return 0
    elif x >= a and x <= b:
        return (x - a) / (b - a)
    else:
        return 1


def linear_turun(a, b, x):
    if x < a:
        return 1
    elif x >= a and x <= b:
        return (b - x) / (b - a)
    else:
        return 0


def segitiga(a, b, x):
    if x <= a:
        return 0
    elif x > a and x <= (a+b)/2:
        return 2*((x-a)/(b-a))**2
    elif x > (a+b)/2 and x < b:
        return 1-2*((x-b)/(b-a))**2
    else:
        return 1


def trapesium(a, b, c, d, x):
    if x <= a:
        return 0
    elif x > a and x <= b:
        return (x-a)/(b-a)
    elif x > b and x <= c:
        return 1
    elif x > c and x <= d:
        return (d-x)/(d-c)
    else:
        return 0


def sigmoid_pertumbuhan(a, b, x):
    y = 1 / (1 + math.exp(-a * (x - b)))
    return y


def sigmoid_penyusutan(a, b, x):
    y = 1 / (1 + math.exp(-a * (b - x)))
    return y


def gauss(x, a, b):
    return np.exp(-(x-a)**2/(2*b**2))


def beta(x, a, b):
    return x**(a-1)*(1-x)**(b-1)


def main():
    while True:
        judul="Fungsi Derajat Keanggotaan Dalam Logika Fuzzy".center(20,"*")
        print(f"""\r\n{judul}\r\n
        1. Linear
        2. Segitiga
        3. Trapesium
        4. Sigmoid
        5. Gauss
        6. Beta 
        7. Keluar
        """)

        menu = int(input("Masukkan pilihan Anda : "))

        if menu == 1:
            print("1. Linear Naik")
            print("2. Linear Turun")
            pilih = int(input("Masukkan pilihan Anda : "))

            if pilih == 1:
                a = float(input("Masukkan nilai a\t: "))
                b = float(input("Masukkan nilai b\t: "))
                x = float(input("Masukkan nilai x\t: "))
                y = linear_naik(a, b, x)
                print(
                    f"Nilai keanggotaan pada Linear Naik dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")
                plt.plot([a, b], [0, 1], 'b--', lw=2)
                plt.ylim(-0.1, 1.1)
                plt.title('Grafik Linear Naik Untuk Fungsi Keanggotaan X')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="cyan")
                plt.show()

            elif pilih == 2:
                a = float(input("Masukkan nilai a\t: "))
                b = float(input("Masukkan nilai b\t: "))
                x = float(input("Masukkan nilai x\t: "))
                y = linear_turun(a, b, x)
                print(
                    f"Nilai keanggotaan pada Linear Turun dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")
                plt.plot([a, b], [1, 0], 'b--', lw=2)
                plt.ylim(-0.1, 1.1)
                plt.title('Grafik Linear Turun Untuk Fungsi Keanggotaan X')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="cyan")
                plt.show()
                
            else:
                print("Pilihan yang anda masukkan tidak valid...")

        elif menu == 2:
            a = float(input("Masukkan nilai a\t: "))
            b = float(input("Masukkan nilai b\t: "))
            x = float(input("Masukkan nilai x\t: "))
            y = segitiga(a, b, x)
            print(
                    f"Nilai keanggotaan pada Grafik Segitiga dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")
            plt.plot([a, (a+b)/2, b], [0, 1, 0], 'b--', lw=2)
            plt.ylim(-0.1, 1.1)
            plt.title('Grafik Segitiga Untuk Fungsi Keanggotaan X')
            plt.xlabel('Nilai x')
            plt.ylabel('Nilai y')
            plt.plot([x], [y], marker='o', markersize=8, color="cyan")
            plt.show()

        elif menu == 3:
            a = float(input("Masukkan nilai a\t: "))
            b = float(input("Masukkan nilai b\t: "))
            c = float(input("Masukkan nilai c\t: "))
            d = float(input("Masukkan nilai d\t: "))
            x = float(input("Masukkan nilai x\t: "))
            y = trapesium(a, b, c, d, x)
            print(
                    f"Nilai keanggotaan pada Grafik Trapesium dengan a={a}, b={b}, c={c}, d={d}, dan x={x} adalah {y:.3f}")
            plt.plot([a, b, c, d], [0, 1, 1, 0], 'b--', lw=2)
            plt.ylim(-0.1, 1.1)
            plt.title('Grafik Trapesium Untuk Fungsi Keanggotaan X')
            plt.xlabel('Nilai x')
            plt.ylabel('Nilai y')
            plt.plot([x], [y], marker='o', markersize=8, color="cyan")
            plt.show()

        elif menu == 4:
            print("1. Kurva Sigmoid Pertumbuhan")
            print("2. Kurva Sigmoid Penyusutan")
            pilih = int(input("Masukkan pilihan Anda : "))

            if pilih == 1:
                a = float(input("Masukkan nilai a\t: "))
                b = float(input("Masukkan nilai b\t: "))
                x = float(input("Masukkan nilai x\t: "))
                y = sigmoid_pertumbuhan(a, b, x)
                print(
                    f"Nilai keanggotaan pada Sigmoid Pertumbuhan dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")

                plt.plot([a, b], [0, 1], 'b--', lw=2)
                xs = [i/10 for i in range(-100, 100)]
                ys = [sigmoid_pertumbuhan(a, b, x) for x in xs]
                plt.plot(xs, ys)
                plt.ylim(-0.1, 1.1)
                plt.title('Grafik Kurva Sigmoid Pertumbuhan Untuk Fungsi Keanggotaan X')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="cyan")
                plt.show()

            elif pilih == 2:
                a = float(input("Masukkan nilai a\t: "))
                b = float(input("Masukkan nilai b\t: "))
                x = float(input("Masukkan nilai x\t: "))
                y = sigmoid_penyusutan(a, b, x)
                print(
                    f"Nilai keanggotaan pada Sigmoid Penyusutan dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")

                plt.plot([a, b], [0, 1], 'b--', lw=2)
                xs = [i/10 for i in range(-100, 100)]
                ys = [sigmoid_penyusutan(a, b, x) for x in xs]
                plt.plot(xs, ys)
                plt.ylim(-0.1, 1.1)
                plt.title('Grafik Kurva Sigmoid Penyusutan Untuk Fungsi Keanggotaan X')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="cyan")
                plt.show()
            
            else: 
                print("Pilihan yang anda masukkan tidak valid...")

        elif menu == 5:
            a = float(input('Masukkan nilai a\t: '))
            b = float(input('Masukkan nilai b\t: '))
            x = np.linspace(-10, 10, 1000)
            y = gauss(x, a, b)
            plt.plot(x, y)
            plt.title(f'Grafik Gaus dengan a={a} dan b={b}')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()

        elif menu == 6:
            a = float(input('Masukkan nilai a\t: '))
            b = float(input('Masukkan nilai b\t: '))
            x = np.linspace(0, 1, 1000)
            y = beta(x, a, b)
            plt.plot(x, y)
            plt.title(f'Grafik Beta dengan a={a} dan b={b}')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()

        elif menu == 7:
            print("Keluar...")
            break

        else:
            print("Pilihan yang Anda masukkan tidak valid. Silahkan coba lagi.....")


if __name__ == '__main__':
    main()
