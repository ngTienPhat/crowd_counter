# Install tutorial

You only need to clone this repo.

Then go to this repo root, then run:
```
pip install -e .
```

If you want to install plugins, run:
```
pip install -e .[<name plugin 1>, <name plugin 2>, ...]
```

Example:
```
pip install -e .[sanet]
```

List of current support:
- sanet

Note: For `sanet`, you will need to run this extra step for keras-contrib.
(No support by PyPi).

```
pip install git+https://www.github.com/keras-team/keras-contrib.git
```


# Extend tutorial
Check file `docs/engine_document.md` to understand our Engine Interface.
