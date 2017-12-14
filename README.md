# MockScreen

A Script to Mock Screen for Mac OS

Requirements:

```bash
brew install brightness pygtk
brew install pygobject3 --with-python3
```

run

```
mkdir -p /Users/phodal/Library/Python/2.7/lib/python/site-packages
echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/phodal/Library/Python/2.7/lib/python/site-packages/homebrew.pth
```

add those to ``.zsrhc`` || ``.bash_profile``:

```bash
function ss() { 
    python "/Users/fdhuang/learing/ss/main.py" 
}
```

License
---

MIT

