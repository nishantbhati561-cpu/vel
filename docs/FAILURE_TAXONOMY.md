# Failure Taxonomy

## Known Failure Modes
1. **Localization Failure:** Agent edits the wrong file.
2. **Understanding Failure:** Agent edits the right file but misunderstands the bug.
3. **Hypothesis Failure:** Agent makes a bad assumption about the fix.
4. **Implementation Failure:** Syntax errors or logic errors in the patch.
5. **Test Selection Failure:** Agent validates using irrelevant tests.
6. **Regression:** Patch breaks existing tests.
7. **Tool Usage:** Agent fails to correctly use harness tools or hits token limits.
