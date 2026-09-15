# ADR-003 — IA baseada em snapshot autorizado

**Status:** Accepted

## Contexto

Uma IA analítica precisa de contexto do negócio, mas acesso direto ao banco aumenta superfície de ataque, risco de vazamento e dificuldade de aplicar RBAC.

## Decisão

A aplicação produz um snapshot estruturado depois de aplicar tenant, role e minimização de PII. O modelo recebe somente esse snapshot e a pergunta.

## Consequências

- autorização continua determinística no backend;
- menor risco de prompt injection resultar em data exfiltration;
- contexto menor e mais barato;
- algumas perguntas exigem novos analytics explícitos no backend.
