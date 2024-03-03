// а^12+а^8+а

#include <iostream>

int main() {
	int a, res;
	std::cin >> a;

	_asm {
		mov eax, a
		mov ecx, 11

	term1:
		imul a
		loop term1

		
		mov ebx, eax
		mov eax, a
		mov ecx, 7

	term2:
		imul a
		loop term2

		add ebx, eax
		add ebx, a
		mov res, ebx 
	}

	std:: cout << "a^12 + a^8 + a = " << '\n';
	std:: cout << "asm: " << res << '\n';
	std:: cout << "C++: " << pow(a, 12) + pow(a, 8) + a ;
	return 0;
}
