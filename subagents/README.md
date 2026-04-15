# Subagents

Subagentes são especialistas nativos do `blueocean-brain-openclaw`.

Eles não substituem a governança central. Eles operam dentro dela.

## Princípios
- herdam governança global do repositório
- são especializados por domínio real, não por ferramenta apenas
- devem ser menores e mais canônicos que os prompts do repositório original
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

## Próximos candidatos
- `competitive-intelligence-analyst.md`
- especialistas adicionais apenas se houver necessidade real de operação

## Regra de qualidade
Ao criar ou revisar um subagent, validar sempre:
1. se ele tem missão clara
2. se o domínio está bem delimitado
3. se a entrada e a saída esperadas estão claras
4. se a lógica de confiança está alinhada ao canon
5. se os handoffs estão corretos
6. se ele está melhor adaptado ao OpenClaw do que uma simples cópia do original
