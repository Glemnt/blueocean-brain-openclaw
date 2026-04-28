# Handoff Inter-Subagente

Template para transferir contexto entre subagents sem perder evidência, confiança, restrições ou decisão pendente.

Use quando um especialista identificar que a causa raiz, a próxima ação ou a validação necessária pertence a outro domínio.

## Quando usar

Exemplos:

- Meta Ads identifica criativo vencedor e precisa de remake → Copy Strategist
- Meta Ads identifica lead ruim ou Lead Fantasma → Dados/BI ou SDR/Comercial
- Dados/BI resolve discrepância e pede reanálise de mídia → Meta Ads
- SDR/Comercial identifica problema de qualidade de lead → Meta Ads
- Copy precisa de dados de performance antes de gerar variações → Meta Ads
- Competitive Intelligence encontra referência útil → Copy ou Meta Ads
- Qualquer subagent encontra risco de governança → agente principal + `playbooks/governance-escalation.md`

## Regra central

A confiança do destino não pode ser maior que a confiança da origem sem nova evidência.

Exemplo:

- se a origem entrega leitura `Parcial`, o destino só pode subir para `Alta` se trouxer nova evidência forte e declarar isso.

## Briefing de handoff

```markdown
# Briefing de Handoff Inter-Subagente

## Origem
- Subagent de origem:
- Playbook/fluxo executado:
- Data/período da análise:
- Confiança da leitura de origem: Alta / Parcial / Frágil / Insuficiente
- Classe de evidência predominante:

## Destino
- Subagent recomendado:
- Playbook/template recomendado:
- Ação esperada:

## Motivo do handoff
- O que foi encontrado:
- Por que isso sai do domínio da origem:
- Qual decisão ou análise depende do destino:

## Escopo transferido
- Conta/cliente/frente:
- Campanha/conjunto/anúncio/criativo, se aplicável:
- Funil/canal, se aplicável:
- Período analisado:
- Fonte mais próxima do evento real usada até agora:

## Dados relevantes
- Métricas principais:
- Evidências observadas:
- Lacunas de dados:
- Conflitos entre fontes:

## Hipótese atual
- Hipótese principal:
- Hipóteses alternativas:
- O que ainda não pode ser concluído:

## Restrições
- O que o destino não deve assumir:
- O que não deve ser mudado sem nova validação:
- Red lines aplicáveis:
- Riscos de interpretação:

## Output esperado
- Formato esperado da resposta:
- Decisão que precisa ser suportada:
- Próximo passo sugerido após o destino responder:
```

## Campos obrigatórios mínimos

Se o handoff precisar ser rápido, preencher pelo menos:

1. subagent de origem;
2. subagent de destino;
3. motivo do handoff;
4. confiança da origem;
5. evidência principal;
6. lacuna ou decisão pendente;
7. ação esperada.

## Regras de qualidade

- não jogar problema para outro subagent sem explicar por quê;
- não omitir fragilidade da leitura de origem;
- não transferir hipótese como se fosse fato;
- não mandar o destino repetir a análise inteira se só falta uma parte;
- não aumentar confiança sem nova evidência;
- preservar red lines e limites do domínio original;
- se houver risco sensível, envolver o agente principal e `playbooks/governance-escalation.md`.

## Handoffs comuns

| Origem | Destino | Gatilho | Próximo fluxo provável |
|---|---|---|---|
| Meta Ads | Copy | criativo/copy precisa remake ou variação | copy generation / análise de mensagem |
| Meta Ads | Dados/BI | discrepância entre plataforma, CRM, Sheets ou dashboard | `playbooks/crm-reconciliation.md` / `playbooks/stack-failure-triage.md` |
| Meta Ads | SDR/Comercial | CPL bom, fundo ruim ou misfit recorrente | análise SDR/comercial |
| Dados/BI | Meta Ads | base saneada permite reavaliar campanha | `marketing-diagnosis.md` |
| Dados/BI | SDR/Comercial | CRM/Sheets indicam gargalo comercial | análise SDR/comercial |
| SDR/Comercial | Meta Ads | qualidade do lead aponta para público/copy/oferta | `marketing-diagnosis.md` |
| SDR/Comercial | Dados/BI | CRM ou planilha impede leitura forte | reconciliação/integridade |
| Copy | Meta Ads | precisa de performance real antes de refazer mensagem | leitura por criativo/campanha |
| Competitive Intelligence | Copy | referência deve virar hipótese de copy | adaptação de mensagem |
| Competitive Intelligence | Meta Ads | referência deve virar hipótese de estrutura/criativo | diagnóstico/teste de mídia |
| Qualquer subagent | Governança | risco, exceção, owner difuso ou decisão sensível | `playbooks/governance-escalation.md` |

## Relação com outros arquivos

- `subagents/README.md`
- `governance/confidence-system.md`
- `governance/decision-framework.md`
- `playbooks/triage.md`
- `playbooks/governance-escalation.md`
