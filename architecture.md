# Arquitetura

## Contexto

O Axis Core é uma plataforma SaaS para operações de serviços com agenda, clientes, profissionais, financeiro, fluxo público de agendamento, billing e uma camada de IA.

A aplicação foi organizada como um **modular monolith**: uma API com módulos bem definidos compartilhando o mesmo banco relacional. Para o estágio atual do produto, isso reduz complexidade operacional sem impedir separação de responsabilidades.

## Componentes conceituais

```mermaid
flowchart TB
    subgraph Clients
      WEB[Administrative Web App]
      BOOK[Public Booking]
      PORTAL[User Portals]
    end

    subgraph Backend[Application API]
      AUTH[Auth / Sessions]
      TENANT[Tenant + RBAC]
      SCHED[Scheduling]
      CRM[Customer / Service Domain]
      FIN[Financial Domain]
      BILL[Billing Integration]
      AI[AI Orchestration]
      OPS[Operations]
    end

    DB[(PostgreSQL)]
    PAY[Payment Provider]
    LLM[LLM Provider]

    WEB --> AUTH
    BOOK --> SCHED
    PORTAL --> TENANT

    AUTH --> TENANT
    TENANT --> SCHED
    TENANT --> CRM
    TENANT --> FIN
    TENANT --> BILL
    TENANT --> AI

    SCHED --> DB
    CRM --> DB
    FIN --> DB
    BILL --> DB
    AI --> DB
    OPS --> DB

    BILL --> PAY
    AI --> LLM
```

O diagrama é propositalmente de alto nível. Nomes de serviços, rotas, filas, jobs, tabelas e infraestrutura comercial não são publicados neste case.

## Por que modular monolith

Microservices adicionariam custos de observabilidade, deploy, consistência distribuída e infraestrutura antes de existir uma necessidade clara de escalabilidade independente por domínio.

No estágio atual, a prioridade é:

1. fronteiras de domínio claras;
2. regras críticas protegidas por invariantes transacionais;
3. integrações encapsuladas;
4. migrations reproduzíveis;
5. testes automatizados;
6. capacidade de extrair serviços futuramente se métricas justificarem.

## Requisições multi-tenant

Toda operação autenticada parte de um usuário e um tenant. O backend valida o vínculo do usuário e produz um contexto de autorização.

```mermaid
flowchart LR
    TOKEN[Session] --> USER[User]
    USER --> MEMBERSHIP[Membership]
    MEMBERSHIP --> TENANT[Tenant]
    MEMBERSHIP --> ROLE{Role}
    ROLE -->|ADMIN| GLOBAL[Tenant scope]
    ROLE -->|MEMBER| LIMITED[Restricted scope]
```

## Agenda e concorrência

A disponibilidade é checada na aplicação para gerar mensagens amigáveis, mas a integridade final pertence ao banco.

```text
App validation -> transaction -> database invariant -> commit
```

Se duas requisições concorrentes tentarem reservar o mesmo recurso no mesmo intervalo, apenas uma deve persistir.

## Deploy

Frontend e backend são entregues separadamente. O processo de release inclui migrations antes da nova versão da API assumir tráfego.

```mermaid
flowchart LR
    SRC[Source Control] --> BUILD[Build Pipeline]
    BUILD --> MIG[Database Migrations]
    MIG --> API[API Service]
    API --> DB[(PostgreSQL)]
    BUILD --> FE[Web Frontend]
```
