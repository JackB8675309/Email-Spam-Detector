# ML Phishing Email Detector

CSCE 478 (Intro to Machine Learning), Fall 2026 course project, team of 2.
Binary classification: given an email, predict **phishing** vs **legitimate**.

---

## 1. One-time setup (each teammate)

Requires **Python 3.12 or 3.13** (the pinned numpy needs ≥ 3.12). Check with `python3 --version`.

**macOS / Linux**
```bash
cd phishing-email-detector
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name phishing-detector --display-name "Python (phishing-detector)"
nbstripout --install          # run once after cloning; keeps notebook outputs out of commits
```

**Windows (PowerShell)**
```powershell
cd phishing-email-detector
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ipykernel install --user --name phishing-detector --display-name "Python (phishing-detector)"
nbstripout --install
```

Then start Jupyter with `jupyter lab` and pick the **Python (phishing-detector)** kernel.

Every time you come back to work: `source .venv/bin/activate` (or `.venv\Scripts\Activate.ps1`).

### Kaggle credentials (for the dataset download)
1. kaggle.com → Settings → API → **Create New Token** (downloads `kaggle.json`).
2. Move it to `~/.kaggle/kaggle.json` (Windows: `C:\Users\<you>\.kaggle\kaggle.json`).
3. Never commit it; it's already in `.gitignore`.

---

## 2. Dataset

**Proposed:** [`ethancratchley/email-phishing-dataset`](https://www.kaggle.com/datasets/ethancratchley/email-phishing-dataset): ~500K real legitimate emails (Enron) + ~20K real phishing/safe emails, already passed through an NLP feature-extraction pipeline.

**Status: needs team and instructor sign-off.** Before committing, check:
- exactly which features are included (TF-IDF? indicator flags like links/urgency?) vs raw text
- size: 500K+ rows may need a subsample
- class imbalance (~25:1): affects metric choice (accuracy alone is misleading) and resampling

Data lives in `data/raw/` locally and is **git-ignored**; each teammate downloads their own copy.
Anything derived goes in `data/processed/` (also ignored), so preprocessing must be reproducible from the notebook.

---

## 3. Project layout

```
phishing-email-detector/
├── data/
│   ├── raw/              # original Kaggle download (git-ignored)
│   └── processed/        # cleaned / split data (git-ignored)
├── notebooks/            # main analysis notebook(s), submitted to teaching staff
├── src/                  # reusable helper code, if notebooks get long
├── models/               # saved trained models (git-ignored)
├── reports/figures/      # plots exported for the paper (committed)
├── paper/                # ACM double-column final report (≤ 4 pages)
├── requirements.txt      # pinned package versions (both teammates use the same)
└── .python-version       # 3.12
```

---

## 4. Team workflow (GitHub)

- `main` stays working. Do work on a branch (`git checkout -b eda`, `git checkout -b naive-bayes`, …) and open a PR for your partner to look at.
- **Notebooks merge badly.** Avoid both editing the same notebook at once: split by section or use one notebook each and combine later.
- `nbstripout` removes cell outputs on commit, so diffs stay readable. Re-run the notebook to see outputs.
- Adding a package? `pip install x`, add it **with its version** to `requirements.txt`, commit, and tell your partner to re-run `pip install -r requirements.txt`.
- Fix the random seed (e.g. `random_state=42`) everywhere so you both get the same splits and scores.

---

## 5. Rubric checklist

| # | Section | Pts | Must cover |
|---|---|---|---|
| 1 | Problem definition & data understanding | 10 | source, target, task type, features, size, data-quality concerns, why ML |
| 2 | Preprocessing & EDA | 15 | missing values, duplicates, encoding, scaling, outliers, feature selection, EDA, train/test split, **data leakage prevention**, *why* for every decision |
| 3 | Model development | 20 | **≥ 2 models**: why chosen, assumptions, key hyperparameters, **tuning** (defaults only ≠ full credit), same split for both |
| 4 | Evaluation & comparison | 20 | multiple justified metrics, train vs test, over/underfitting, tables/plots, trade-offs, final recommendation |
| 5 | Peer review | 5 | 2+ strengths, 2+ improvements, are conclusions supported, 1 specific suggestion |
| 6 | Final report | 30 | ≤ 4 pages ACM format: problem, dataset, models, setup, results, selection, error analysis, improvements, **task distribution**, **AI usage acknowledgement** |

## 6. Key dates

| Date | What |
|---|---|
| Oct 18 (Sun) 11:59pm CT | Share dataset, notebook & materials with teaching staff |
| Week 12 | Mandatory 30-min team check-in with teaching staff |
| Nov 24 (Tue), in class | Peer review of draft code/report |
| Dec 1 (Tue) 11:59pm CT | Final version ready for instructor evaluation |
| Dec 6 (Sun) 11:59pm CT | Final report PDF due |

## 7. Open decisions

- [ ] Confirm dataset (team + instructor)
- [ ] Pick the 2+ models (candidates: Multinomial Naive Bayes, Logistic Regression, Random Forest)
- [ ] Task split between teammates (needed for the paper's task-distribution section)
- [ ] Create GitHub repo and add partner as collaborator
