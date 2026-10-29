# -*- coding: utf-8 -*-
import sys, json
from client import OpenClawGenParkArbitrage

arbitrage = OpenClawGenParkArbitrage()

def run_tool(name, args):
    if name == "fit_pairs_model":
        sy = [float(x) for x in args.get("series_y", [])]
        sx = [float(x) for x in args.get("series_x", [])]
        return arbitrage.fit_pairs_model(sy, sx)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running OpenClaw GenPark Arbitrage Self-Test...")
        sy = [100.0, 102.0, 101.5, 105.0, 108.0, 107.0]
        sx = [50.0, 51.0, 50.8, 52.5, 54.0, 53.5]
        res = arbitrage.fit_pairs_model(sy, sx)
        assert res["hedge_ratio_beta"] > 1.0
        assert "z_score" in res
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
