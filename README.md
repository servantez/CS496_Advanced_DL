# Ensemble Adversarial Training and Random FGSM

## Problem Statement

placeholder

## Input and Output

Input: a clean image (e.g. original MNIST image)
Output: a perturbed image (e.g. adversarial MNIST image)

## Deliverables
* [Pretrained models](https://github.com/servantez/CS496_Advanced_DL/tree/master/models) (undefended, adversarial and ensemble trained models)
* Script for [training models](https://github.com/servantez/CS496_Advanced_DL/blob/master/train_script.py)
* Script for [testing attack and defense performance] (https://github.com/servantez/CS496_Advanced_DL/blob/master/test_script.py)
* Script for [identifying optimal alpha norm] for Random FGSM attack (https://github.com/servantez/CS496_Advanced_DL/blob/master/alpha_script.py)
* Code for [Ensemble adversarial training](https://github.com/servantez/CS496_Advanced_DL/blob/master/train_adv.py) and [Random FGSM attack](https://github.com/servantez/CS496_Advanced_DL/blob/master/simple_eval.py)
* [Dockerfile](https://github.com/servantez/CS496_Advanced_DL/blob/master/Dockerfile) used to build docker image
* [Docker image](https://hub.docker.com/repository/docker/servantez/ensemble) (ready to deploy)
