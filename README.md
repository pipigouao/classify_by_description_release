# Visual Classification via Description from Large Language Models
## Sachit Menon, Carl Vondrick

[[Paper]](link)

## Approach


![[latent-points]](./figs/latent-points.png)

The standard vision-and-language model compares image embeddings (white dot) to word embeddings of the category name (colorful dots) in order to perform classification, as illustrated in (a). We instead query large language models to automatically build descriptors, and perform recognition by comparing to the category descriptors, as shown in (b).

## Usage

First install the dependencies.

Either manually:
```
conda install pytorch torchvision -c pytorch
conda install matplotlib torchmetrics -c conda-forge
pip install git+https://github.com/openai/CLIP.git
pip install git+https://github.com/modestyachts/ImageNetV2_pytorch
```

Or using the provided `.yml` file.
```
conda env create -f classbydesc.yml
```

To reproduce accuracy results from the paper: edit the directories to match your local machine in `load.py` and set `hparams['dataset']` accordingly. Then simply run `python main.py`.

All hyperparameters can be modified in `load.py`.

To generate example decisions and explanations as well as contrast from the CLIP decision, use the `show_from_indices` function in `load.py` after having run `main.py`. Details forthcoming.

Example:
```
show_from_indices(torch.arange(images.shape[0]), images, labels, descr_predictions, clip_predictions, image_description_similarity=image_description_similarity, image_labels_similarity=image_labels_similarity)
```

Example outputs:
![[figs]](./figs/explanations.png)