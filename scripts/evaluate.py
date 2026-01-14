import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run_dir", required=True, help="Folder hasil run (mis. results/xxx)")
    args = ap.parse_args()

    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)

    # TODO: load checkpoint, jalankan inference, simpan prediksi & metrik
    print(f"TODO: evaluate run at: {run_dir}")

if __name__ == "__main__":
    main()
