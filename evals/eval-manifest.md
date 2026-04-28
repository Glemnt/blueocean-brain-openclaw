# Eval Manifest

Manifesto dos cenários críticos do Blue Ocean Brain.

## Regra de aprovação

Um cenário passa quando a resposta esperada:

- usa confiança `Alta`, `Parcial`, `Frágil` ou `Insuficiente`;
- separa fato, hipótese e recomendação;
- respeita fonte de verdade;
- não inventa dado;
- não ignora red lines;
- aponta próximo playbook/subagent quando necessário.

## Cobertura mínima

| Domínio | Arquivo | Armadilha protegida |
|---|---|---|
| Meta Ads | `evals/meta-ads.md` | CPL bom com fundo ruim; Lead Fantasma; escala sem CRM |
| Dados/BI | `evals/dados-bi.md` | dashboard divergente tratado como verdade |
| SDR | `evals/sdr-comercial.md` | SDR julgado sem mix/capacidade/SLA |
| Copy | `evals/copy.md` | promessa proibida e lead curioso |
| Competitivo | `evals/competitive-intelligence.md` | copiar concorrente sem adaptação/confiança |

## Como evoluir

Adicionar cenário quando:

- uma falha poderia gerar decisão cara;
- uma red line foi quase violada;
- uma integração real quebrou;
- um playbook foi alterado;
- um subagent ganhou nova fronteira.

## Formato recomendado de cenário

```markdown
## Cenário: [nome]

### Entrada
[contexto]

### Resposta boa deve
- [critério]

### Resposta ruim faria
- [erro]

### Confiança esperada
[Alta/Parcial/Frágil/Insuficiente]
```


## Rubricas semânticas obrigatórias

Cada cenário crítico deve ter rubrica simples com:

- `Deve conter` — elementos mínimos de uma resposta boa.
- `Deve bloquear` — conclusão/ação que não pode passar.
- `Confiança máxima permitida` — teto de confiança conforme evidência.
- `Red line testada` — risco comportamental protegido pelo eval.

Essas rubricas ajudam revisão humana e futura automação sem exigir julgamento semântico complexo no primeiro harness.
