# Google Sheets Integration

Documentação canônica da integração Google Sheets dentro do `blueocean-brain-openclaw`.

## Papel da integração
Google Sheets atua como camada operacional auxiliar e, em alguns fluxos, como buffer temporário, log ou apoio analítico.

Ela pode ser útil para:
- buffers de automação
- logs intermediários
- consolidações operacionais
- visibilidade rápida de dados transitórios

## O que a integração faz bem
- armazenar buffers simples e auditáveis
- dar visibilidade rápida a dados temporários
- registrar logs de workflows e matches
- apoiar consolidações operacionais de baixo atrito

## O que ela não deve virar
- não deve virar fonte final de verdade comercial
- não deve prevalecer sobre CRM quando o tema é lead válido ou avanço
- não deve prevalecer sobre plataforma quando o tema é spend ou entrega
- não deve ser usada como substituto de reconciliação

## Quando o uso é saudável
- buffer temporário entre webhook e CRM
- log de alertas ou execuções
- controle operacional complementar
- apoio de conferência durante implementação ou validação

## Fragilidades conhecidas
- atualização manual ou parcial contamina leitura
- fórmulas podem mascarar erro de origem
- planilha derivada pode divergir do CRM ou da plataforma
- edição humana sem governança reduz confiabilidade
- crescimento desordenado transforma Sheets em pseudo-banco sem controle

## Erros comuns de interpretação
- tratar planilha como fonte final só porque está visível
- confiar em cálculo derivado sem revisar origem dos dados
- esquecer que a planilha pode estar desatualizada
- usar Sheets para decidir quando CRM e plataforma divergem

## Relação com fonte de verdade
Sheets pode ser útil, mas quase sempre é uma camada derivada ou intermediária.

Na hierarquia típica:
- plataforma prevalece para entrega e spend
- CRM prevalece para lead válido e avanço
- Sheets apoia, mas raramente decide sozinho

## Relação com outras camadas
- automação: `integrations/n8n.md`
- CRM: `integrations/kommo.md`
- mídia: `integrations/meta-ads.md`
- reconciliação: `playbooks/crm-reconciliation.md`

## Regra final
Sheets é excelente como apoio operacional.

Mas, quando começa a competir com a fonte mais próxima do evento real, ele vira risco de interpretação em vez de ajuda.
