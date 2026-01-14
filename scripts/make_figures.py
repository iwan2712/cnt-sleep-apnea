import argparse
from pathlib import Path

import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run_dir", required=True, help="Folder hasil run (mis. results/xxx)")
    args = ap.parse_args()

    run_dir = Path(args.run_dir)
    fig_dir = run_dir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    # Placeholder figure
    plt.figure()
    plt.plot([0, 1, 2], [0.7, 0.8, 0.9])
    plt.title("Placeholder Figure (replace with real Fig.3/Fig.4 generator)")
    out = fig_dir / "placeholder.png"
    plt.savefig(out, dpi=200, bbox_inches="tight")
    print("Saved:", out)

if __name__ == "__main__":
    main()
