# Instructions for blogging

## Useful aliases

Add these to your `~/.zshrc` or equivalent:

```zsh
alias blog='make devserver'
alias blog-stop='./develop_server.sh stop'
alias blog-update='ghp-import -b master output'

alias gpush='git push origin master'
```

## Install dependencies (assuming Python 3.X)

### Texlive 

(Optional)

`apt get install texlive-full`
(TODO: figure out a way to avoid the installation of `texlive-lang-*` packages)

### Zotero

https://github.com/retorquere/zotero-deb
https://askubuntu.com/a/1160369

## Repositories and dependencies needed

1. Clone pelican-themes from `git@github.com:getpelican/pelican-themes.git` in a folder at the same (folder) level than this repo.
2. https://github.com/getpelican/pelican-plugins


**Note**: Previously, I cloned separately pelican-ipynb from `git@github.com:danielfrg/pelican-ipynb.git` at commit `292d29a` inside `plugins/ipynb`.

## Blog development environment with `conda`

```zsh
conda env create -f environment.yml
conda activate blog
blog &
jupyter-notebook content &
`****

**Old note**: just to make sure I have an exact copy of the environment available if necessary, I also exported my current conda environment with `conda env export > environment-2018-08-25.yml` and included it in the blog repository.

Simply use environment.yml, and let anaconda solver do its job.
