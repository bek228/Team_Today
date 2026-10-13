# FIN331 L15 WACC Card: Execution Guide

Oct 13, 2026 · @Ben

## Context block for another AI chat

Paste this block at the top of a new AI chat (or your coding agent) before asking for help. It gives the assistant everything it needs without the notebook.

```markdown
I'm a student in FIN331 (Data Analytics and AI for Finance) at Lehigh. Assignment: Lecture 15, "Teams, GitHub, and a WACC Starter Project."

SETUP: Our team (3-4 people) acts as a consulting firm. The CEO picks one real public company as the client. We build a "WACC card": a one-page Streamlit app showing the client's WACC, every input behind it, and the source for every input.

FORMULA: WACC = w_E * r_E + w_D * r_D * (1 - tax), where r_E = rf + beta * MRP.
- beta: estimated in code from 5 years of daily returns vs SPY, cov(Ri, Rm) / var(Rm)
- rf: 10-year Treasury yield (FRED DGS10 or Yahoo ^TNX), as of a named date
- MRP: a choice, typically 4-6%, must be justified
- r_D: yield on the firm's bonds, or rf + credit spread (interest expense / debt can mislead)
- tax: statutory 21% or effective (tax expense / pretax income)
- w_E, w_D: MARKET values (market cap and total debt), must sum to 1

REPO: created from the template https://github.com/LeDataSciFi/fin331-team-repo-template. Files:
- README.md: the plan (client, team, roles). Defines the output contract.
- AGENTS.md / CLAUDE.md: rules for agents (never commit to main, never force-push, never commit keys, only edit files your role owns, relative paths, quote every source in assumptions.csv).
- code/wacc.py: 3 TODO functions: get_returns(ticker), estimate_beta(rets, ticker), compute_wacc(beta, a). Reads inputs/assumptions.csv, writes outputs/wacc.csv.
- inputs/assumptions.csv: columns item,value,source. Items: rf, mrp, rd, tax, w_e, w_d. Values are decimals.
- outputs/wacc_FAKE.csv: placeholder with the same columns as the real output.
- app.py: the Streamlit card. Reads outputs/wacc.csv if it exists, else the FAKE file. Must only read files (no downloads, no estimation).
- requirements.txt: pandas, numpy, yfinance, streamlit.

OUTPUT CONTRACT (outputs/wacc.csv, one row, these columns in order):
ticker, asof, beta, rf, mrp, cost_of_equity, rd, tax, w_e, w_d, wacc

ROLES AND BRANCHES:
- CEO: README.md, creates repo, reviews and merges every PR (branch: main)
- Developer: code/wacc.py (branch: dev-wacc)
- Product manager: app.py (branch: pm-app)
- Analyst: inputs/assumptions.csv (branch: analyst-inputs)
- Team of 3: CEO is also the analyst.

WORKFLOW: branch -> commit -> push -> pull request -> teammate review -> CEO merges. Merge the analyst's PR BEFORE the developer's final run of wacc.py.

DONE WHEN: everyone has merged at least one PR, and `streamlit run app.py` shows the client's real WACC with sources. Repo link goes in the class Team Projects sheet by Thursday Oct 15 class.

MY ROLE: <fill in>. MY CLIENT TICKER: <fill in>. I'm on Windows using PowerShell and VS Code. Explain each git command before running it.
```

## Deliverables and definition of done

The only graded deliverable this week is your team's repo link in the Team Projects sheet by Thursday Oct 15 class; nothing goes to Coursesite. Thursday's final project kickoff (Lecture 16) builds on this same repo, and this team is your final project team.

| Wrap-up poll level | What it means | Target |
| --- | --- | --- |
| 1 | Repo exists and everyone can push | Tuesday in class |
| 2 | At least one PR merged | Tuesday in class |
| 3 | Every teammate has merged at least one PR | Tuesday in class |
| 4 | `streamlit run app.py` shows the client's real WACC with sources | By Thursday Oct 15 |

Also in the notebook, not graded but worth doing: Question 1 (sketch the card before coding) and Question 2 (the stale `wacc.csv` problem). Both are answered below.

## Master checklist

Work top to bottom; phases 4a to 4c run at the same time.

**Phase 0: Everyone, before or at the start of class**

- [ ] Git installed and identity set (`git --version`, `git config --global --list`)
- [ ] GitHub account exists, and its email matches your git config email
- [ ] Python works in PowerShell (`python --version`) and VS Code is installed
- [ ] A coding agent is available (Claude Code, Codex, or Copilot agent mode), or GitHub Desktop as backup
- [ ] Create a class folder outside System32, e.g. `C:\Users\<you>\Documents\FIN331`

**Phase 1: Form the team (10 min)**

- [ ] Pick 3 or 4 people; agree on target grade and weekly hours out loud
- [ ] Pick a team name
- [ ] Assign roles: CEO, Developer, Product manager, Analyst (CEO doubles as Analyst in a team of 3)
- [ ] Fill a row in the Team Projects sheet: team name, members, each GitHub username

**Phase 2: Agree on the output first (Question 1, laptops closed)**

- [ ] Sketch the WACC card on paper with every number
- [ ] Compare the sketch to the README column list; note what's missing either way
- [ ] Confirm nobody changes the `wacc.csv` columns without telling the team

**Phase 3: CEO sets up the repo (everyone watches)**

- [ ] Pick the client ticker (see Key decisions)
- [ ] Use this template at github.com/LeDataSciFi/fin331-team-repo-template; choose public or private
- [ ] Settings > Collaborators: add teammates and `donbowen`
- [ ] Teammates accept invitations
- [ ] Fill every `<...>` in README.md on github.com and commit directly to `main` (the only direct commit to main)
- [ ] Paste the repo link into the Team Projects sheet

**Phase 4: Everyone clones and branches**

- [ ] Clone the repo, create your branch (`dev-wacc`, `pm-app`, or `analyst-inputs`), publish it
- [ ] `pip install -r requirements.txt`
- [ ] Reopen VS Code in the repo folder and restart the agent so it reads AGENTS.md

**Phase 4a: Analyst**

- [ ] Replace all six values in `inputs/assumptions.csv` with sourced numbers and dates
- [ ] Commit, push, open PR, get review, CEO merges

**Phase 4b: Developer**

- [ ] Set `CLIENT` and fill the three TODO functions in `code/wacc.py`
- [ ] Run it, sanity check beta and WACC, commit, push
- [ ] After the analyst PR merges: merge `main` into `dev-wacc`, rerun, commit `outputs/wacc.csv`, open PR, review, merge

**Phase 4c: Product manager**

- [ ] Improve `app.py` on the FAKE numbers (CFO sentence, formatting, optional slider)
- [ ] Commit, push, open PR, review, merge

**Phase 5: Everyone verifies**

- [ ] Switch to `main`, pull, run `python code/wacc.py` then `streamlit run app.py`
- [ ] Card shows the real ticker, real WACC, no FAKE warning, every source filled
- [ ] Answer Question 2 (in the README or your notes)
- [ ] Optional level ups: merge conflict drill, competitor rows, private-firm WACC, Streamlit deploy

## Key decisions and recommendations

The client choice and the as-of date drive everything else, so make those two first and write every other choice into the `source` column with its reason.

### Team and repo decisions

| Decision | Options | Recommendation | Why |
| --- | --- | --- | --- |
| Team size | 3 or 4 | 3 if you have a choice | The notebook calls 3 optimal; fewer handoffs, CEO doubles as analyst |
| Who is CEO | Anyone | The most organized person, not the best coder | CEO reviews and merges every PR and owns the plan; the bottleneck if slow |
| Who is Developer | Anyone | Most comfortable with Python and pandas | Only role whose bugs break the number |
| Repo visibility | Public or private | Public | Simpler to share, works with free Streamlit deploy, doubles as a portfolio piece; no secrets in this project |
| How to drive git | Coding agent, GitHub Desktop, VS Code panel | Agent for speed, GitHub Desktop to see what happened | Mix freely; they do the same thing underneath |

### Choosing the client firm

Pick a plain, profitable, non-financial US company with real debt and at least 5 years of trading history.

| Avoid | Why it breaks the WACC card |
| --- | --- |
| Banks and insurers (JPM, BAC, AIG) | Debt is their raw material, not financing; WACC is the wrong tool |
| Firms with big captive finance arms (Ford, GM, Deere, and Caterpillar to a degree) | Finance-subsidiary debt inflates w\_D and drags WACC down; the professor's example is CAT, so you'd also look like a copy |
| IPOs under \~5 years old | `wacc.py` asserts more than 1,000 daily returns and will fail |
| Firms with losses | Effective tax rate is meaningless or negative |
| Near-zero debt firms | Valid, but WACC equals cost of equity and the card is boring |
| Tickers with a dot (BRK.B) | Yahoo uses a dash (BRK-B); easy to get wrong |

Good candidates: Coca-Cola (KO), PepsiCo (PEP), Home Depot (HD), Union Pacific (UNP), McDonald's (MCD), Lockheed Martin (LMT), Delta (DAL). Bonus if the firm connects to something your team might do for the final project.

### The as-of date

Agree on one date and use it for every input. The developer's `asof` is the last trading day in the downloaded returns; the analyst should pull rf, market cap, and debt as close to that date as possible and write the date in each source. Note that Mon Oct 12, 2026 was Columbus Day, when bond markets close, so FRED `DGS10` has no value that day; use the latest available observation and cite its date.

### The finance inputs

| Input | Recommended choice | Alternatives | What to watch |
| --- | --- | --- | --- |
| rf | FRED `DGS10`, latest observation on or before the as-of date | Yahoo `^TNX` | FRED reports percent: 4.10 means 0.0410. Check `^TNX` scaling the same way. 10-year matches long-lived projects |
| MRP | 5.0%, citing Kroll's recommended US ERP or Damodaran's current implied ERP (look up the current figure; do not reuse an old one) | Historical average ERP (around 4-6% depending on period) | A choice, not a fact. One sentence of justification in the source |
| beta | Raw OLS beta, 5 years daily vs SPY, adjusted prices | Blume-adjusted (0.67 x raw + 0.33) as an optional extra on the card | Do not change the `beta` column meaning; add extras only by agreement |
| r\_D | rf plus a credit spread matched to the firm's S&P or Moody's rating, using FRED's ICE BofA US corporate option-adjusted spread for that rating bucket | YTM on a long-dated bond of the firm (FINRA bond data) | Interest expense / debt reflects old coupons; show it only as a cross-check |
| tax | 21% federal statutory (or about 25% with state, if you say so) | Effective rate from the latest 10-K: income tax expense / pretax income | The tax shield works at the marginal rate; effective rate is a check. Odd effective rates (under 10% or over 35%) are a red flag |
| w\_E, w\_D | Market cap = price x shares outstanding on the as-of date; debt = total debt (short-term + current portion + long-term) from the latest 10-Q balance sheet | Include operating lease liabilities, or use net debt (debt minus cash) | Decide on leases and cash explicitly and write it down. Yahoo's "Total Debt" often includes leases. Book debt is an accepted stand-in for market debt |

Two mechanical rules for the analyst: values are decimals (0.041, not 4.1), and set w\_d = 1 - w\_e at the same precision (0.8734 and 0.1266), because `wacc.py` asserts they sum to 1 within 0.000001.

## Role-by-role instructions

Each person edits only their own file; that one rule prevents nearly every merge conflict.

### CEO (owns README.md, reviews and merges everything)

1. Create the repo from the template, add collaborators plus `donbowen`, and fill in the README on github.com: team name, client firm and ticker, the question, and the roles table with names, GitHub usernames, and branches.
2. Optional but smart: Settings > Branches > add a rule for `main` requiring a pull request before merging (free on public repos). This makes the "never commit to main" rule automatic.
3. Review checklist for every PR before clicking Merge:
   - Does it only touch the files that role owns?
   - No `.env`, keys, `__pycache__`, or stray files
   - Developer PR: the reviewer ran `python code/wacc.py` and the numbers look sane
   - Analyst PR: every value is a decimal with a dated, quoted source
   - PM PR: the app still runs and only reads files
4. Enforce merge order: analyst first, then the developer's rerun, PM whenever ready.
5. Agent prompt: "Read README.md and AGENTS.md. Ask me the questions you need to fill in the README. Don't write code."
6. Team of 4: the CEO has no PR by default, so make a small one (for example, add your team's Question 1 and 2 answers to the README on a branch called `ceo-notes`) so everyone has merged a PR.

### Analyst (owns inputs/assumptions.csv)

1. Collect each number from the Key decisions table, all as of the agreed date.
2. Write each `source` as: what it is, where from, which date, and why this choice. Example format: `"10-year Treasury, FRED DGS10, 2026-10-09 close; matches long-lived project horizon"`.
3. Keep every source in double quotes; sources contain commas.
4. Keep a scratch note (not committed, or committed as `inputs/notes.md` if the team agrees) with market cap, share count, debt components, and the rating used, so you can defend the weights.
5. Agent prompt: "Help me find sources for each assumption in inputs/assumptions.csv for \<TICKER>, as of \<DATE>. Show me where each number comes from; I'll check it." Then verify every number yourself on the actual page; agents misread tables and dates.

### Developer (owns code/wacc.py)

1. Set `CLIENT = '<TICKER>'`.
2. Fill the three functions. A reference version, tested on synthetic data (it reproduces the FAKE file's WACC of 0.079535 from the FAKE inputs), so your agent's version should match it:

```python
def get_returns(ticker, mkt=MKT, years=YEARS):
    px = yf.download([ticker, mkt], period=f'{years}y',
                     auto_adjust=True, progress=False)['Close']
    rets = px[[ticker, mkt]].pct_change(fill_method=None).dropna()
    assert not rets.empty, 'download returned nothing: check ticker or internet'
    return rets


def estimate_beta(rets, ticker, mkt=MKT):
    c = rets[[ticker, mkt]].cov()
    return c.loc[ticker, mkt] / c.loc[mkt, mkt]


def compute_wacc(beta, a):
    coe = a['rf'] + beta * a['mrp']
    wacc = a['w_e'] * coe + a['w_d'] * a['rd'] * (1 - a['tax'])
    return {'rf': a['rf'], 'mrp': a['mrp'], 'cost_of_equity': coe,
            'rd': a['rd'], 'tax': a['tax'], 'w_e': a['w_e'],
            'w_d': a['w_d'], 'wacc': wacc}
```

3. Why each detail matters: passing a list of two tickers makes `['Close']` a two-column table; `auto_adjust=True` makes prices include dividends and splits; computing cov and var from one `.cov()` matrix keeps the degrees-of-freedom consistent; `compute_wacc` must return exactly the eight keys the `__main__` block expects.
4. Cross-check beta with `np.polyfit(rets['SPY'], rets[CLIENT], 1)[0]`; it should be identical.
5. Run on the placeholder assumptions first, commit, push. Do not open the final PR until the analyst's PR is merged (see Git workflow).
6. Commit `outputs/wacc.csv`. It is not in `.gitignore`, and the app needs it on `main`.
7. Agent prompt: "Fill in the three TODO functions in code/wacc.py for ticker \<TICKER>. Don't change the output columns. Run it and show me the output."

### Product manager (owns app.py)

1. Start immediately on the FAKE numbers; the app switches to the real file automatically.
2. Goal: a CFO understands it in 30 seconds. Priorities, in order:
   - One sentence at the top answering the CFO: "New projects as risky as \<firm>'s typical business should earn at least X% a year."
   - Show the formula with the actual numbers plugged in
   - Format the inputs table: values as percents, sources fully visible (not truncated)
   - Show the as-of date prominently
3. Optional leverage slider. If you build it, relever beta, or the result is wrong. Tested snippet (it returns the card's own WACC at the current w\_d):

```python
st.subheader('What if leverage changes?')
wd = st.slider('Debt share of capital (w_d)', 0.0, 0.8, float(card['w_d']), 0.01)
de_now = card['w_d'] / card['w_e']
bu = card['beta'] / (1 + (1 - card['tax']) * de_now)       # unlever
be = bu * (1 + (1 - card['tax']) * wd / (1 - wd))          # relever
coe = card['rf'] + be * card['mrp']
w = (1 - wd) * coe + wd * card['rd'] * (1 - card['tax'])
st.metric('WACC at this leverage', f'{w:.2%}', delta=f'{(w - card["wacc"]) * 100:.2f} pp')
st.caption('Holds the cost of debt fixed; in reality r_D rises with leverage.')
```

4. Rule from AGENTS.md: the app only reads files from `outputs/` and `inputs/`. No yfinance calls inside the app.
5. Agent prompt: "Improve app.py so a CFO would understand it in 30 seconds. It must only read files. Start from the ideas in the TODO comment."

## Git workflow and merge order

The analyst's PR must merge before the developer's final run, or the committed WACC is built on placeholder numbers.

### The merge sequence

1. CEO commits the filled README directly to `main`.
2. Everyone clones and creates their branch from that `main`.
3. PM's PR can merge whenever ready; it touches only `app.py`.
4. Analyst's PR merges.
5. Developer brings the new assumptions into their branch: `git switch main`, `git pull`, `git switch dev-wacc`, `git merge main`.
6. Developer reruns `python code/wacc.py`, commits `outputs/wacc.csv` and `code/wacc.py`, pushes, opens the PR.
7. A teammate checks out `dev-wacc`, runs it, approves; CEO merges.
8. Everyone: `git switch main`, `git pull`, run both commands, confirm the card.

### Commands for each step (what your agent runs underneath)

```bash
# once
cd $HOME\Documents\FIN331
git clone https://github.com/CEO-USERNAME/REPO-NAME.git
cd REPO-NAME
git switch -c analyst-inputs          # your branch name
pip install -r requirements.txt

# every work session (from AGENTS.md)
git switch main
git pull
git switch analyst-inputs
git merge main

# after each working change
git add inputs/assumptions.csv
git commit -m "Add sourced rf, mrp, rd, tax, and weights for KO"
git push -u origin analyst-inputs     # later pushes: git push
```

Then open the PR from the yellow **Compare & pull request** banner on GitHub, with 1 to 2 sentences on what changed and how you checked it.

### Windows and setup gotchas

| Symptom | Fix |
| --- | --- |
| `git` not recognized right after installing | Close and reopen PowerShell and VS Code |
| You're in `C:\WINDOWS\System32` | `cd $HOME\Documents` before cloning; never create projects there |
| `python` opens the Microsoft Store or isn't found | Try `py` instead, or install Python from python.org with "Add to PATH" ticked |
| `streamlit` not recognized | Run `python -m streamlit run app.py` |
| `FileNotFoundError: inputs/assumptions.csv` | You're not in the repo root; `cd` into the repo folder first |
| First push opens a browser window | Normal: Git Credential Manager signing you in to GitHub; approve it |
| Warning about LF and CRLF line endings | Harmless on Windows; ignore it |
| `assumptions.csv` looks broken after editing | Don't open it in Excel, which strips quotes and reformats numbers; edit in VS Code |
| Push rejected: "updates were rejected" | Someone pushed first: `git pull`, then push again. Never `--force` |
| Agent wants to run `git reset --hard`, `rebase`, or `push --force` | Say no and ask it to explain; AGENTS.md forbids these without a human OK |

## Question 1 and Question 2

### Question 1: sketch the card, then compare to the columns

The card a CFO wants has more on it than `wacc.csv` holds; the gap is filled by `assumptions.csv`, which the app also reads.

| On a typical sketch but not in the columns | In the columns but often missing from sketches |
| --- | --- |
| Company name (not just ticker) | `asof` date |
| A source and date next to every input | `tax` rate |
| Market cap and debt in dollars behind the weights | `w_d` as a separate number from `w_e` |
| After-tax cost of debt, r\_D x (1 - tax) | `mrp` as its own visible choice |
| A one-line hurdle-rate answer for the CFO |  |
| Credit rating used for the spread |  |

Takeaway to write down: sources live in `assumptions.csv`, numbers live in `wacc.csv`, and any extra the team wants on the card (dollar amounts, rating) needs either a new column agreed by the developer and PM or a new row in `assumptions.csv`.

### Question 2: the stale wacc.csv

**What's wrong:** `outputs/wacc.csv` on `main` was computed with the old `rf`. Its `rf`, `cost_of_equity`, and `wacc` are stale. Worse, the app reads the sources table from `assumptions.csv` (new rf) and the headline WACC from `wacc.csv` (old rf), so the card silently contradicts itself.

**Request to the agent:**

> "The analyst's PR changed rf after my outputs/wacc.csv was committed, so the WACC on main is stale. Make a new branch from the latest main called dev-rerun, run python code/wacc.py, confirm the rf in outputs/wacc.csv matches inputs/assumptions.csv, then commit only outputs/wacc.csv and push the branch. Explain each step. Don't touch main directly."

**Steps underneath:**

1. `git switch main` and `git pull` (get the analyst's merged change)
2. `git switch -c dev-rerun` (or `git switch dev-wacc` then `git merge main`, if that branch still exists)
3. `python code/wacc.py`
4. Check `rf` in `outputs/wacc.csv` equals `rf` in `inputs/assumptions.csv`
5. `git add outputs/wacc.csv`, `git commit -m "Rerun WACC with final assumptions"`, `git push -u origin dev-rerun`
6. Open a PR, teammate reviews, CEO merges; everyone pulls `main`

**Prevention:** the PM can add a guard to `app.py` (still read-only) that shows `st.error` when `card['rf']` differs from `inputs.loc['rf', 'value']`, and likewise for the other five inputs.

## Sanity checks and common errors

A large-cap WACC usually lands around 6% to 11%; anything outside that needs a written reason before the PR merges.

| Check | Plausible range for a large US company | If it fails |
| --- | --- | --- |
| beta | 0.4 to 1.8 (staples low, airlines and industrials higher) | Wrong column order, prices instead of returns, or a bad ticker |
| rf | Matches the FRED value on your cited date, as a decimal | A value like 4.1 means you forgot to divide by 100 |
| rd | Above rf | Spread added wrong, or rf and rd from different dates |
| cost\_of\_equity | Above after-tax rd | Beta or MRP is off |
| w\_e + w\_d | Exactly 1 | Set w\_d = 1 - w\_e |
| tax | 0.15 to 0.30 | Effective rate distorted by one-time items; use 21% |
| wacc | Between after-tax rd and cost\_of\_equity | Arithmetic or weights swapped |
| Card | No FAKE warning, real ticker, every source filled, no "TODO" left | `outputs/wacc.csv` not on main, or analyst PR not merged |

| Error message | Likely cause | Fix |
| --- | --- | --- |
| `AssertionError: expected about 5 years of daily returns` | Empty download (Yahoo rate limit, no internet, wrong ticker) or a young IPO | Retry in a minute; check the ticker on finance.yahoo.com |
| `AssertionError: weights must sum to 1` | Rounding in assumptions.csv | Write w\_d as exactly 1 - w\_e |
| `AssertionError: WACC outside 0-25%` | Percent instead of decimal somewhere | Check every value is below 1 |
| `KeyError: 'value'` or misaligned columns | An unquoted comma in a source | Wrap every source in double quotes |
| `NotImplementedError` | A TODO function not filled yet | Finish all three functions |
| `ModuleNotFoundError: yfinance` | Requirements not installed | `pip install -r requirements.txt` |
| Merge conflict in a PR | Two people edited the same lines | Ask the agent to show both versions, decide together, don't push until agreed |

## Splitting the work as a team

The split is already built into the template: one file per person, and the fake output file means only one handoff (analyst to developer) actually blocks anyone.

&#91;embedded content: team workflow · 4 lanes, 1 dependency\]

The analyst's merge is the one gate; everything else runs side by side.

### Team of 3 vs team of 4

| Role | Team of 4 | Team of 3 | Load |
| --- | --- | --- | --- |
| CEO | Own person: README, reviews, merges, plus a small `ceo-notes` PR | Same person as Analyst | Light coding, heavy coordination |
| Analyst | Own person | CEO does it | Heaviest research; most judgment calls |
| Developer | Own person | Own person | Short code, but must rerun after analyst |
| Product manager | Own person | Own person | Most open-ended; can absorb level-ups |

In a team of 3, the CEO-analyst is the busiest person, so the developer should review the analyst's PR (and run the numbers) and the PM should take any level-up work.

### Suggested schedule

1. **Tue in class (first 25 min):** form team, Question 1 sketch, CEO creates repo, everyone clones and branches.
2. **Tue in class (rest):** all three lanes work in parallel. Goal: PM PR merged and analyst PR open before class ends (poll levels 1 to 3).
3. **Tue night or Wed:** analyst PR merged; developer reruns and opens the final PR; teammate reviews.
4. **Wed:** CEO merges; everyone pulls and runs the card (poll level 4). Quick 10-minute check-in call or group chat confirmation.
5. **Before Thu Oct 15 class:** repo link in the Team Projects sheet; optional level-ups; skim ideas for the final project kickoff.

### Team norms worth agreeing on now

- One group chat; post the PR link there whenever you open one, so reviews don't stall.
- Reviews within a few hours, not days; the CEO is the bottleneck by design.
- Anyone who needs a change in someone else's file asks the owner instead of editing it.
- Put decisions (client, as-of date, MRP choice, lease treatment) in the README so every teammate's agent reads them.

### Splitting the level-ups (if you finish early)

| Level-up | Who | Notes |
| --- | --- | --- |
| Merge conflict drill | Any two people, CEO resolves | Do it now; far better than the night before the final is due |
| Competitor rows | Developer (rows in wacc.csv) + PM (side-by-side view) + Analyst (competitor inputs) | Changes the contract to one row per ticker: update the README first |
| Private-firm WACC | Analyst + Developer | Unlever 3 comps' betas, average, relever at the private firm's leverage |
| Deploy to Streamlit | PM | share.streamlit.io, pick the repo and `app.py`; public repo makes this easiest |
