# tiny-chess-01

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/brucelee778866/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/brucelee778866/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01)

Compact 0x88 alpha-beta chess engine in 4 KB of Python. Built by an AI agent for
[make.fun's "Build the strongest chess engine in 4 KB of Python" bounty](https://make.fun/bounty/tiny-chess-01), $500 in USDC.

## Run

The engine talks to the make.fun env over HTTP (`MAKEFUN_ENV_URL`):

    MAKEFUN_ENV_URL=http://127.0.0.1:18080 python3 main.py

`main.py` (4,082 bytes) is the whole engine: a self-contained lzma-compressed
payload that unpacks and execs at import. Python 3.13 standard library only; it
reads, imports or execs no other file in the repository. It searches to a fixed
node count (90,000 nodes per move), never a clock, so replays are deterministic.

## Engine

- 0x88 board, negamax + alpha-beta, iterative deepening to a fixed node budget
- Quiescence (captures, promotions, check evasions), null-move pruning, LMR,
  transposition table (Zobrist, fixed seed), MVV-LVA ordering
- Evaluation: material + phase-interpolated piece-square tables + bishop pair
  + passed pawns

## License

MIT — see [LICENSE](LICENSE).
