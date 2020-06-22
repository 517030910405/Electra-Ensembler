# [Electra-Ensembler](https://github.com/517030910405/Electra-Ensembler)

This repo is a single-task fine-tuning focused on CoLA Glue. It uses the Electra-Large as its base models and ensemble them with a newly-proposed ensemble method. It achieves 62.9 in CoLA defeating the Electra-Large. 

For detailed information, please see the paper. 

## Environment Requirements

[Transformers Lib](https://github.com/huggingface/transformers) and its sub-models. 

Transformers can be installed using pip. 

## How to run the base models? 

```bash
cd src
bash ./run_many.sh
```

The new evaluation and output will be added into `src/allans` and `src/alleval`

See the hyper-params in `src/run.sh` 

## How to ensemble the models

Open `src/alleval` and select the fine-tuned models. Manually write the selected models (Score>=68) in the `src/ensemble.py`

```bash
python3 ensemble.py
```

Now, you get a `src/ens.csv`. Rename it with `CoLA.tsv` and submit. 

[<img src = "https://github.com/517030910405/Electra-Ensembler/raw/master/test_result/gluebenchmark_submission.png">](https://github.com/517030910405/Electra-Ensembler/tree/master/test_result)
