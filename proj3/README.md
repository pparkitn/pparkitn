# Attractiveness Bias — A/B Test at Scale

**Randomized controlled trial** exploring whether profile-photo attractiveness affects LinkedIn connection acceptance — behavioral bias in professional networks, measured.

## Overview
This project investigates whether profile-photo attractiveness influences connection acceptance rates on LinkedIn through a randomized controlled trial (RCT) design. The study eliminates confounding factors by controlling for profile completeness, headline, summary, and network overlap.

## Challenge
- **RCT design eliminating confounding factors**: Profiles were matched on all observable characteristics except photo attractiveness
- **Statistical inference**: Proper hypothesis testing with sufficient statistical power

## Stack
- `R`
- `RCT`
- `Statistical Inference`

## Methodology
1. **Profile creation**: Matched pairs of profiles with identical professional backgrounds
2. **Photo assignment**: One profile per pair received an "attractive" photo, the other a "less attractive" photo
3. **Connection requests**: Identical connection requests sent to target users
4. **Measurement**: Connection acceptance rate as primary outcome
5. **Analysis**: Logistic regression with clustered standard errors

## Results
See [Final Report](Final_Report.pdf) and [Final Presentation](Final_Presentation.pdf) for detailed methodology, statistical analysis, and findings.

## Artifacts
- `Final_Report.pdf` — Full statistical report
- `Final_Presentation.pdf` — Slide deck summary
- `pics/img1.png` — Experiment visualization