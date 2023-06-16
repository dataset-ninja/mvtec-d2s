Please visit dataset [homepage](https://www.mvtec.com/company/research/datasets/mvtec-d2s) to download the data. 

Afterward, you have the option to download it in the universal supervisely format by utilizing the *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='MVTEC D2S', dst_path='~/dtools/datasets/MVTEC D2S.tar')
```
