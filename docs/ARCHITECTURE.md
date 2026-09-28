# Architecture Document

## System Flow

                    ISSUE
                      |
                      v
              ISSUE UNDERSTANDING
                      |
                      v
             HYBRID RETRIEVAL
        /       |       |        \
 lexical    semantic   tests    symbols
        \       |       |        /
                 v
          CANDIDATE RANKING
                 |
                 v
          GRAPH EXPLORATION
           /            \
      neighbors       subgraph
           \            /
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
          +------+------+
          |             |
        PASS           FAIL
          |             |
          v             v
     REGRESSION     DIAGNOSE
          |             |
          |       UPDATE HYPOTHESIS
          |             |
          +------<------+
                 |
                 v
             FINAL DIFF
                 |
                 v
           PATCH HYGIENE
                 |
                 v
            SUBMIT PATCH

Wrapped around this is the ADAPTIVE BUDGET CONTROLLER.
