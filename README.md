# <p align='center'><img width="32px" height="32px" src="https://popcat.click/img/op.353767c3.png" />PyPopcat</p>

Taiwan NO.1 !!!

## Features

- drive multiple Chrome windows to click by multithreading.
- use TOR proxy to prevent to be blocked by API rate limit (WIP)

## Screenshots

![Demo](./img/screenshot.png)
![MultiWindows](./img/multi_windows.png)

## Prerequisites

- Download [Chrome driver](https://chromedriver.chromium.org/) based on your OS.
- Move the driver to folders in `PATH` such as `/usr/local/bin`, `/usr/bin`.

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run pypopcat emit --n_threads 1 --country TW
```

## Notes

According popcat's rules, you can't exceed 800 clicks every 30s. You need to adjust `n_threads` due to worker's pps.
