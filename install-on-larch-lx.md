# Install MAVIS 4.3 on Arch Linux

<div align="left">
   <img alt="mavis" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-icon-banner-3.svg">
   <img alt="mavis-launcher" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-launcher-icon-banner-3.svg">
   <img alt="mavis-terminal" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-terminal-icon-banner-3.svg">
   <img alt="tg-loerrach" src="https://img.shields.io/badge/TG Lörrach-red?style=flat">
   <img alt="peharge" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/Peharge-icon-banner-3.svg">
</div>

<br>

```bash
sudo pacman -Syu
```

Normally gcc is already installed
```bash
sudo pacman -S gcc
```

Normally Python is already installed
```bash
sudo pacman -S python3
```

Normally Python is already installed
```bash
sudo pacman -S ffmpeg
```

```bash
sudo pacman -S g++
```

```bash
sudo pacman -S rustc
```

```bash
sudo pacman -S git
```

```bash
yay -S ollama
```

```bash
mkdir PycharmProjects
```

```bash
cd PycharmProjects
```

```bash
git cloen https://github.com/Peharge/MAVIS.git
```

```bash
cd MAVIS
```

Run:

>```bash
>bash mavis-launcher-4.py
>```

Or:

>```bash
>python3 -m venv .env
>```
>
>```bash
>source .env/bin/activate
>```
>
>```bash
>cd install
>```
>
>```bash
>python3 install-mavis-4.py
>```
>
>see models
>```bash
>python3 m-help-models.py
>```
>
>```bash
>python3 install-ollama-mavis-4.py
>```
>
>```bash
>cd
>```
>
>```bash
>cd PycharmProjects
>```
>
>```bash
>cd MAVIS
>```
>
>```bash
>python3 mavis-4-3-main-lx.py
>```
>
>new window
>```bash
>ollama start
>```
>