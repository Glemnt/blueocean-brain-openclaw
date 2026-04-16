# Executive Reporting Playbook

Playbook principal para transformar análise operacional em leitura executiva clara, confiável e acionável.

## Quando usar
- fechamento de período
- resumo executivo de campanha, operação, comercial ou conta
- apresentação de diagnóstico para tomada de decisão
- necessidade de consolidar muita informação em poucos pontos úteis
- comparação entre resultado, risco e próximos passos

## Objetivo
1. resumir o que realmente importa sem perder rigor
2. separar dado forte de leitura frágil
3. destacar o que exige decisão, correção ou monitoramento
4. evitar relatório bonito, mas vazio ou enganoso

## Pré-checagem obrigatória
Antes de consolidar:
- qual é o período analisado?
- qual é o recorte: conta, operação, mídia, comercial ou empresa?
- a base está íntegra o suficiente para leitura executiva?
- o que é fato, o que é hipótese e o que ainda depende de validação?
- existe alguma linha vermelha, risco sensível ou trava de governança?

## Hierarquia de leitura
### 1. Contexto do período
Verificar:
- o que está sendo resumido
- se houve mudança relevante no período
- qual é a pergunta executiva principal

### 2. Resultado principal
Verificar:
- o que melhorou, piorou ou ficou estável
- quais números sustentam a leitura
- se o resultado é operacionalmente confiável

### 3. Risco e fragilidade
Verificar:
- base frágil, stack contaminada ou conflito entre fontes
- risco de interpretação errada
- alertas que mudam a leitura executiva

### 4. Implicação prática
Verificar:
- o que isso significa para a Blue Ocean
- qual decisão, correção ou acompanhamento decorre da leitura
- se existe urgência real ou só ruído

### 5. Próximos passos
Concluir:
- o que fazer agora
- o que monitorar
- o que ainda precisa validar

## Classes de evidência
Usar esta leitura mínima:
- Classe 1: fato consolidado em base íntegra
- Classe 2: fato observado em fonte confiável com ressalva limitada
- Classe 3: leitura comparativa ou padrão com pequena fragilidade
- Classe 4: inferência executiva sobre base parcial
- Classe 5: dado ausente, frágil ou conflito relevante

## Confiança
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

Usar sempre o sistema: Alta, Parcial, Frágil ou Insuficiente.

## Saída recomendada
A leitura executiva final deve responder:
1. resumo executivo
2. período e escopo
3. principais resultados
4. classe de evidência predominante
5. confiança final
6. principais ganhos
7. principais riscos ou alertas
8. leitura do que exige decisão
9. próximos passos priorizados
10. o que ainda precisa validar

## Regras de qualidade
- não esconder fragilidade de base para parecer mais executivo
- não transformar hipótese em manchete
- não lotar o resumo com detalhe operacional desnecessário
- não omitir risco sensível que muda a decisão
- usar `governance/confidence-system.md` para sustentar a confiança da leitura
- usar `playbooks/action-prioritization.md` quando a decisão exigir ordenação clara de ações

## Referências
- `governance/confidence-system.md`
- `governance/decision-framework.md`
- `knowledge/company-brain/source-truth-rules.md`
- `playbooks/marketing-diagnosis.md`
- `playbooks/crm-reconciliation.md`
- `playbooks/stack-failure-triage.md`
