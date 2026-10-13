# Seni bina

🌐 [English](Architecture) · [Dansk](Architecture-da) · **Bahasa Malaysia**

## Modul (`src/`)

| Modul | Tanggungjawab |
| --- | --- |
| `main.py` | Mencipta skrin dan objek serta menjalankan gelung permainan |
| `constants.py` | Semua pemalar, ditakrifkan sekali sahaja |
| `player.py` | `Player(Turtle)`: `go_up`, `is_at_finish_line`, `go_to_start` |
| `car_manager.py` | `CarManager`: `create_cars`, `move_cars`, `is_hit`, `level_up` |
| `car_shape.py` | Lukisan sebuah kereta: badan, kabin, tingkap, lampu depan, dua roda |
| `collision.py` | `is_colliding`: ujian segi empat tepat tulen, tanpa turtle |
| `scoreboard.py` | `Scoreboard(Turtle)`: teks tahap dan `GAME OVER` |

## Pilihan reka bentuk

- **Kereta kelihatan seperti kereta.** Sebuah kereta ialah bentuk turtle
  gabungan dalam tapak 40 x 20 piksel yang ditetapkan tugasan. Satu bentuk
  didaftarkan bagi setiap warna, jadi tiada fail imej diperlukan.
- **Boleh diuji tanpa tetingkap.** Geometri (`car_components`), ujian perlanggaran
  dan peraturan penciptaan ialah kod biasa. `CarManager` menerima kilang kereta
  dan sumber rawak, jadi ujian menggunakan kereta palsu dan dadu yang ditetapkan.
- **Perlanggaran menggunakan seluruh kereta.** Pemain dibandingkan dengan segi
  empat tepat kereta, bukan hanya bahagian tengahnya.

## Dokumentasi

Komen dalam sumber ialah komen Doxygen. Bina dengan `doxygen Doxyfile`.
Dokumen perancangan dan semakan terdapat dalam `docs/`.

Kembali ke [Laman utama](Home-ms).
