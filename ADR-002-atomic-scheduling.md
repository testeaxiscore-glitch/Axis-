# ADR-002 — Integridade atômica da agenda

**Status:** Accepted

## Contexto

Duas requisições simultâneas podem observar o mesmo horário como disponível antes que qualquer uma faça commit.

## Decisão

Manter validação no serviço para UX e adicionar uma `EXCLUDE CONSTRAINT` no PostgreSQL para impedir interseção de intervalos ativos do mesmo profissional.

## Consequência

O banco se torna a última linha de defesa contra double booking. A API traduz violações da constraint para conflito de domínio.
