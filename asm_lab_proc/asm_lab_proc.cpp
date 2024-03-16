#include <iostream>

extern "C" int procedure(int);

int main() {

	int x;
	std::cout << "Enter x: ";
	std:: cin >> x;

	std::cout << "Result by c++ : " << (4 * x - 1) * (4 * x + 1) / 4 << '\n';
	std::cout << "Result by assembler : " << procedure(x) << '\n';
	
	return 0;
}
