# MCP Architecture for Always-On Analysis

Arquitetura alvo para tornar o agente Blue Ocean capaz de analisar Meta Ads, Kommo e Google Sheets em tempo real sem depender de uma máquina local ligada.

## Objetivo
Garantir que o agente consiga:
- consultar dados reais de mídia, CRM e planilhas operacionais
- cruzar topo, meio e fundo de funil em tempo real
- operar de forma estável no VPS onde o OpenClaw roda
- evitar dependência de scripts locais, localhost de notebook ou sessão manual

## Diagnóstico do modelo anterior
O repositório original assumia:
- MCPs locais rodando em `localhost`
- pasta `.mcp-servers/` presente no ambiente
- start manual via `./start-mcps.sh`
- sessão do agente reiniciada após mudanças

Esse modelo não atende o objetivo atual porque:
- os servidores locais não estão presentes no host atual
- a infraestrutura depende de ambiente local específico
- a disponibilidade não é garantida
- o agente fica sem leitura live quando a base local some

## Arquitetura alvo
### Camada 1. Serviços MCP always-on
Serviços persistentes no mesmo VPS do OpenClaw, ou em serviços de backend acessíveis de forma estável:
- `kommo-mcp`
- `meta-ads-mcp`
- `google-sheets-mcp`

Preferência inicial:
- rodar no mesmo host do OpenClaw
- bind em loopback
- expor apenas internamente para o próprio host
- gerenciar por `systemd`

### Camada 2. Credenciais centralizadas
Credenciais devem morar no servidor, não no laptop:
- Meta Ads API
- Kommo API/OAuth
- Google service account ou OAuth
- opcionais: Apify, n8n

Princípios:
- usar variáveis de ambiente ou arquivos `.env` fora do repositório público
- separar credencial por serviço
- permitir rotação sem reescrever o brain

### Camada 3. Integração OpenClaw
O OpenClaw deve consumir os MCPs via configuração nativa:
- `openclaw mcp set`
- `openclaw mcp list`
- `openclaw mcp show`

Modelo preferido:
- OpenClaw apontando para URLs estáveis do próprio host, por exemplo `http://127.0.0.1:3001/mcp`
- MCPs tratados como infraestrutura do ambiente, não como detalhe do workspace

## Fonte de verdade por MCP
### Meta Ads MCP
Responsável por:
- campanhas, ad sets, ads, criativos
- spend, CTR, CPM, CPC, frequência
- insights por conta, campanha, conjunto e anúncio
- breakdowns por placement, age, gender

### Kommo MCP
Responsável por:
- leads, pipelines, SDRs, closers, motivos de perda
- performance de SDR e funil
- lead real versus lead fantasma
- cruzamento de source IDs, pipelines e campos customizados

### Google Sheets MCP
Responsável por:
- planilhas operacionais derivadas
- reuniões marcadas, realizadas, qualificadas
- fechamentos e valor quando a operação usar planilha como camada complementar

Regra transversal:
- Sheets ajuda a consolidar e enriquecer
- Kommo prevalece sobre Sheets em caso de conflito de CRM
- plataforma prevalece para spend e entrega

## Requisitos não funcionais
A arquitetura deve ser:
- always-on
- reiniciável automaticamente
- independente de notebook local
- observável com healthcheck simples
- simples de reconfigurar quando credenciais mudarem
- segura o suficiente para não expor APIs desnecessariamente

## Estratégia de deploy recomendada
### Fase 1. Loopback-only no VPS
Primeira implementação recomendada:
- cada MCP rodando em `127.0.0.1`
- portas dedicadas
- `systemd` para manter ativo
- OpenClaw consumindo via loopback

Exemplo:
- `kommo-mcp` → `127.0.0.1:3001`
- `meta-ads-mcp` → `127.0.0.1:3002`
- `google-sheets-mcp` → `127.0.0.1:3003`

### Fase 2. Hardening e observabilidade
Depois de validar a operação:
- healthchecks por serviço
- logs estruturados
- restart automático
- opcional: reverse proxy interno se houver necessidade operacional real

## Ordem de reconstrução recomendada
1. Redescobrir ou reimplementar `kommo-mcp`
2. Redescobrir ou reimplementar `meta-ads-mcp`
3. Redescobrir ou reimplementar `google-sheets-mcp`
4. Validar cada um isoladamente
5. Integrar todos ao OpenClaw
6. Validar análise cross-MCP com período real

## Critério de pronto
A reconstrução só está pronta quando:
- OpenClaw listar os três MCPs configurados
- os três responderem via healthcheck básico
- o agente conseguir consultar Meta + Kommo + Sheets no mesmo período
- o agente conseguir produzir diagnóstico com confiança melhor do que Frágil

## Regra final
O agente principal não deve depender de uma máquina local ligada para realizar análises críticas da Blue Ocean.

A infraestrutura MCP precisa ser tratada como parte do sistema operacional do brain, não como acessório temporário de workspace.
