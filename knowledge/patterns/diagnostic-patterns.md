# Diagnostic Patterns

Padrões diagnósticos recorrentes para acelerar triagem e investigação.

## Como usar
Cada padrão deve ajudar a reconhecer um cenário recorrente sem substituir validação. Usar o padrão para orientar leitura, ação inicial e skill ou playbook recomendado.

## Padrões principais

### Padrão 1: CPL bom, fundo morto
- fingerprint: CPL saudável, volume de leads aceitável, poucas reuniões e quase nenhuma oportunidade
- diagnóstico: o topo funciona, o fundo não converte
- causa raiz provável: qualidade do lead, SLA, qualificação fraca ou oferta desalinhada
- armadilha: escalar porque o CPL parece bom
- ação imediata: auditar qualidade do lead no CRM antes de decidir budget

### Padrão 2: volume sem aderência
- fingerprint: alto volume, muito misfit, feedback comercial de público errado, CPL até baixo
- diagnóstico: segmentação ou copy atraindo público errado
- causa raiz provável: audiência ampla demais, criativo genérico, copy sem filtro de ICP
- armadilha: culpar o SDR por baixa conversão
- ação imediata: revisar segmentação, copy e filtros de ICP

### Padrão 3: creative fatigue
- fingerprint: CTR caindo, frequência alta, CPL subindo, hook rate piorando
- diagnóstico: o público saturou o criativo
- causa raiz provável: rotação insuficiente, público pequeno, budget excessivo para o tamanho da audiência
- armadilha: culpar a audiência quando o criativo cansou
- ação imediata: revisar frequência por conjunto e preparar novos criativos

### Padrão 4: fantasma dominante
- fingerprint: lead fantasma alto em CTWA, Meta mostra conversa mas CRM mostra poucos leads reais
- diagnóstico: o clique acontece, a conversa real não
- causa raiz provável: CTA confuso, mensagem pré-preenchida ruim, posicionamento errado ou público frio demais para WhatsApp
- armadilha: tratar como campanha sem performance
- ação imediata: filtrar Lead Real e revisar CTA e mensagem pré-preenchida

### Padrão 5: stack invisível
- fingerprint: discrepância alta entre plataforma e CRM, campos vazios e dashboard divergente
- diagnóstico: a stack quebrou silenciosamente
- causa raiz provável: webhook, n8n, salesbot ou automação falhando
- armadilha: analisar mídia como se o problema fosse de campanha
- ação imediata: bloquear decisão de mídia e auditar a stack inteira

### Padrão 6: lead bom desperdiçado
- fingerprint: lead com fit, SLA lento, ausência de resposta após contato tardio
- diagnóstico: o problema não é o lead, é a velocidade do contato
- causa raiz provável: SDR sobrecarregado, distribuição ruim ou ausência de monitoramento de SLA
- armadilha: classificar como lead ruim
- ação imediata: auditar SLA real e capacidade comercial antes de escalar campanha

### Padrão 7: pipeline inflado
- fingerprint: muitas oportunidades, poucas com próximo passo real, várias paradas e win rate baixo
- diagnóstico: pipeline parece cheio, mas está poluído
- causa raiz provável: critério frouxo, CRM mal preenchido ou pressão por pipeline cosmético
- armadilha: usar esse pipeline para forecast
- ação imediata: sanear pipeline e contar só oportunidades reais

### Padrão 8: conta em espiral silenciosa
- fingerprint: cliente responde menos, pendências acumulam, risco não formalizado
- diagnóstico: a conta está degradando sem oficialização
- causa raiz provável: owner reativo, falta de rotina e risco não formalizado
- armadilha: esperar o cliente reclamar
- ação imediata: formalizar risco, definir plano e escalar

### Padrão 9: escopo elástico
- fingerprint: pequenos fora de escopo recorrentes, absorção informal, expectativa do cliente muda
- diagnóstico: o fora de escopo virou rotina
- causa raiz provável: ausência de registro e medo de confronto
- armadilha: chamar de flexibilidade ou bom atendimento
- ação imediata: registrar, classificar e travar absorção automática

### Padrão 10: terra de ninguém
- fingerprint: todos conhecem o problema, ninguém assume, áreas se apontam
- diagnóstico: ausência de ownership
- causa raiz provável: fronteira ambígua entre áreas ou dono não definido
- armadilha: tomar lado sem definir owner
- ação imediata: definir owner antes de aprofundar o diagnóstico

### Padrão 11: decisão em base podre
- fingerprint: decisão importante prestes a acontecer com CRM incompleto, dashboard divergente ou stack contaminada
- diagnóstico: decisão irreversível em base frágil
- causa raiz provável: urgência acima de prudência, uso cego do dashboard ou ausência de auditoria de fonte
- armadilha: aceitar a decisão porque alguém importante quer velocidade
- ação imediata: travar a decisão e expor a fragilidade da base

### Padrão 12: atribuição fantasma
- fingerprint: plataforma, CRM, Sheets ou dashboard atribuem volume/resultado a uma origem, campanha ou SDR sem trilha íntegra entre clique, lead, automação e avanço comercial
- diagnóstico: a atribuição parece existir no relatório, mas não está comprovada na trilha operacional
- causa raiz provável: source/source_id mal preenchido, webhook incompleto, match temporal frágil, campo de campanha ausente, dashboard derivado ou regra de atribuição antiga
- armadilha: otimizar mídia, copy ou comercial com base em atribuição aparente
- ação imediata: auditar a cadeia de captura → automação → CRM → Sheets antes de declarar vencedor, vilão ou CPL real
