#include <iostream>
#include <iomanip>
#include <cmath>

double calculateFunction(double x, double a, double b, double c) {
    double result;
    double cnst = 11;
    double minus = -1;

    _asm {
        finit
        fld x
        fmul st(0), st(0)
        fld a
        fmulp st(1), st(0)
        fstp result

        fld x
        fld cnst
        faddp st(1), st(0)
        fld b
        fdivrp st(1), st(0)
        fld minus
        fmulp st(1), st(0)
        fld c
        faddp st(1), st(0)
        fld result
        faddp st(1), st(0)
        fstp result
    };

    return result;
}

void findRoots(double left, double right, double a, double b, double c, double e) {
    double leftValue = calculateFunction(left, a, b, c);
    double rightValue = calculateFunction(right, a, b, c);

    if (leftValue * rightValue > 0) {
        std::cout << "No roots found in the given interval." << std::endl;
        return;
    }

    if (fabs(right - left) < e) {
        std::cout << "Root: " << std::setprecision(9) << (left + right) / 2.0 << std::endl;
        return;
    }

    double middle = (left + right) / 2.0;
    double middleValue = calculateFunction(middle, a, b, c);

    if (leftValue * middleValue < 0) {
        findRoots(left, middle, a, b, c, e);
    }
    else {
        findRoots(middle, right, a, b, c, e);
    }
}

int main() {
    double left = -10;
    double right = 10;
    double e = 1.00 / pow(10, 9);
    double a, b, c;

    std::cout << "Enter the value of a: ";
    std::cin >> a;

    std::cout << "Enter the value of b: ";
    std::cin >> b;

    std::cout << "Enter the value of c: ";
    std::cin >> c;

    findRoots(left, right, a, b, c, e);

    return 0;
}