The authors of the dataset introduced the **Densely Segmented Supermarket (D2S)** dataset as a novel benchmark for instance-aware semantic segmentation in an industrial domain. The benchmark was meticulously designed to mimic real-world settings of automatic checkout, inventory, or warehouse systems. In the training images, only objects of a single class appeared against a homogeneous background, while the validation and test sets were more complex and diverse. The scenes were captured under different lighting conditions, rotations, and backgrounds to evaluate the robustness of instance segmentation methods.

Care was taken to ensure unambiguous labeling of every instance, resulting in pixel-precise annotations. The comprehensive labeling allowed for the use of individual instance crops for artificial data augmentation. The dataset presented various challenges relevant to the field, including limited training data and high diversity in the validation and test sets.

The instance segmentation dataset offered high-resolution images representing a real-world, industrial environment. Annotations for 60 different object categories were obtained through meticulous labeling, ensuring high-quality annotations. The authors emphasized that the training set's high-quality region annotations could be effectively used for artificial data augmentation, leading to a significant improvement in average precision (AP) on the test set.

The dataset was designed to realistically represent applications such as automatic checkout, inventory, or warehouse systems. In these scenarios, isolated products on a conveyor belt were identified, but external influences and partly occluded objects posed challenges. The dataset's object categories included common everyday products like fruits, vegetables, cereal packets, pasta, and bottles, organized in a class hierarchy tree. The dataset provided scenes captured from various angles and under different lighting settings to evaluate the robustness of instance segmentation methods.

The validation and test scenes included diverse backgrounds, while the training set was limited to images with a single homogeneous background to mimic the settings of a warehouse system.

The dataset also included instances with occlusions from objects of the same class, objects of different classes, and clutter objects with categories not present in the training images. These additions were meant to evaluate the robustness of methods to novel objects.

The data collection utilized a high-resolution industrial color camera with 1920 × 1440 pixels mounted above a turntable. The camera's intentional off-centered mounting introduced more variations in the rotated images. The scenes were rotated ten times in increments of 36 degrees, ensuring precise rotation angles.

To assess the robustness to illumination changes and reflection, each scene and rotation were captured under three different lighting settings using an LED ring light attached to the camera, spanning a wide spectrum of possible lightings.

Note, that this is a **version 1.1 of D2S annotations** - with new subsets containing specific
difficulties (not mentioned in paper), such as occlusion, clutter or random background.
