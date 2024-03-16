; (4 * x – 1) * (4 * x + 1) / 4

.686P
.model flat, c
.code

procedure		proc x:dword
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
		ret
procedure		endp
end