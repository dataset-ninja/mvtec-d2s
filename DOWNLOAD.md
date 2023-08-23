Dataset **MVTec D2S** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/R/Q/gC/9pnMTzLXmYUvI9jb1r0PIGNE1XtN4nh3Y4uW59NME3mpQtv9iStG7FmCePSJCXuyD0x5WFP4rumAAYj2SM4fxTiAlSf8pirfxROOAYdGDp7FcQdIYcsuoeKTI1Yk.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='MVTec D2S', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.mvtec.com/company/research/datasets/mvtec-d2s).