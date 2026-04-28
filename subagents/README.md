# Subagents

Subagentes são especialistas nativos do `blueocean-brain-openclaw`.

Eles não substituem a governança central. Eles operam dentro dela.

## Princípios
- herdam governança global do repositório
- são especializados por domínio real, não por ferramenta apenas
- devem ser curtos, canônicos e operacionais
- devem apontar para playbooks e knowledge em vez de duplicar tudo
- precisam deixar claro quando usar, quando bloquear e para onde fazer handoff

## Papel na arquitetura
A lógica do sistema fica distribuída assim:
- `governance/` define limites, ownership, confiança e decisão
- `company/` define identidade, oferta, ICP e vocabulário
- `knowledge/` concentra referência recorrente
- `playbooks/` definem fluxos operacionais canônicos
- `subagents/` executam leituras especializadas dentro desses limites

## Fronteiras obrigatórias
Um subagent deve:
- operar no seu domínio
- explicitar confiança
- respeitar a fonte mais próxima do evento real
- travar quando a base não sustenta leitura forte
- fazer handoff quando a causa principal estiver fora do seu domínio

Um subagent não deve:
- virar roteador genérico
- duplicar governança inteira localmente
- tomar decisão irreversível com base frágil
- invadir domínio de outro especialista sem sinalizar a fronteira

## Subagents atuais
- `meta-ads-analyst.md`
- `dados-bi-analyst.md`
- `sdr-comercial-analyst.md`
- `copy-strategist.md`
- `competitive-intelligence-analyst.md`

## Próximos candidatos
- especialistas adicionais apenas se houver necessidade real de operação

## Regra de qualidade
Ao criar ou revisar um subagent, validar sempre:
1. se ele tem missão clara
2. se o domínio está bem delimitado
3. se a entrada e a saída esperadas estão claras
4. se a lógica de confiança está alinhada ao canon
5. se os handoffs estão corretos
6. se ele está claro, acionável e aderente à governança central

## Spawn / Handoff Protocol

Use este protocolo sempre que o agente principal precisar dividir uma demanda entre especialistas ou transferir contexto entre domínios.

### Quando spawnar um subagent

Spawnar quando:

- a análise exige leitura especializada profunda;
- há múltiplas frentes paralelas independentes;
- o contexto precisa ser preservado sem misturar raciocínios;
- o trabalho demanda auditoria/revisão dedicada;
- um domínio não deve invadir outro sem owner claro.

Não spawnar quando:

- a resposta cabe em um playbook simples;
- falta dado mínimo para qualquer especialista;
- a demanda é só roteamento;
- o custo de contexto é maior que o benefício.

### Handoff obrigatório

Todo handoff deve usar ou espelhar `templates/handoff-subagente.md` com:

- origem e destino;
- objetivo do handoff;
- contexto mínimo;
- evidências e fontes;
- confiança da origem;
- lacunas conhecidas;
- red lines;
- output esperado;
- decisão que o destino pode ou não tomar.

### Regra de confiança

A confiança do destino **não pode ser maior** que a confiança da origem sem evidência nova.

Se o destino encontrar conflito, deve:

1. explicitar conflito;
2. reduzir confiança;
3. pedir/recomendar validação;
4. não tomar decisão forte.

### Handoff por domínio

- Meta → Dados/BI: quando a leitura depende de CRM, Sheets, CPL real ou Lead Fantasma.
- Meta → Copy: quando o diagnóstico aponta fadiga, hook fraco, promessa ou remake.
- Dados/BI → SDR: quando a quebra está em SLA, qualificação, no-show ou motivo de perda.
- SDR → Governança: quando há owner ausente, risco de conta, SLA crítico sem plano ou red line.
- Competitivo → Copy/Meta: quando o aprendizado deve virar hipótese de teste, não cópia literal.

### Output mínimo de subagent

Todo subagent deve devolver:

- diagnóstico ou achado;
- evidências usadas;
- confiança;
- limites/lacunas;
- ação recomendada;
- handoff necessário, se houver.
