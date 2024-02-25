// Для натурального числа n выяснить, входит ли цифра 3 в запись числа n^2

#include <iostream>

int main() {
	int n;
	std:: cin >> n;

	bool has3 = false;

	_asm {
		mov eax, n
		imul eax, n

		check_f:
		cmp eax, 0      //проверяем, есть ли цифры
		je end_check    //если нет, завершаем проверку

		mov edx, eax    
		mov ecx, 10    

		cdq
		div ecx         //eax = eax / ecx, edx = eax % ecx

		cmp edx, 3      //сравниваем остаток с 3
		je found_3      //если равно 3, переходим к found_3

		jmp check_f     //продолжаем проверку следующей цифры

		found_3:
		mov has3, 1     //устанавливаем флаг has3 в true
		jmp end_check   

		end_check:
	}

	if (has3) {
		std::cout << "The number 3 is included in the number " << n << "^2" << '\n';
	} else {
		std::cout << "The number 3 is not included in the number " << n << "^2" << '\n';
	}

	return 0;
}
