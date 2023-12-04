print('Informe seu nome:');
nome = input();
print('Informe sua idade:');
age = input();
confirm = '';
while confirm.lower() != 'yes':
    print('Você é: '+nome+' de '+age+' anos? (Yes/No)');
    confirm = input();
    if confirm.lower() == 'yes':
        print('Cadastro Concluído!');
    elif confirm.lower() == 'no': 
        print('Ok! Informe seu nome novamente:');
        nome = input();
        print('Informe sua idade novamente:');
        age = input();
