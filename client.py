# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Arbitrage - Statistical Pairs Cointegration & Spread Trader
Standard Library only: math, typing.
Calculates OLS hedge ratio beta, spread residual series, rolling Z-score,
and Ornstein-Uhlenbeck mean-reversion half-life parameters.
"""

import math
from typing import Dict, List, Any

class OpenClawGenParkArbitrage:
    def fit_pairs_model(self, series_y: List[float], series_x: List[float]) -> Dict[str, Any]:
        """
        Fits OLS regression: Y = alpha + beta * X + epsilon
        """
        n = len(series_y)
        if n < 5 or len(series_x) != n:
            raise ValueError("Series must be of equal length and have at least 5 points")

        mean_y = sum(series_y) / n
        mean_x = sum(series_x) / n

        cov_xy = sum((series_x[i] - mean_x) * (series_y[i] - mean_y) for i in range(n))
        var_x = sum((series_x[i] - mean_x) ** 2 for i in range(n))

        if var_x <= 1e-8:
            raise ValueError("Zero variance in independent series X")

        beta = cov_xy / var_x
        alpha = mean_y - beta * mean_x

        # Calculate spread residuals
        spread = [series_y[i] - (alpha + beta * series_x[i]) for i in range(n)]

        spread_mean = sum(spread) / n
        spread_var = sum((s - spread_mean) ** 2 for s in spread) / (n - 1)
        spread_std = math.sqrt(max(1e-8, spread_var))

        current_spread = spread[-1]
        z_score = round((current_spread - spread_mean) / spread_std, 3)

        # Ornstein-Uhlenbeck half-life estimation: delta_s = -theta * (s_{t-1} - mean)
        d_spread = [spread[i] - spread[i-1] for i in range(1, n)]
        lag_spread = [spread[i-1] - spread_mean for i in range(1, n)]
        cov_ou = sum(d_spread[i] * lag_spread[i] for i in range(len(d_spread)))
        var_ou = sum(lag_spread[i] ** 2 for i in range(len(lag_spread)))
        theta = -cov_ou / max(1e-8, var_ou)
        half_life_periods = round(math.log(2.0) / max(1e-4, theta), 2) if theta > 0 else 999.0

        # Signal generation
        signal = "HOLD"
        if z_score >= 2.0: signal = "SHORT_SPREAD_ENTER"
        elif z_score <= -2.0: signal = "LONG_SPREAD_ENTER"
        elif abs(z_score) <= 0.2: signal = "CLOSE_POSITIONS"

        return {
            "hedge_ratio_beta": round(beta, 4),
            "intercept_alpha": round(alpha, 4),
            "current_spread": round(current_spread, 4),
            "spread_std": round(spread_std, 4),
            "z_score": z_score,
            "ou_half_life_periods": half_life_periods,
            "signal": signal,
            "sample_size": n
        }
