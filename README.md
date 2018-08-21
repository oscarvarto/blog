# Instructions for developing/adding more posts

# Install dependencies (assuming Python 3.X)

## Texlive
`apt get install texlive-full`

## Zotero
From https://github.com/smathot/zotero_installer:

```
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install zotero-standalone
```

## Inside a conda environment:
`$ conda install pelican tipogrify beautifulsoup4 markdown jupyter ipython nbconvert jupyterlab`
(verify that `ghp-import` is installed as a dependency)

```
$ pip install cite2c
$ python -m cite2c.install

$ pip install citeproc-py
$ pip install unicode_tex
```

## Repositories and dependencies needed

1. Clone pelican-themes from `git@github.com:getpelican/pelican-themes.git` in a folder at the same (folder) level than this repo.
2. `danielfrg/pelican-ipynb.git` is cloned at commit `292d29a` inside `plugins/ipynb`.

oscarvarto.github.io should be cloned with the `--recursive` flag:
`git clone git@github.com:oscarvarto/oscarvarto.github.io.git --recursive`

or in three steps:
```
git clone git@github.com:oscarvarto/oscarvarto.github.io.git
cd oscarvarto.github.io
git submodule update --init --recursive
```

## Useful aliases for blogging:

Maybe you can add these to your `~/.zshrc` or equivalent:

```
alias blog='make devserver'
alias blog-stop='./develop_server.sh stop'
alias blog-update='ghp-import -b master output'

alias gpush='git push origin master'
```