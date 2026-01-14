# CN-T Sleep Apnea (Starter Repo)

Repo ini adalah **template paling mudah** untuk menaruh hasil penelitian di GitHub dengan struktur yang rapi dan bisa direproduksi.

## Isi Repo
- `scripts/` : perintah cepat (preprocess/train/evaluate/make_figures)
- `src/cnt_osa/` : kode utama (data, preprocess, models, training, evaluasi)
- `configs/` : konfigurasi eksperimen (YAML)
- `assets/` : gambar untuk README (diagram, contoh output)
- `results/` : output hasil (DI-IGNORE Git) — taruh file hasil di sini saat running

> Catatan: folder `data/` dan `checkpoints/` tidak ikut di-commit (sesuai praktik umum riset).

## Cara Pakai (Paling Simpel)
1) Install Python (disarankan 3.10+)
2) Buat environment dan install:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

3) Jalankan smoke test:
```bash
python scripts/smoke_test.py
```

## Reproduksi Eksperimen (nanti)
Nanti Anda cukup isi implementasi di `src/` dan sesuaikan config di `configs/`, lalu jalankan:
```bash
python scripts/train.py --config configs/train_sleepedf.yaml
python scripts/evaluate.py --run_dir results/example_run
python scripts/make_figures.py --run_dir results/example_run
```

## Sitasi
- Tambahkan paper Anda ke `CITATION.cff` dan `docs/CITATION.bib`.

## Lisensi
Default: MIT (ubah jika perlu).
