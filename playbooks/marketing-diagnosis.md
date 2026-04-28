# Marketing Diagnosis Playbook

Playbook principal para diagnosticar campanhas e performance de mídia da Blue Ocean sem cair na armadilha de olhar só CPL ou plataforma.

## Quando usar
- queda de performance em Meta Ads ou Google Ads
- dúvida entre escalar, pausar, manter ou reestruturar
- suspeita de criativo fadigado, segmentação ruim ou oferta desalinhada
- conflito entre leitura de mídia e resultado no CRM
- necessidade de identificar se o problema está na mídia ou fora dela

## Objetivo
1. ler a mídia como sistema, não como painel isolado
2. separar problema de estrutura, segmentação, criativo, oferta, stack, CRM ou comercial
3. cruzar plataforma com funil real sempre que possível
4. produzir uma decisão proporcional à força da evidência

## Pré-checagem obrigatória
Antes de analisar performance:
- qual é o período analisado?
- qual conta, campanha, conjunto ou anúncio está em foco?
- qual é o objetivo da campanha?
- a fonte mais próxima do evento real está disponível?
- existe CRM coerente para cruzamento?
- existe sinal de stack contaminada, lead fantasma ou dashboard divergente?

Se a base estiver contaminada, rebaixar a confiança e priorizar reconciliação antes de qualquer decisão forte.

## Hierarquia de leitura
Toda análise deve seguir esta ordem.

### 1. Estrutura
Verificar:
- naming legível e padronizado
- separação lógica por objetivo, oferta, temperatura e público
- organização coerente entre campanha, conjunto e anúncio
- excesso de duplicação, desordem ou campanhas obsoletas

### 2. Segmentação e entrega
Verificar:
- aderência do público ao ICP
- geo, idade, gênero e posicionamento coerentes
- budget proporcional ao tamanho e potencial da audiência
- frequência saudável ou saturação
- distribuição de entrega entre conjuntos

### 3. Criativo e mensagem
Verificar:
- clareza de gancho, dor, promessa e CTA
- aderência ao estágio do funil
- risco de curiosidade errada
- sinais de fadiga criativa
- se o criativo atrai lead aderente ou apenas clique barato

### 4. Performance de plataforma
Verificar:
- tendências de CPL, CTR, CPM, frequência e volume
- desempenho por campanha, conjunto e anúncio
- benchmark interno aplicável
- diferença entre criativo barato e criativo que realmente gera avanço

### 5. Cruzamento com CRM e funil
Verificar:
- CPL real no CRM
- percentual de Lead Fantasma
- avanço para qualificação, reunião, oportunidade e venda
- onde o funil quebra
- se o problema real está no comercial, operação, stack ou governança

### 6. Decisão
A decisão final deve cair em uma destas classes:
- escalar
- pausar
- manter
- reestruturar
- trocar criativo
- trocar copy
- trocar oferta
- trocar público
- trocar posicionamento
- revisar CRM, comercial, stack ou funil

## Regras de decisão
### Escalar
Só quando houver:
- evidência forte ou pelo menos útil com fundo validado
- lead aderente no CRM
- avanço comercial consistente
- capacidade comercial e operacional para absorção

### Pausar
Só quando houver:
- causa razoavelmente identificada
- validação de que o problema não está principalmente fora da mídia
- nível de perda ou desperdício suficiente para justificar a pausa

### Reestruturar
Usar quando:
- a estrutura compromete leitura ou execução
- a segmentação está claramente desalinhada
- a oferta atrai o público errado
- há dependência excessiva de criativo vencedor isolado

### Revisar fora da mídia
Priorizar quando aparecer:
- Padrão CPL bom, fundo morto
- Padrão lead bom desperdiçado
- Padrão stack invisível
- Padrão atribuição fantasma

## Padrões diagnósticos a observar
- `Padrão 1: CPL bom, fundo morto`
- `Padrão 2: volume sem aderência`
- `Padrão 3: creative fatigue`
- `Padrão 4: fantasma dominante`
- `Padrão 5: stack invisível`
- `Padrão 12: atribuição fantasma`

Referenciar o padrão quando houver sintomas suficientes, mas sem transformar padrão em prova final.

## Classe de evidência
Usar esta leitura mínima de evidência:
- Classe 1: fato observado na plataforma
- Classe 2: métrica cruzada com CRM
- Classe 3: hipótese operacional baseada em padrão
- Classe 4: inferência provisória
- Classe 5: dado ausente ou frágil

Mapeamento para confiança:
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

## Saída recomendada
A análise final deve sempre responder:
1. diagnóstico executivo
2. principal tipo de problema
3. fonte mais próxima do evento real usada na leitura
4. classe de evidência predominante
5. confiança final: Alta, Parcial, Frágil ou Insuficiente
6. leitura estrutural
7. leitura de segmentação
8. leitura de criativo e mensagem
9. leitura de performance
10. leitura de CRM e funil
11. owner principal do problema
12. co-owner ou interface
13. nível de decisão: pode seguir, pode seguir com ressalva, precisa subir, não pode recomendar com confiança ainda, ou deve travar
14. ação inicial recomendada
15. plano de ação por prioridade
16. principais alertas
17. o que ainda precisa validar

## Regras de qualidade
- não chamar campanha de boa só porque o CPL está baixo
- não recomendar escala com base apenas em plataforma
- não recomendar pausa forte sem checar CRM, stack e comercial
- não fingir causalidade forte quando a base é parcial
- não usar dashboard como verdade final se divergir da origem
- se a análise visual do criativo não existir, sinalizar a limitação
- usar `knowledge/matrices/ownership-governance-matrix.md` quando houver dúvida de owner
- se houver conflito entre áreas, risco sem plano, ou decisão estrutural com base frágil, aplicar o escalonamento do `governance/decision-framework.md`

## Referências
- `company/icp.md`
- `company/offers.md`
- `governance/confidence-system.md`
- `governance/decision-framework.md`
- `knowledge/benchmarks/blue-ocean-benchmarks.md`
- `knowledge/patterns/diagnostic-patterns.md`
- `knowledge/company-brain/source-truth-rules.md`
