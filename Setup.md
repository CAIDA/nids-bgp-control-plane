[README](README.md) | [Introduction](Introduction.md) | Setup ⮕ | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Report](Report.md)

# Set Up Your Local Environment

## Step 1: Install uv and Python dependencies

This module uses [uv](https://docs.astral.sh/uv/), the same Python package and project manager you used in `nids-asn-introduction`.

```bash
# Install uv (skip if already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install this module's Python dependencies
uv sync
```

## Step 2: Install the bgpkit-parser CLI

The `bgpkit-parser` command-line tool lets you explore MRT files interactively without writing any code.

```bash
# macOS
brew install bgpkit/tap/bgpkit-parser

# Other platforms: download a pre-built binary from
# https://github.com/bgpkit/bgpkit-parser/releases
```

## Step 3: Verify everything is working

Run the provided setup checker to confirm that Python, the bgpkit library, the bgpkit CLI, and the data directory are all ready:

```bash
uv run scripts/check-setup.py
```

All checks must pass before you proceed to [Datasets.md](Datasets.md). If a check fails, follow the fix hint printed next to it.

[README](README.md) | [Introduction](Introduction.md) | Setup ⮕ | [Datasets](Datasets.md) | [Tasks](Tasks.md) | [Report](Report.md)
