# Architecture

## Primary Conceptual Flow
```
          ISSUE
            |
            v
    ISSUE UNDERSTANDING
            |
            v
    HYBRID RETRIEVAL
      /     |     \
 lexical semantic tests
            |
            v
    CANDIDATE RANKING
            |
            v
    GRAPH EXPLORATION
            |
            v
      CODE EVIDENCE
            |
            v
    ROOT-CAUSE MODEL
            |
            v
      PATCH PLANNER
            |
            v
       MINIMAL EDIT
            |
            v
       TARGETED TEST
            |
       +----+----+
       |         |
     PASS      FAIL
       |         |
       v         v
   REGRESSION DIAGNOSE
       |         |
       +----<----+
            |
            v
      PATCH HYGIENE
            |
            v
      SUBMIT PATCH
```

## Guiding Principles
- Hybrid localization over single-modality.
- Adaptive time budget based on task difficulty.
- Minimal edits over refactoring.
