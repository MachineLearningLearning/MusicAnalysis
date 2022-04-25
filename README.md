# MusicAnalysis

## Dataset
Due to the dataset's file size, the source code will not ship with any music.
데이터 세트의 파일 크기으로인해 소스 코드는 음성파일들이 함께 포함되어있지 않습니다.

Prior to running the `build_dataset` notebook, a `data/` folder should be populated with music files in `.wav` format, categorised into folders corresponding to their labels.
`build_dataset` 노트북을 실행하기 전에 `data/` 폴더에 `.wav` 형식의 음악 파일들이 알맞는 레이블에 해당하는 폴더로 분류해 채워야 합니다.

For example, it may look like:
예를들어:
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
`.wav` 파일들이 모두 다음과 같은 사양으로 (GTZAN 데이터 세트의 스타일과 같이) 준수한다면 이상적입니다.
```
Duration: 00:00:30.01, bitrate: 352 kb/s
Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 22050 Hz, 1 channels, s16, 352 kb/s
```

It is recommended that the original GTZAN dataset is used to reproduce our results. To do so, download the dataset as an archive file from one of the links below and extract the contents of the "genres_original" folder into `data/`.
결과를 재현하기 위해서는 원래의 GTZAN 데이터 세트를 사용하는 것을 추천드립니다. 사용 하려면 아래 링크 중 하나에서 데이터 세트를 아카이브 파일로 다운로드하고 "generes_original" 폴더의 내용을 `data/`로 추출하십시오.
- https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification?resource=download
- http://marsyas.info/downloads/datasets.html
- http://opihi.cs.uvic.ca/sound/genres.tar.gz
