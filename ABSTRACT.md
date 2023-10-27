The authors of the dataset introduced the **Densely Segmented Supermarket (D2S)** dataset as a novel benchmark for instance-aware semantic segmentation in an industrial domain. The benchmark was meticulously designed to mimic real-world settings of automatic checkout, inventory, or warehouse systems. In the training images, only objects of a single class appeared against a homogeneous background, while the validation and test sets were more complex and diverse. The scenes were captured under different lighting conditions, rotations, and backgrounds to evaluate the robustness of instance segmentation methods.

Care was taken to ensure unambiguous labeling of every instance, resulting in pixel-precise annotations. The comprehensive labeling allowed for the use of individual instance crops for artificial data augmentation. The dataset presented various challenges relevant to the field, including limited training data and high diversity in the validation and test sets.

The instance segmentation dataset offered high-resolution images representing a real-world, industrial environment. Annotations for 60 different object categories were obtained through meticulous labeling, ensuring high-quality annotations. The authors emphasized that the training set's high-quality region annotations could be effectively used for artificial data augmentation, leading to a significant improvement in average precision (AP) on the test set.

<img src="https://github.com/supervisely/supervisely/assets/78355358/d3b26cc7-7fdd-49b1-a980-577c4957bdaa" alt="image" width="800">

The dataset was designed to realistically represent applications such as automatic checkout, inventory, or warehouse systems. In these scenarios, isolated products on a conveyor belt were identified, but external influences and partly occluded objects posed challenges. The dataset's object categories included common everyday products like fruits, vegetables, cereal packets, pasta, and bottles, organized in a class hierarchy tree. The dataset provided scenes captured from various angles and under different lighting settings to evaluate the robustness of instance segmentation methods.

| split                | all   | train        | val          | test         |
| -------------------- | ----- | ------------ | ------------ | ------------ |
| scenes               | 700   | 146          | 120          | 434          |
| images               | 21000 | 4380         | 3600         | 13020        |
| objects              | 72447 | 6900         | 15654        | 49893        |
| objects/image        | 3.45  | 1.58         | 4.35         | 3.83         |
| scenes w. occlusion  | 393   | 10           | 84           | 299          |
| scenes w. clutter    | 86    | 0            | 18           | 68           |
| rotations            |       | **✓** | **✓** | **✓** |
| lighting variation   |       | **✓** | **✓** | **✓** |
| background variation |       |              | **✓** | **✓** |
| clutter              |       |              | **✓** | **✓** |

To meet the mentioned industrial requirements, the training scenes are selected to be as simple as possible: They have a homogeneous background, mostly contain only one object and the amount of occlusions is reduced to a minimum. 

*train* split properties:
* contain only objects of one category
* provide new views of an object
* only contain objects with no or marginal overlap
* have no ***clutter*** and a ***homogeneous background***

The remaining scenes are split between the *validation* and the *test* set. They consist of scenes with:
* single or multiple objects of different classes
* touching or objects with ***occlusion***
* ***clutter*** objects
* ***random background***

The dataset also included <i>ablation study</i> which is performed to evaluate importances of different variations including all rotations and lightings for one placement of objects in the scene, and the ability of methods to learn invariance with respect to rotations and illumination. For this purpose, authors created three subsets of the full training set train. The train ***rot0*** set contains all three lightings, but only the first rotation of each scene. The train ***light0*** set contains only the default lighting, but all ten rotations of each scene. The train ***rot0_light0*** set contains only the default lighting and the first rotation for each scene.

The data collection utilized a high-resolution industrial color camera with 1920 × 1440 pixels mounted above a turntable. The camera's intentional off-centered mounting introduced more variations in the rotated images. The scenes were rotated ten times in increments of 36 degrees, ensuring precise rotation angles. To assess the robustness to illumination changes and reflection, each scene and rotation were captured under three different lighting settings using an LED ring light attached to the camera, spanning a wide spectrum of possible lightings.

<i>Note, that this is a **version 1.1 of D2S annotations** - with new subsets containing specific difficulties (not mentioned in paper), such as occlusion, clutter or random background.</i>
