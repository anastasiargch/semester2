
// (4 * x - 1) * (4 * x + 1) / 4;

#include <iostream>

int main() {
	int x;
	std::cin >> x;
	int result;
	int result_c;

	_asm {
		mov eax, x
		imul eax, 4
		sub eax, 1;

		mov ebx, x
		imul ebx, 4
		add ebx, 1;

		imul eax, ebx
		mov ecx, 4
		cdq
		idiv ecx
		mov result, eax;
	}
	result_c = (4 * x - 1) * (4 * x + 1) / 4;

	std::cout << "Result by assembler : " << result << '\n';
	std::cout << "Result by c++ : " << result_c << '\n';
}