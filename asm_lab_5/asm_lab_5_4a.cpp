#include <iostream>

using namespace std;

int main() {
    float x = 0;
    int a = 0;
    float b = 2 * 3.1415926535;
    int n = 100000;
    float h = (b - a) / n;
    float integralSum = 0;
    float two = 2;

    _asm {
        finit

        mov ecx, n

        loop1:
        fld x
            fmul x; x ^ 2
            fld x
            fsin; sin(x)
            fadd; x ^ 2 + sin(x)
            fld x
            fadd h
            fst x; new x
            fmul 
            fld x
            fsin; sin(x)
            fadd; x ^ 2 + sin(x)
            fadd; (x ^ 2 + sin(x)) + (x ^ 2 + sin(x))
            fmul h; h* ((x ^ 2 + sin(x)) + (x ^ 2 + sin(x))) / 2
            fdiv two
            fadd integralSum; добавляем к сумме
            fstp integralSum

            fld x; загружаем x
            fadd h; добавляем h
            fstp x; сохраняем новое значение x

            loop loop1
    }

    cout << integralSum;
    return 0;
}