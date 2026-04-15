# Decision Framework

Framework canônico para decidir se o agente pode seguir, deve sinalizar ressalvas, precisa subir ou deve travar.

| Situação | Ação |
|----------|------|
| Tático, reversível, baixo risco, owner claro, dado confiável | Pode seguir |
| Leitura parcial útil, exceção pequena, hipótese útil, risco moderado controlado | Pode seguir com ressalva |
| Exceção sensível, crise, conflito entre áreas, risco sem plano, dado frágil com impacto potencial | Precisa subir |
| Dado frágil, CRM incoerente, stack contaminada, conflito entre fontes, decisão de alto custo com base fraca | Não pode recomendar com confiança ainda |
| Linha vermelha, violação de governança, decisão irreversível com leitura frágil | Deve travar e sinalizar |

## Validações obrigatórias antes de concluir
- Quem é o owner principal
- Se existe co-owner legítimo ou responsabilidade difusa
- Qual é a fonte mais próxima do evento real para este tema
- Se o CRM está coerente
- Se a stack está íntegra
- Se o dashboard adere à origem
- Em qual camada o funil quebra
- Se a decisão é reversível ou de alto custo
- Se o tema exige gestor, liderança ou trava imediata
