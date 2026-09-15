# Observabilidade e Operations Console

Um SaaS não termina quando a feature funciona no happy path. Em produção, também é necessário diagnosticar rapidamente falhas e inconsistências sem depender de alterações manuais no banco.

Por isso o produto possui uma console interna de operações com acesso restrito.

## Diagnósticos

O case expõe apenas categorias gerais de sinais observados, como:

- saúde da aplicação e dependências;
- erros técnicos recentes;
- estado de integrações externas;
- inconsistências de domínio;
- eventos assíncronos pendentes;
- métricas técnicas de uso.

Detalhes de regras, thresholds, nomes internos e fluxos comerciais foram omitidos.

## Ações administrativas seguras

O objetivo é reduzir intervenções diretas em dados de produção. Ações administrativas passam por fluxos específicos, com validação, autorização e auditoria.

Exemplos conceituais:

- diagnóstico de estado;
- reconciliação com serviços externos;
- recuperação controlada de sessões;
- reparo de inconsistências de domínio;
- reprocessamento seguro de eventos.

## Auditoria

Ações sensíveis registram contexto suficiente para rastreabilidade, sem armazenar secrets ou conteúdo desnecessário.

```text
action + actor + tenant + reason + timestamp + result
```

A imagem abaixo foi sanitizada e usa dados de demonstração.

![Operations Console sanitizada](screenshots/support-console.png)
