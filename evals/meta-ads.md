# Evals — Meta Ads

## Cenário 1 — CPL bom, fundo ruim

Contexto:
- CPL plataforma baixo e volume alto.
- CRM/Sheets indicam poucas reuniões, quase nenhuma oportunidade e feedback de misfit.

Resposta boa deve:
- não recomendar escala;
- declarar que CPL baixo não prova campanha saudável;
- investigar mensagem, público, oferta e qualificação;
- pedir ou usar dados de CRM/Sheets para CPL real e avanço;
- confiança no máximo Parcial se fundo não estiver validado.

Resposta ruim faria:
- escalar só porque CPL parece bom.

## Cenário 2 — Lead Fantasma dominante em CTWA

Contexto:
- Meta mostra muitas conversas iniciadas.
- Kommo/Sheets mostram muitos `Lead Fantasma` e poucos `Lead Real`.

Resposta boa deve:
- separar volume bruto de volume válido;
- calcular leitura usando Lead Real;
- acionar `playbooks/stack-failure-triage.md` ou reconciliação se a trilha não estiver íntegra;
- investigar CTA, mensagem pré-preenchida, público e automação.

Resposta ruim faria:
- tratar conversa/plataforma como lead válido.

## Cenário 3 — Audience Network infla resultado

Contexto:
- Audience Network concentra gasto, CTR alto e CPL baixo.
- Leads não respondem ou não qualificam.

Resposta boa deve:
- identificar risco de clique acidental/baixa qualidade;
- cruzar por placement com CRM/Sheets;
- recomendar limitar/excluir placement se evidência sustentar;
- não chamar CTR alto de vitória isolada.

Resposta ruim faria:
- aceitar métrica de topo sem qualidade de fundo.

## Cenário 4 — Evento de conversão errado

Contexto:
- campanha aparece com zero lead ou conversões inconsistentes.
- há suspeita de evento custom/pixel/promoted object incorreto.

Resposta boa deve:
- exigir identificação do evento correto no ad set antes de interpretar `actions[]`;
- rebaixar confiança se evento não estiver confirmado;
- não declarar campanha sem resultado antes da validação.

Resposta ruim faria:
- diagnosticar mídia ruim quando a leitura do evento está errada.

## Rubricas semânticas

### Cenário 1 — CPL bom, fundo ruim
- Deve conter: separação entre CPL plataforma, CPL real, reuniões e oportunidades.
- Deve bloquear: recomendação de escala baseada só em CPL baixo.
- Confiança máxima permitida: `Parcial` sem validação CRM/Sheets; `Frágil` se fontes divergirem.
- Red line testada: otimizar topo ignorando qualidade comercial.

### Cenário 2 — Lead Fantasma dominante em CTWA
- Deve conter: distinção entre conversa iniciada, Lead Real e Lead Fantasma.
- Deve bloquear: tratar métrica Meta como lead operacionalmente válido.
- Confiança máxima permitida: `Frágil` se trilha CTWA/Kommo não estiver íntegra.
- Red line testada: atribuição forte sem trilha robusta.

### Cenário 3 — Audience Network infla resultado
- Deve conter: análise por placement cruzada com CRM/Sheets.
- Deve bloquear: vitória por CTR/CPL isolado.
- Confiança máxima permitida: `Parcial` sem validação de fundo; `Frágil` se qualidade do lead estiver ausente.
- Red line testada: confundir atenção barata com aquisição qualificada.

### Cenário 4 — Evento de conversão errado
- Deve conter: validação de evento/pixel/promoted object antes do diagnóstico.
- Deve bloquear: declarar campanha ruim sem confirmar evento.
- Confiança máxima permitida: `Insuficiente` até confirmar evento correto.
- Red line testada: decisão de mídia em cima de mensuração quebrada.
