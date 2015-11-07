# muffle

Simple module for silencing all output from external process. Really, all. Based on this [post](http://stackoverflow.com/questions/11130156/suppress-stdout-stderr-print-from-python-functions).

#### install

```
pip install muffle
```

#### use

```python
import muffle

with muffle.on():
  # do noisy stuff
```
