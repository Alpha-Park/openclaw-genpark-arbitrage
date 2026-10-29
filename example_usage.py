# -*- coding: utf-8 -*-
from client import OpenClawGenParkArbitrage

def main():
    trader = OpenClawGenParkArbitrage()
    print("=== OpenClaw GenPark Statistical Arbitrage ===")

    # Historical prices for BTC and WBTC / closely correlated pair
    btc = [64000, 64200, 64100, 64500, 64800, 65200, 65000, 65600, 66000]
    eth_proxy = [3200, 3210, 3205, 3225, 3240, 3260, 3250, 3280, 3300]

    model = trader.fit_pairs_model(btc, eth_proxy)
    print(f"Hedge Ratio Beta: {model['hedge_ratio_beta']}")
    print(f"Spread Z-Score: {model['z_score']}")
    print(f"Mean-Reversion Half-Life: {model['ou_half_life_periods']} steps")
    print(f"Action Signal: {model['signal']}")

if __name__ == "__main__":
    main()
