# Conceptual architecture

```mermaid
flowchart LR
 A[Opportunity metadata] --> B[Eligibility checks]
 C[Synthetic applicant profile] --> B
 B --> D[Explainable shortlist]
 D --> E[Human review of official criteria]
```

This is an illustrative architecture, not a verified production topology. Private ingestion pipelines, CV processing, ranking logic, credentials and payment infrastructure are excluded. Unknown eligibility requirements must remain unknown until checked against official sources.
