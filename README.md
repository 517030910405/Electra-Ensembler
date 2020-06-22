# [Electra-Ensembler](https://github.com/517030910405/Electra-Ensembler)

## Environment Requirements

[Transformers Lib](https://github.com/huggingface/transformers) and its sub-models. 

Transformers can be installed using pip. 

## How to run the base models? 

```bash
cd src
bash ./run_many.sh
```

The new evaluation and output will be added into `allans` and `alleval`

See the hyper-params in `src/run.sh` 

## How to ensemble the models

Open `src/alleval` and select the fine-tuned models. Manually write the selected models (Score>=68) in the `src/ensemble.py`

```bash
python3 ensemble.py
```

Now, you get a `src/ens.csv`. Rename it with `CoLA.tsv` and submit. 

[<img src = "https://raw.githubusercontent.com/517030910405/Electra-Ensembler/master/test_result/gluebenchmark_submission.png?token=AKB52JPTQS53QBCVVJVW3PS66CIHC">](https://github.com/517030910405/Electra-Ensembler/tree/master/test_result)
