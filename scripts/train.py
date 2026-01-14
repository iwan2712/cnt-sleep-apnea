import argparse
import yaml
from pathlib import Path

from cnt_osa.utils.seed import set_seed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="Path ke file YAML config")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    set_seed(int(cfg.get("seed", 42)))

    # TODO: implement training loop / PyTorch Lightning module
    print("Loaded config:", cfg)
    print("TODO: training implementation")

if __name__ == "__main__":
    main()
