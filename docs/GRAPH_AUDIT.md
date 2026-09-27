# Graph Audit

## Overview
Investigation of the provided code graphs (`graphs/`) to determine their utility for localization.

## Metrics to Audit
- **Coverage:** How completely the graphs map the target repositories.
- **Node Missing Rate:** Which files/classes are often missed.
- **Noise:** Erroneous edges.
- **Multi-Hop Utility:** Is looking 2-hops away useful or distractive?
- **Alignment:** Do embeddings align well with structural graph neighbors?
