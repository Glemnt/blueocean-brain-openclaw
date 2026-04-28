# Evals — SDR/Comercial

## Cenário 1 — SDR saudável

Contexto:
- SLA bom, qualificação consistente, no-show baixo, CRM bem preenchido e motivos de perda variados.

Resposta boa deve:
- reconhecer como saudável;
- não inventar problema;
- sugerir manutenção e eventual replicação de boas práticas.

Resposta ruim faria:
- forçar coaching desnecessário para parecer útil.

## Cenário 2 — Qualificação frouxa

Contexto:
- taxa de qualificação muito alta, mas poucas reuniões e muitas perdas por sem interesse/misfit.

Resposta boa deve:
- diagnosticar pipeline inflado ou critério frouxo;
- investigar script/critério antes de culpar mídia ou volume;
- sugerir revisão de qualificação.

Resposta ruim faria:
- tratar alta qualificação como métrica positiva isolada.

## Cenário 3 — SLA crítico

Contexto:
- contato demora muito, leads esfriam e perdas indicam falta de atenção.

Resposta boa deve:
- priorizar SLA como causa provável;
- não classificar lead como ruim sem checar velocidade de contato;
- recomendar rotina/notificação/capacidade.

Resposta ruim faria:
- diagnosticar mídia ruim quando o lead foi desperdiçado.

## Cenário 4 — No-show alto em CTWA

Contexto:
- muitos agendamentos, no-show alto, reuniões marcadas para muito longe e pouca confirmação.

Resposta boa deve:
- tratar como problema de processo e compromisso;
- considerar baixa barreira do CTWA;
- recomendar confirmação D-1/D0, agenda mais próxima e follow-up.

Resposta ruim faria:
- culpar apenas SDR ou apenas campanha.


## Confiança esperada

- Usar `Parcial` quando houver dados de CRM/SLA suficientes.
- Usar `Frágil` quando houver amostra pequena, mix de canal diferente ou campos incompletos.
- Usar `Insuficiente` quando não houver dados por SDR/etapa.

## Rubricas semânticas

### Cenário 1 — SDR saudável
- Deve conter: reconhecimento de saúde e manutenção/replicação de boas práticas.
- Deve bloquear: inventar problema para parecer útil.
- Confiança máxima permitida: `Parcial` se há dados suficientes; `Alta` só com múltiplos períodos e CRM consistente.
- Red line testada: diagnóstico forçado sem evidência.

### Cenário 2 — Qualificação frouxa
- Deve conter: pipeline inflado, critério de qualificação e revisão de script.
- Deve bloquear: tratar alta qualificação como vitória isolada.
- Confiança máxima permitida: `Parcial`; `Frágil` se motivos de perda/campos estiverem incompletos.
- Red line testada: métrica comercial de vaidade.

### Cenário 3 — SLA crítico
- Deve conter: SLA como causa provável e plano de resposta/capacidade.
- Deve bloquear: chamar lead de ruim sem checar velocidade de contato.
- Confiança máxima permitida: `Parcial` com dados de SLA; `Frágil` sem timestamps confiáveis.
- Red line testada: lead desperdiçado sendo atribuído à mídia.

### Cenário 4 — No-show alto em CTWA
- Deve conter: confirmação D-1/D0, agenda próxima, follow-up e baixa barreira CTWA.
- Deve bloquear: culpar só SDR ou só campanha.
- Confiança máxima permitida: `Parcial`; `Frágil` se origem/agendamento não estiverem confiáveis.
- Red line testada: causa única para problema multi-camada.
