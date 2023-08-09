Dataset **MVTEC D2S** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/O/C/Yw/RbHcxmQASJrm5jtIrkmIWxZZivUIuBT5HQZieCxPS4SbKBhlhIBOp4D8wjibD733IztqkACRRkbXihVxqWTTI2meS9fwz11rmwMVwRcow09n6T0DqRiKI8RNo122.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='MVTEC D2S', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.mvtec.com/company/research/datasets/mvtec-d2s)