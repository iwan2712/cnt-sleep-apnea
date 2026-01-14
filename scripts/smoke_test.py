"""Smoke test: memastikan struktur repo dan import berjalan."""

from cnt_osa.utils.seed import set_seed
from cnt_osa.eval.metrics import confusion_to_metrics

def main():
    set_seed(42)
    m = confusion_to_metrics(tp=50, tn=40, fp=5, fn=5)
    print("Smoke test OK")
    print("Metrics:", m)

if __name__ == "__main__":
    main()
