---
name: openclaw-genpark-arbitrage
description: OpenClaw GenPark statistical pairs cointegration and mean-reverting spread trading engine with OLS beta and Ornstein-Uhlenbeck half-life modeling.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'fit_pairs_model', 'description': 'Compute hedge ratio, residual spread Z-score, and mean-reversion trading signal.'}
---

# Openclaw Genpark Arbitrage

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Arbitrage**.
Your primary directive is to execute: OpenClaw GenPark statistical pairs cointegration and mean-reverting spread trading engine with OLS beta and Ornstein-Uhlenbeck half-life modeling.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'fit_pairs_model', 'description': 'Compute hedge ratio, residual spread Z-score, and mean-reversion trading signal.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'fit_pairs_model', 'description': 'Compute hedge ratio, residual spread Z-score, and mean-reversion trading signal.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
