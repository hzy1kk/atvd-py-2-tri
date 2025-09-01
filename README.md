🔢 Jogo de Adivinhação com Dicas
Este é um jogo de adivinhação onde o computador seleciona um número aleatório e o jogador precisa descobrir qual é, recebendo dicas se está quente ou frio.

📋 Descrição
O Jogo de Adivinhação com Dicas gera um número secreto entre 1 e 100 e desafia o usuário a descobri-lo no menor número de tentativas possível. A cada palpite, o sistema informa se o jogador está "quente" (perto) ou "frio" (longe) do número correto.

🚀 Como Usar
Certifique-se de ter o Python instalado

Salve o código em um arquivo .py (ex: adivinhacao.py)

Execute no terminal: python adivinhacao.py

Digite números para tentar adivinhar o número secreto

🎮 Instruções de Uso
Digite um número entre 1 e 100

Receba dicas se está "quente" ou "frio"

Tente acertar em menos tentativas possível

Ao acertar, veja quantas tentativas foram necessárias

🏗️ Estruturas Utilizadas
Loop While
Utilizei um loop while para:

Manter o jogo rodando até o usuário acertar o número

Controlar o fluxo principal do jogo

Permitir múltiplas tentativas sem reiniciar o programa

Break
Usei break para finalizar o loop quando o usuário acerta o número secreto, encerrando elegantemente o jogo.

Validação de Entradas
Implementei validações robustas:

Verificação se o valor digitado é numérico

Garantia de que o número está dentro do intervalo 1-100

Prevenção contra entradas vazias

Condicionais (if, elif, else)
Usei estruturas condicionais para:

Comparar o palpite com o número secreto

Fornecer feedback visual (emojis) sobre a proximidade

Calcular a diferença entre o palpite e o número secreto

Dar dicas personalizadas baseadas na distância
