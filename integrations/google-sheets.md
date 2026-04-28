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
- não deve virar fonte final universal de verdade comercial
- não deve substituir Kommo/CRM quando a pergunta é entidade viva, owner, pipeline ou status estrutural
- não deve substituir plataforma quando o tema é spend ou entrega
- não deve transformar volume bruto em volume válido sem regra do funil
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
Sheets pode ser camada derivada, intermediária ou operacional principal, dependendo do fluxo real.

Na hierarquia típica:
- plataforma prevalece para entrega e spend
- Kommo/CRM prevalece para entidade estrutural do lead, owner, pipeline e status vivo quando os campos críticos estão íntegros
- Sheets apoia reconciliação, contexto e leitura operacional diária
- em WhatsApp/CTWA, a validade operacional exige separar Lead Real de Lead Fantasma, cruzando `WHATSAPP` e Kommo quando possível
- dashboard continua sendo derivado, mesmo quando nasce de Sheets

Regra prática:
- se Sheets estiver mais bem mantido que o CRM para reuniões, próximos passos ou operação diária, ele pode prevalecer nesse recorte específico
- isso não transforma Sheets em verdade universal; apenas aplica a regra da fonte mais próxima e mais íntegra para aquela pergunta

## Relação com outras camadas
- automação: `integrations/n8n.md`
- CRM: `integrations/kommo.md`
- mídia: `integrations/meta-ads.md`
- reconciliação: `playbooks/crm-reconciliation.md`

## Regra final
Sheets é excelente como apoio operacional.

Mas, quando começa a competir com a fonte mais próxima do evento real, ele vira risco de interpretação em vez de ajuda.
