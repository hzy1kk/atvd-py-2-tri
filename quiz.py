# Sistema de Quiz Interativo

print("🎯 Bem-vindo ao Quiz Interativo!")
print("Responda as perguntas digitando a letra da alternativa correta (a, b, c, d)\n")

# Lista de perguntas, alternativas e respostas corretas
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "alternativas": {"a": "Rio de Janeiro", "b": "Brasília", "c": "São Paulo", "d": "Salvador"},
        "resposta_correta": "b"
    },
    {
        "pergunta": "Quantos planetas existem no sistema solar?",
        "alternativas": {"a": "7", "b": "8", "c": "9", "d": "10"},
        "resposta_correta": "b"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "alternativas": {"a": "Machado de Assis", "b": "Miguel de Cervantes", "c": "William Shakespeare", "d": "Luís de Camões"},
        "resposta_correta": "b"
    }
]

while True:
    pontuacao = 0
    print("=" * 50)
    
    # Loop através de todas as perguntas
    for i, pergunta in enumerate(perguntas, 1):
        print(f"Pergunta {i}: {pergunta['pergunta']}")
        
        # Exibe as alternativas
        for letra, texto in pergunta['alternativas'].items():
            print(f"  {letra}) {texto}")
        
        # Validação da entrada do usuário
        while True:
            resposta = input("\nSua resposta: ").strip().lower()
            
            if resposta == "":
                print("❌ Por favor, digite uma resposta (a, b, c ou d).")
                continue
            
            if resposta not in ['a', 'b', 'c', 'd']:
                print("❌ Opção inválida! Digite apenas a, b, c ou d.")
                continue
            else:
                break
        
        # Verifica se a resposta está correta
        if resposta == pergunta['resposta_correta']:
            print("✅ Correto!")
            pontuacao += 1
        else:
            print(f"❌ Incorreto! A resposta correta é {pergunta['resposta_correta'].upper()}.")
        
        print("-" * 30)
    
    # Exibe a pontuação final
    print(f"\n🎉 Quiz finalizado! Sua pontuação: {pontuacao}/{len(perguntas)}")
    
    # Feedback baseado na pontuação
    if pontuacao == len(perguntas):
        print("🌟 Excelente! Você acertou todas as perguntas!")
    elif pontuacao >= len(perguntas) / 2:
        print("👍 Bom trabalho! Você foi bem no quiz.")
    else:
        print("💪 Continue estudando! Você pode melhorar.")
    
    # Pergunta se o usuário quer jogar novamente
    while True:
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        
        if jogar_novamente == "":
            print("Por favor, digite 's' para sim ou 'n' para não.")
            continue
        
        if jogar_novamente not in ['s', 'n']:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")
            continue
        else:
            break
    
    if jogar_novamente == 'n':
        print("\nObrigado por jogar! Até a próxima! 👋")
        break

    print("\n" + "=" * 50)
