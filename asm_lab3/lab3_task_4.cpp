#include <iostream>

int main() {
    int num, denom, nod;

    std::cout << "Enter a numerator: ";
    std::cin >> num;

    std::cout << "Enter a denominator: ";
    std::cin >> denom;

    _asm {
        mov eax, num
        mov ebx, denom
        cmp eax, ebx
        je _1
    f_nod:
        cmp ebx, 0
        jz nod_done

        xor edx, edx
        div ebx

        mov eax, ebx
        mov ebx, edx

        jmp f_nod

    nod_done:
        mov nod, eax

        mov eax, num
        cdq
        idiv nod
        mov num, eax
        mov eax, denom
        cdq
        idiv nod
        mov denom, eax
        jmp _end

    _1:
        mov num, 1
        mov denom, 1

    _end:
    }
    std::cout << "Simplified fraction: " << num << "/" << denom << std::endl;
    return 0;
}