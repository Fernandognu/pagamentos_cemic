import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

# PERGUNTAS #
perguntaNomeFavorecido = "Quem deseja pagar? "
perguntaBancoFavorecido = "Qual o Banco? "
perguntaContaCorrente = "Conta Corrente? "
perguntaAgencia = "Agencia? "
perguntaValorTotal = "Qual o valor total? "

# VARIAVEIS #
nomeFavorecido = input(perguntaNomeFavorecido)
bancoFavorecido = input(perguntaBancoFavorecido)
agenciaFavorecido = input(perguntaAgencia)
contaFavorecido = input(perguntaContaCorrente)

# VALOR #
valorTotal =  float(input(perguntaValorTotal))
valorForamatado = locale.currency(valorTotal, grouping=True, symbol=False)

print("Voce deseja pagar", nomeFavorecido, "o valor de R$", valorForamatado, ".")
print("Banco:", bancoFavorecido, "AG:", agenciaFavorecido, "CC:", contaFavorecido, ".")