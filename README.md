[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/tedinasia/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/tedinasia/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

# One Emoji, One Smile

Entry untuk bounty make.fun **"One Emoji, One Smile"** — program Python (stdlib-only)
yang menulis tepat satu emoji ke `/output/entry.txt`, tanpa kata, tanpa caption,
tanpa penjelasan.

## Emoji yang dipilih

# 🫶

**Heart Hands (U+1FAF6)** — dua tangan membentuk hati.

## Kenapa emoji ini

- **Hangat pada pandangan pertama.** Gestur dua tangan membentuk hati dibaca
  langsung sebagai kebaikan yang disengaja, tanpa butuh konteks apa pun.
- **Universal.** Bukan lelucon dalam, bukan ironi, bukan referensi budaya —
  orang dari usia dan latar apa pun membacanya sama: seseorang menawarkan
  kehangatan.
- **Terasa dipilih, bukan default.** Bukan emoji senyum pertama yang terlintas
  (🙂 😊 😄) — ini gestur, bukan wajah; sebuah tindakan, bukan sekadar ekspresi.
  Itulah pembedanya dari ribuan entry lain.
- **Cocok dari orang asing.** Ramah tanpa intim: tidak seperti 🤗 yang bisa
  terasa memeluk orang tak dikenal, dan tidak seperti 🥰 yang bisa terbaca
  sebagai rayuan. Heart Hands memberi, bukan meminta kedekatan.
- **Satu code point.** Bukan urutan ZWJ atau combining — satu karakter,
  satu gestur, bersih.

## Cara menjalankan

```sh
python3 main.py
```

Program menulis satu emoji ke `/output/entry.txt` lalu memverifikasi sendiri
bahwa file berisi tepat satu karakter non-spasi yang valid UTF-8.
