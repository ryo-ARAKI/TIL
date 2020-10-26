# Clean install TeXLive

## Remove old TeXLive

- [How to remove everything related to TeX Live for fresh install on Ubuntu?](https://tex.stackexchange.com/questions/95483/how-to-remove-everything-related-to-tex-live-for-fresh-install-on-ubuntu)
- Note that I use `\*` instead of `*` because I use fish shell, not bash

```bash
sudo apt purge texlive\*
sudo rm -rf /usr/local/texlive/\*
sudo rm -rf /usr/share/texmf/
sudo rm -rf /usr/share/texlive/
sudo rm -rf /var/lib/texmf/
sudo rm -rf /etc/texmf/
sudo apt remove tex-common --purge
find -L /usr/local/bin/ -lname /usr/local/texlive/\*/bin/\* | xargs rm
sudo apt autoremove
```

## Install latest TeXLive manually

- [TeX Live のインストール](https://texwiki.texjp.org/?Linux#texliveinstall)

```bash
cd ~/Downloads/
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar xvf install-tl-unx.tar.gz
cd install-tl-*/
sudo ./install-tl -no-gui
```

ダイアログに従ってインストールが終了後， `.bashrc` に下記を追記

```bashrc
# Add TexLive 20** PATH
export PATH=/usr/local/texlive/20**/bin/x86_64-linux:$PATH
export MANPATH=/usr/local/texlive/20**/texmf-dist/doc/man:$MANPATH
export INFOPATH=/usr/local/texlive/20**/texmf-dist/doc/info:$INFOPATH
```

して `source .bashrc` で完了

## Install TeXLive package for manually installed TeXLive

```bash
tlmgr install <package>
```
