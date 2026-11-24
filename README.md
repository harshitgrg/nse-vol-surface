# NSE Implied Volatility Surface (`nse-vol-surface`)

Tools and notebooks for analyzing National Stock Exchange of India (NSE) Derivatives Bhavcopy data, computing option chain metrics, and preparing data for implied volatility surface modeling.

## Features

- **NSE Bhavcopy Extraction & Parsing:** Automated retrieval and parsing of historical and daily NSE F&O bhavcopy records (including new UDiFF formats).
- **Trading Day Calendar & Expiry Calculation:** Precise computation of Time-to-Maturity ($T$) based on NSE annual trading holiday calendars.
- **Option Metrics Transformation:**
  - Filtering near-expiry noise (Vega collapse filter).
  - Forward price calculation ($F = S \cdot e^{rT}$) using T-Bill risk-free proxies.
  - Log-moneyness calculation ($k = \ln(K / F)$).
- **Options Data Processing:** Workflows for NIFTY / equity options preparing data for Black-Scholes implied volatility inversion and surface construction.

## Project Structure

```text
├── README.md                                  # Project overview and documentation
├── .gitignore                                 # Git ignore patterns
├── bhavcopy_analysis.py                       # Bhavcopy processing and trading days calculation
├── sample_nb.ipynb                            # Interactive notebook for scraping, parsing, and cleaning
├── BhavCopy_NSE_FO_0_0_0_20260902_F_0000.csv  # Sample NSE Bhavcopy data
├── BhavCopy_NSE_FO_0_0_0_20260902_F_0000.csv.zip
├── BhavCopy_NSE_FO_0_0_0_20261016_F_0000.csv.zip
├── fo020926.zip
├── fo020926/                                  # Sample historical derivatives records
└── option-chain-ED-HDFCBANK-27-Oct-2026.csv   # Sample stock option chain snapshot
```

## Setup & Prerequisites

```bash
pip install numpy pandas matplotlib requests
```

## Usage

Run the analysis script:
```bash
python bhavcopy_analysis.py
```
Or launch Jupyter Notebook to run `sample_nb.ipynb`:
```bash
jupyter notebook sample_nb.ipynb
```
