# MCP Rebuild Plan

Plano técnico de reconstrução da camada MCP da Blue Ocean para operação always-on no host do OpenClaw.

## Status atual
### Confirmado
- o OpenClaw atual não tem MCPs configurados
- os endpoints locais antigos não estão respondendo
- não há dependência operacional de `.mcp-servers/` neste host
- a documentação de uso e a lógica analítica continuam válidas
- o bloqueio atual é infraestrutura, não arquitetura do brain

## Objetivo da reconstrução
Restaurar capacidade de análise em tempo real para:
- Meta Ads
- Kommo
- Google Sheets

Sem depender de notebook local, scripts manuais de sessão ou diretórios ocultos não versionados.

## Estratégia escolhida
### Princípio
Reaproveitar implementações MCP existentes quando forem maduras o suficiente, e complementar com camada própria da Blue Ocean apenas onde houver lacuna crítica.

### Motivo
Isso reduz tempo de reconstrução, diminui risco de bugs evitáveis e acelera a volta da capacidade operacional live.

## Candidatos identificados
### 1. Meta Ads
Candidato encontrado:
- `https://github.com/pipeboard-co/meta-ads-mcp`

Leitura inicial:
- projeto maduro
- suporte a local self-hosted e remote MCP
- escopo forte para campanhas, ad sets, anúncios, insights e criativos
- parece bom candidato para bootstrap rápido da camada Meta

Risco principal:
- confirmar se a leitura de eventos e estruturas necessárias para Blue Ocean cobre bem o uso de CTWA, promoted object e cruzamentos relevantes para o nosso diagnóstico

### 2. Kommo
Candidato encontrado:
- `https://github.com/NatrixAi/kommo-mcp`

Leitura inicial:
- cobre leads, contatos, empresas, tarefas, pipelines, usuários, campos customizados, tags e eventos
- parece suficiente para leitura operacional e reconciliação inicial

Risco principal:
- confirmar profundidade analítica para relatórios mais específicos da operação Blue Ocean
- confirmar se lida bem com custom fields, responsible user, filtros úteis e volume operacional real

### 3. Google Sheets
Candidato encontrado:
- `https://github.com/xing5/mcp-google-sheets`

Leitura inicial:
- projeto relativamente completo
- já traz ferramentas de leitura, escrita, listagem e operações em lote
- bom fit para uso como camada operacional derivada

Risco principal:
- precisa configuração cuidadosa para evitar excesso de ferramentas e custo de contexto

## Arquitetura recomendada para implantação
### Modelo base
No mesmo host do OpenClaw:
- `kommo-mcp` em `127.0.0.1:3001`
- `meta-ads-mcp` em `127.0.0.1:3002`
- `google-sheets-mcp` em `127.0.0.1:3003`

### Gerenciamento
- processo persistente por `systemd`
- reinício automático em falha
- logs separados por serviço
- bind em loopback sempre que possível

### Integração
Configurar o OpenClaw para consumir os 3 MCPs nativamente.

## Segredos e credenciais necessários
### Meta Ads
Necessário confirmar e provisionar:
- Meta access token ou fluxo OAuth compatível com o servidor escolhido
- app/client config se o modo self-hosted exigir aplicação própria
- ad account IDs relevantes

### Kommo
Necessário confirmar e provisionar:
- `KOMMO_SUBDOMAIN`
- `KOMMO_TOKEN` de longo prazo ou credencial equivalente

### Google Sheets
Necessário confirmar e provisionar:
- service account JSON ou OAuth config
- `DRIVE_FOLDER_ID` padrão, se fizer sentido operacionalmente
- acesso compartilhado às planilhas necessárias

## Ordem de implantação recomendada
### Fase 1. Prova de vida por serviço
Objetivo: validar que cada MCP sobe e responde isoladamente.

Ordem sugerida:
1. Google Sheets, porque costuma ser o mais previsível
2. Kommo, porque a autenticação é relativamente direta
3. Meta Ads, porque tende a ser o mais sensível a app config e escopo

### Fase 2. Fixar runtime always-on
Para cada serviço:
- criar diretório limpo de runtime
- instalar dependências
- criar `.env` ou environment file fora do repositório público
- criar unit file de `systemd`
- validar subida após reboot de serviço

### Fase 3. Configurar no OpenClaw
Depois dos três responderem, configurar:
- `openclaw mcp set ...` para cada um
- validar `openclaw mcp list`
- validar uso real pelo agente

### Fase 4. Validação analítica Blue Ocean
Rodar uma leitura real cruzando:
- spend e entrega na Meta
- leads e campos no Kommo
- complemento operacional no Sheets

Só considerar a pilha pronta quando isso funcionar de ponta a ponta.

## Critérios de aceite por MCP
### Google Sheets
- listar planilhas acessíveis
- ler aba e intervalo específicos
- escrever teste controlado se necessário

### Kommo
- listar pipelines
- listar leads recentes
- ler campos customizados relevantes
- identificar responsible users / SDRs

### Meta Ads
- listar contas e campanhas
- ler insights por campanha e ad set
- identificar sinais necessários para diagnóstico
- confirmar cobertura para eventos customizados ou dados necessários para descobrir o evento correto

## Decisão sobre build próprio vs reaproveitamento
### Recomendação atual
Adotar estratégia híbrida:
- começar por servidores existentes para recuperar capacidade live mais rápido
- construir camada própria Blue Ocean só se surgirem lacunas reais

### Quando construir MCP próprio
Só vale construir MCP próprio se acontecer pelo menos um destes cenários:
- servidor existente não expõe dados críticos para o modelo analítico Blue Ocean
- autenticação do projeto externo for frágil ou inviável no VPS
- manutenção externa for instável demais
- precisarmos normalizar ferramentas e nomenclaturas de forma específica da operação

## Próxima ação prática
A próxima etapa deve ser preparar um inventário de implantação para cada MCP com:
- runtime recomendado
- dependências
- variáveis de ambiente
- comando de execução
- forma de healthcheck
- formato de configuração no OpenClaw

Esse inventário será a ponte entre arquitetura e deploy real.
