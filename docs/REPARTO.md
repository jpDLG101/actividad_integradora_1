# Reparto del trabajo

Principio: **todos hacen de todo**. Cada persona implementa un algoritmo (código + tests + su sección en `ALGORITMOS.md`), es dueña de una pieza transversal y revisa el PR de otra persona.

| Issue | Persona | Algoritmo | Pieza transversal | Revisa el PR de |
|---|---|---|---|---|
| #1 | Ricky | KMP (Parte 1) | `io_utils.py` + archivos de ejemplo | Jp |
| #2 | Jp | Manacher (Parte 2) | `main.py` | Fabian |
| #3 | Fabian | Substring común con KMP (Parte 3) | README, ARQUITECTURA y prueba end-to-end | Ricky |

## Dependencias
- C usa `kmp.prefix_function` de A: programar contra la firma de `ARQUITECTURA.md` y hacer rebase cuando el PR de A esté en `main`.
- B necesita las 3 funciones para el `main.py` final: al inicio usa stubs que devuelven valores fijos.

## Flujo
1. Una rama por issue: `parte-1-kmp`, `parte-2-manacher`, `parte-3-lcs`.
2. PR referenciando el issue (`Closes #N`), con al menos 1 aprobación de quien revisa.
3. Commits chicos y con mensaje claro.
4. No se cambian firmas sin actualizar `ARQUITECTURA.md` y avisar al equipo.

## Orden sugerido de merges
A (KMP + io) → B (Manacher + main) → C (LCS + docs finales).
