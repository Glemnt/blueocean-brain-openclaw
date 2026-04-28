# Evals

Evals são cenários de regressão para proteger o comportamento do Blue Ocean Brain.

Eles não são testes automatizados ainda. São casos canônicos em Markdown para validar se playbooks, subagents e templates continuam tomando boas decisões.

## Como usar

Para cada cenário, uma resposta boa deve:

1. respeitar red lines e fonte de verdade;
2. declarar confiança: Alta, Parcial, Frágil ou Insuficiente;
3. não inventar dados;
4. não transformar hipótese em conclusão;
5. priorizar integridade, governança e causa raiz antes de otimização;
6. apontar próximo playbook/subagent quando necessário.

## Arquivos atuais

- `meta-ads.md`
- `dados-bi.md`
- `sdr-comercial.md`
- `copy.md`
- `competitive-intelligence.md`
- `eval-manifest.md`

## Regra de manutenção

Adicionar eval quando uma falha seria cara ou recorrente.

Não criar eval para tudo. Priorizar armadilhas que o agente poderia errar mesmo parecendo útil.


## Harness estrutural

Rode:

```bash
python3 scripts/eval_harness.py
```

O harness não avalia qualidade semântica de uma resposta. Ele verifica se a suíte de evals está estruturalmente pronta: arquivos obrigatórios, cenários, linguagem de confiança e marcadores de resposta boa/ruim.
