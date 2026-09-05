# Climate Resiliency and Digital Sovereignty Learning Lab

A complete three-pathway workshop for OLC learners and instructors, connecting public environmental data, agricultural questions, interpretation and data stewardship. The regional example concerns Pine Ridge and the White River watershed.

**Opening question:** How can regional drought and streamflow records help frame questions about livestock water availability, and what additional local evidence would we need?

Teams may instead frame a question about grazing, gardens, plant resources or watershed stewardship. Regional drought and streamflow provide context; they do not establish pasture condition, drinking-water quality, irrigation supply or a management threshold.

## Learning objectives

By the end of the hackathon, students should be able to:

1. **Frame a relevant question** about climate, agriculture or natural-resource stewardship and explain why it interests them.
2. **Use their selected notebook pathway** to explore environmental data, documenting what they tried and any challenges encountered.
3. **Interpret and communicate evidence**, explaining the source, location, time period and meaning of any results or visualizations they present.
4. **Recognize limitations and uncertainty**, distinguishing what the data show from what would require additional evidence.
5. **Propose a future project**, identifying a next question and the data, skills or partnerships needed to pursue it.
6. **Describe potential community benefits** and explain who might find the work useful.
7. **Identify appropriate reviewers or collaborators** and explain how their perspectives could improve interpretation and guide responsible sharing.

These objectives apply across all three tracks. Students demonstrate learning through their final presentations and explanations of completed or attempted work; a finished visualization is not required.

## Choose a pathway

| Pathway | Time | Activity | Learner product |
| --- | --- | --- | --- |
| [Guided Explorer](tracks/01_guided_explorer.ipynb) | 90 minutes | Read a prepared regional drought record | Figure interpretation, limitation and stewardship record |
| [Data Investigator](tracks/02_data_investigator.ipynb) | Half day | Compare gauges, periods and illustrative weights | Evidence comparison and explanation of a value choice |
| [Technical Extender](tracks/03_technical_extender.ipynb) | Half day or extension | Validate low-flow methods, estimators and provenance | Reproducible method comparison and documented limitations |

These tracks are the complete workshop; no additional reference notebook is required. Beginners start with Guided Explorer. Students stay with one chosen track; these are parallel pathways, not a sequence. Shared instruction takes 15–20 minutes, followed by 5–10 minutes of track orientation, then supported project work. For September 15–16, Lilly Jones leads 8½ hours of hackathon activity. See the [event agenda and facilitation outline](guides/event_schedule.md) for the supplied schedule, team milestones and final-session plan.

## Start here

```sh
conda env create -f environment.yml
conda activate ed-py
python scripts/check_environment.py
jupyter lab
```

Open [readiness](onboarding/00_readiness_check.ipynb), then the chosen track. The core environment supports all three tracks. Installation requires internet; the prepared-data activities run offline afterward. The optional data-refresh script requires internet and should be run by instructors before an event, not by every learner.

The included snapshots have a dated [manifest](data/sample_or_fallback/manifest.json). Run `python scripts/verify_snapshots.py` before class. These are historical source snapshots, not current conditions. Never replace missing observations with zero.

## Learning and OLC NIFA alignment

The activities support environmental data literacy, experiential learning, instructor capacity and responsible stewardship. [Alignment and assessment](guides/alignment_and_assessment.md) maps learning aims to activities and evidence. This is a proposed curriculum mapping; OLC must map it to the actual approved award objectives before using it as grant reporting evidence.

Students prepare a [seven-question final presentation](guides/final_presentation.md) about their question, learning, created or attempted work, uncertainty, future projects, potential beneficiaries and reviewers. Any visualizations should include source, place, period and meaning; a finished visualization is not required. Keep the practical [stewardship record](templates/stewardship_record.md) in agreed class storage. No culturally sensitive knowledge is required to complete the lesson. Cultural reflection prompts should use locally selected framing and can be replaced or declined.

## Workshop use

Use teams of 3–5 and rotate navigator, driver, data steward, interpreter and recorder roles. Spoken, typed, drawn or assisted responses are welcome. Follow [accessibility guidance](guides/accessibility.md) and the [beginner cell guide](guides/beginner_cell_guide.md).

The core analysis intentionally uses public-source climate and gauge data. It provides evidence for discussion, not a validated watershed health score, official emergency threshold or causal climate attribution. The investigator's component scores are explicitly illustrative; they are not environmental measurements.

Generated results remain classroom drafts until the intended use and appropriate review are established. [Governance guidance](guides/data_governance.md) prioritizes local authority; framework references do not establish Tribal adoption or endorsement.

## Instructor resources

- [Instructor guide and schedules](guides/instructor_guide.md)
- [Learner quickstart](guides/learner_quickstart.md) and [glossary](guides/glossary.md)
- [Assessment rubric](guides/alignment_and_assessment.md) and [lesson adaptation](templates/instructor_adaptation.md)
- [Troubleshooting](guides/troubleshooting.md), [data policy](data/README.md), and [validation](validation.md)

Code and original instructional text use [LICENSE](LICENSE). Cite the resource using [CITATION.cff](CITATION.cff) and cite each source dataset separately. Funding acknowledgments and award numbers must come from the approved award; none are inferred here.
