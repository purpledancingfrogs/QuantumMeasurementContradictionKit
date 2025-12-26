# FAQ

## Is this a physics-accurate simulator?
No. QMCK is intentionally a toy-model sandbox built to surface where assumptions diverge.

## What does "contradiction-preserving" mean?
The toolkit avoids baking in a single resolution. When two descriptions rely on mutually incompatible assumptions
(e.g., unitary evolution vs. definite collapse), the mismatch is made explicit (flags/notes) instead of hidden.

## What is the intended use?
Education, demos, and structured comparison of assumptions across interpretations.

## Where do outputs go?
- examples/sample_report.json for a concrete, committed reference output
- runs/ for local runs (often ignored by git)