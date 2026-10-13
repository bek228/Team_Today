"""The WACC card.

Run from the repo root:   streamlit run app.py

Owner: the product manager. This works today on the FAKE numbers, so you can build
the page before the real numbers exist. When the developer's pull request is merged,
outputs/wacc.csv appears and the app switches to it automatically.

The app only reads files from outputs/ and inputs/. No downloads, no estimation.
"""
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title='WACC card', layout='centered')

real = Path('outputs/wacc.csv')
card = pd.read_csv(real if real.exists() else 'outputs/wacc_FAKE.csv').iloc[0]
inputs = pd.read_csv('inputs/assumptions.csv', index_col='item')

NAMES = {'PM': 'Philip Morris International'}
firm = NAMES.get(card['ticker'], card['ticker'])

if not real.exists():
    st.warning('Showing FAKE numbers. Run `python code/wacc.py` to make outputs/wacc.csv.')

# Headline: the answer a CFO wants
st.title(f"WACC card: {firm} ({card['ticker']})")
st.markdown(f"**As of {card['asof']}** (5 years of daily returns through this date)")
st.info(f"New projects as risky as {firm}'s typical business should earn at least "
        f"**{card['wacc']:.1%} a year**.")

c1, c2, c3 = st.columns(3)
c1.metric('WACC', f"{card['wacc']:.2%}")
c2.metric('Cost of equity', f"{card['cost_of_equity']:.2%}")
c3.metric('Beta', f"{card['beta']:.2f}")

# The formula with the numbers plugged in
st.subheader('How we got there')
after_tax_rd = card['rd'] * (1 - card['tax'])
st.markdown('**Cost of equity** = rf + beta × MRP')
st.code(f"{card['rf']:.2%} + {card['beta']:.2f} × {card['mrp']:.2%} = {card['cost_of_equity']:.2%}",
        language=None)
st.markdown('**WACC** = w_E × r_E + w_D × r_D × (1 − tax)')
st.code(f"{card['w_e']:.1%} × {card['cost_of_equity']:.2%} + {card['w_d']:.1%} × "
        f"{card['rd']:.2%} × (1 − {card['tax']:.0%}) = {card['wacc']:.2%}",
        language=None)
st.caption(f"After-tax cost of debt: {after_tax_rd:.2%}")

# Inputs as percents, with full sources visible
st.subheader('Inputs and sources')
labels = {'rf': 'Risk-free rate (rf)', 'mrp': 'Market risk premium (MRP)',
          'rd': 'Pre-tax cost of debt (r_D)', 'tax': 'Tax rate',
          'w_e': 'Equity weight (w_E)', 'w_d': 'Debt weight (w_D)'}
rows = [f"| {labels.get(item, item)} | {row['value']:.2%} | {row['source']} |"
        for item, row in inputs.iterrows()]
rows.append(f"| Beta | {card['beta']:.2f} | Estimated in code/wacc.py: 5y daily returns vs SPY |")
st.markdown('| Input | Value | Source |\n|---|---|---|\n' + '\n'.join(rows))

# What-if: leverage slider (relevers beta so the answer stays consistent)
st.subheader('What if leverage changes?')
wd = st.slider('Debt share of capital (w_d)', 0.0, 0.8, float(card['w_d']), 0.01)
de_now = card['w_d'] / card['w_e']
bu = card['beta'] / (1 + (1 - card['tax']) * de_now)       # unlever
be = bu * (1 + (1 - card['tax']) * wd / (1 - wd))          # relever
coe = card['rf'] + be * card['mrp']
w = (1 - wd) * coe + wd * card['rd'] * (1 - card['tax'])
st.metric('WACC at this leverage', f'{w:.2%}', delta=f'{(w - card["wacc"]) * 100:.2f} pp')
st.caption('Holds the cost of debt fixed; in reality r_D rises with leverage.')
