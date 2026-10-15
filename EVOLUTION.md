# Vias de Evolução do thermoLEO

Documento revisado em 15/10/2026 após a consolidação dos achados.

## 1. Resolução temporal

**Status:** implementado em resolução mensal (1.600 células).

**Resultados:**
- ML mensal atinge R²=0.42 em LOO por ano
- Regime change 2024-25 confirmado (R²=0.01 fora da amostra)
- Resolução mensal é o teto — abaixo disso, ruído domina

**Próximo passo:** capturar tempestades geomagnéticas individuais
(resolução diária) requer corrigir por regime.

## 2. Expansão do espectro de altitude

**Status:** implementado como tomografia multi-banda (11 bandas,
550–1550 km).

**Resultados:**
- Colapso oscilatório em todas as bandas
- Banda 1150 km: -2.34 (mais forte)
- Banda 550 km: +0.88 (invertida — saturação)
- 10/11 bandas com slope positivo pós-2020

**Próximo passo:** correlacionar cada banda com B_C do CHAOS-7
para isolar dependência em altitude.

## 3. Complexidade preditiva (ML)

**Status:** testado. ML não supera regressão linear.

**Limitações estruturais identificadas:**
- Regime change 2024-25 não é predizível com features disponíveis
- Viés por banda (leave-band-out R²=-125)
- Amostra temporal pequena (n=12 grupos independentes)

**Conclusão:** o sinal é observacional, não preditivo. Skewness
deve ser tratada como proxy físico, não target de ML.

## 4. Interpolação vertical

**Status:** validado com Swarm (in-situ) e CHAOS-7 (modelo).

**Resultados:**
- Swarm B_C: r = -0.67 (p = 0.0003)
- CHAOS-7 B_C: r = -0.61 (p = 0.0015)
- Magnitude |B|: r = -0.21 (n.s.)
- Dipolo puro: r = -0.38 (n.s.)
- Anomalia: r = -0.41 (p = 0.04)

**Conclusão:** o driver é a componente RADIAL do campo
geomagnético (B_C), não a magnitude nem harmônicos isolados.

**Próximo passo:** interpolar entre 550 km (saturado) e 1150 km
(colapso máximo) para reconstruir perfil vertical da termosfera.

## Como citar

DOI: 10.5281/zenodo.23376365
GitHub: https://github.com/Nat699/thermoLEO
