# Revision Notes

**Data da revisão:** 15/10/2026

## Resumo

Este repositório foi revisado após testes adicionais que refinaram a
narrativa inicial. Três hipóteses foram refutadas e cinco achados
foram consolidados. As mudanças estão documentadas abaixo.

## Hipóteses refutadas

### 1. Variação continental da skewness
A análise inicial sugeria skewness diferente por continente.
Controle com 343 estações terrestres mostrou que era **viés de
amostragem**, não efeito geográfico.

### 2. Modulação solar direta (F10.7)
A correlação r=0.91 entre skewness e F10.7 na população bruta era
**confound de população** (Starlink entrando após 2019). Com
população fixa (4.108 satélites), a correlação cai para r=−0.13
(não significativa).

### 3. ML preditivo
Gradient Boosting e Random Forest **não superam regressão linear**
para prever skewness. Três limitações estruturais:
- Regime change em 2024-25 não é predizível
- Viés por banda (leave-band-out R²=−125)
- Amostra temporal pequena (n=12 anos)

## Achados consolidados

### 1. Fingerprint orbital
Skewness é propriedade da classe orbital:
- SSO: +1.37
- Polar: −0.55
- Inclinada: −0.34
- Equatorial: +0.35

### 2. Driver é a componente RADIAL do campo geomagnético
Validação dupla independente:
- Swarm in-situ: r = −0.67 (p = 0.0003)
- CHAOS-7 modelo: r = −0.61 (p = 0.0015)
- Concordância entre fontes: r = +0.81

Refutados como driver:
- Módulo |B|: r = −0.21 (n.s.)
- Dipolo puro: r = −0.38 (n.s.)
- Anomalia (grau 2-20): r = −0.41 (p = 0.04)

### 3. Tomografia multi-banda
11 bandas (550–1550 km) analisadas. Colapso oscilatório:
- Banda 1150 km: −2.34 (mais forte)
- Banda 850 km: −1.88
- Banda 550 km: **+0.88** (invertida — saturação)

### 4. Saturação em 550 km
Skewness vai de **−2.43 (2014)** para **−0.05 (2025)**.
Bootstrap 2.000×: IC 95% não se sobrepõem.

### 5. Migração de banda acelerando
0.85% (2019) → 14.9% (2025). 17× de aumento. Coincide com
máximo solar 25.

## O que mudou nos artefatos

| Arquivo | v1 | v2 |
|---|---|---|
| README.md | "colapso da skewness" | "B_C radial é o driver" |
| Dashboard | narrativa de colapso | validação dupla Swarm+CHAOS |
| One-pager | números antigos | precisa regenerar |
| E-mails comerciais | números antigos | precisa follow-up |

## Como citar

A versão atual é v2. O DOI 10.5281/zenodo.23376365 aponta para
a release v0.1.0 original, que contém a narrativa preliminar.
Uma release v0.2.0 será publicada com a narrativa revisada.
