[org 07c00h]

[bits 16]
	cli

	lgdt [gdtDescriptor]
	
	mov eax, cr0
	or eax, 1
	mov cr0, eax

	jmp gdt_codeSeg:start32
	
[bits 32]
start32:
	xor eax, eax
	mov ax, gdt_dataSeg
	mov ds, ax
	mov es, ax
	mov fs,	ax
	mov gs, ax

	mov ebp, 0x90000
	mov esp, ebp


BEGIN_ProtMod:
	mov ebx, message
	mov edi, vmSeg

print_string_pm_loop:
	mov al, [ebx]
	mov ah, color

	cmp al, 0
	je done

	mov [edi], ax

	add ebx, 1 
	add edi, 2

	jmp print_string_pm_loop


done:
	mov eax, cr0
	and al, 0xfe
	mov cr0, eax

	sti

	jmp $
	
gdt_start:
gdt_null:
	dd 0x0
	dd 0x0

gdt_code:
	dw 0xffff
	dw 0x0
	db 0x0
	db 10011010b
	db 11001111b
	db 0x0

gdt_data:
	dw 0xffff 
	dw 0x0 
	db 0x0 
	db 10010010b 
	db 11001111b 
	db 0x0 
gdt_end:

gdtDescriptor:
	dw gdt_end - gdt_start - 1
	dd gdt_start
	
	message db "Protected Mode", 0
	gdt_codeSeg equ gdt_code - gdt_start
	gdt_dataSeg equ gdt_data - gdt_start
	vmSeg equ 0b8000h
	color equ 0fh

	times 510 - ($-$$) db 0
	dw 0aa55h
