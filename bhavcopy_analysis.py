import numpy as np
import pandas as pd

# 0. Load BhavCopy data
csv_path = "BhavCopy_NSE_FO_0_0_0_20260902_F_0000.csv"
df = pd.read_csv(csv_path, parse_dates=['TradDt', 'XpryDt'])

# 1. Define NSE annual trading holidays (YYYY-MM-DD strings)
nse_holidays_2026 = np.array([
    '2026-01-26',  # Republic Day
    '2026-03-25',  # Holi
    '2026-04-14',  # Dr. Ambedkar Jayanti
    '2026-05-01',  # Maharashtra Day
    '2026-08-15',  # Independence Day
    '2026-10-02',  # Gandhi Jayanti
    '2026-11-09',  # Diwali-Balipratipada
    '2026-12-25'   # Christmas
], dtype='datetime64[D]')

# 2. Convert pandas datetime columns to numpy datetime64[D] arrays
trad_dates = df['TradDt'].dt.date.values.astype('datetime64[D]')
xpry_dates = df['XpryDt'].dt.date.values.astype('datetime64[D]')

# 3. Compute trading days (excluding weekends and explicit holidays)
df['trading_days'] = np.busday_count(
    trad_dates, 
    xpry_dates, 
    holidays=nse_holidays_2026
)

# 4. Express Time to Maturity (T) in annual trading terms
df['T'] = df['trading_days'] / 252.0

if __name__ == "__main__":
    print("Shape:", df.shape)
    print(df[['TradDt', 'XpryDt', 'TckrSymb', 'StrkPric', 'OptnTp', 'trading_days', 'T']].head(10))