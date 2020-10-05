```
from memeparser import MemeParser, parse_all_meme

dir_path = "path/to/dir/with/memes"
memes = parse_all_meme(dir_path) # it applies MemeParser to each meme_fpath

# memes is a dict with names (short names) of the TFs.
```
