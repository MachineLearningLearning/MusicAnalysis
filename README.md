# MusicAnalysis

## Dataset
Due to the dataset's file size, the source code will not ship with any music.

Prior to running the `build_dataset` notebook, a `data/` folder should be populated with music files in `.wav` format, categorised into folders corresponding to their labels.

For example, it may look like:
```
data/
├───blues
│       blues.00000.wav
│       blues.00001.wav
│       blues.00002.wav
│       ...
│
├───classical
│       classical.00000.wav
│       classical.00001.wav
│       classical.00002.wav
│       ...
│
├───country
│       ...
...
```

It would be ideal if the `.wav` files all adhered to the following specifications (as in GTZAN style datasets):
```
Duration: 00:00:30.01, bitrate: 352 kb/s
Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 22050 Hz, 1 channels, s16, 352 kb/s
```

It is recommended that the original GTZAN dataset is used to reproduce our results. To do so, download the dataset as an archive file from one of the links below and extract the contents of the "genres_original" folder into `data/`.
- https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification?resource=download
- http://marsyas.info/downloads/datasets.html
- http://opihi.cs.uvic.ca/sound/genres.tar.gz
