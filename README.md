# AfrigrantPipeline | Engineering Portfolio

**Research funding discovery · Explainable opportunity screening · MABRIG Technologies**

[Product website](https://www.afrigrantpipeline.com) · [Developer profile](https://github.com/mabrig1) · [Contact](https://www.mabrigkorie.org)

AfrigrantPipeline focuses on academic funding and opportunity discovery. This portfolio illustrates relevant engineering concepts without exposing the original implementation or confidential applicant information.

## Explore the portfolio

- [Conceptual architecture](docs/architecture.md)
- [Engineering case study](docs/case-study.md)
- [Interactive fictional scholarship screening demonstration](demo/index.html) — download and open locally.
- [Independent Python eligibility example](demo/matching.py)
- [Automated tests](demo/test_matching.py)
- [CI workflow](.github/workflows/demo.yml)

## Reproduce the example

```sh
python demo/matching.py
python -m unittest discover -s demo -v
```

Python 3.10+; no dependencies or keys. The sample distinguishes potential matches, mismatches and missing eligibility information using fictional records. It does not retrieve live opportunities, process CVs, invoke AI or guarantee funding. Production capabilities and availability are not independently verified here.

## Engineering competencies

Explainable filtering, data validation, uncertainty handling, provenance-aware system design, privacy boundaries and automated testing.

## Intellectual property and technical review

See [NOTICE.md](NOTICE.md). Production source, proprietary ranking, applicant data and payment infrastructure are excluded. Recruiters and collaborators can contact MABRIG Technologies for a guided demonstration or scoped technical discussion.
