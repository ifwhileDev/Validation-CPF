def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


print("-=" * 20)
print("CPF VALIDATION")
print("-=" * 20)
cpf = input('CPF: ')
if cpf_validate(cpf):
    print('This CPF is FALSE.')
else:
    print('This CPF is TRUE.')

