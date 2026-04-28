# Métricas Derivadas de Dashboard

## Princípio

Dashboard é camada derivada, não fonte final. Ele acelera leitura, mas precisa apontar origem e confiança.

## Regras

- Toda métrica derivada deve ter fórmula documentada.
- Toda fórmula deve indicar fontes.
- Campos vazios, zero e nulo têm significados diferentes.
- Mudança de schema precisa versão/data.
- Divergência com origem deve aparecer como alerta, não ser escondida.

## Fórmulas recomendadas

- `CPL plataforma = gasto_meta / leads_meta`
- `CPL operacional = gasto_meta / leads_operacionalmente_validos`
- `CPL real = gasto_meta / leads_reais`
- `CPAg = gasto_meta / reunioes_agendadas`
- `CPR = gasto_meta / reunioes_realizadas`
- `Taxa no-show = 1 - reunioes_realizadas / reunioes_agendadas`
- `Taxa Lead Fantasma = 1 - leads_reais / leads_meta_ctwa`

## Confiança

- Alta: fonte cruzada e sem divergência relevante.
- Parcial: uma fonte principal e validação indireta.
- Frágil: divergência, campos faltantes ou stack instável.
- Insuficiente: origem ausente ou schema quebrado.
