# Information Retrieval

This repo contains solutions for the assignments from the Information Retrieval course taught by Jun.-Prof. Dr. Martin Potthast at the University of Leipzig.

https://temir.org/teaching/information-retrieval-ss23/information-retrieval-ss23.html

## TIRA and Docker commands

### Milestone 1

```console
tira-run --output-directory ${PWD}/ir-anthology-dataset --image ir-anthology --allow-network true --command '/irds_cli.sh --ir_datasets_id iranthology-ir-lab-sose2023-information-retrievers --output_dataset_path $outputDir'

tira-run --input-directory ${PWD}/ir-anthology-dataset --image webis/tira-ir-starter-pyterrier:0.0.1-base --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/full-rank-pipeline.ipynb'

docker tag ir-anthology registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-information-retrievers/ir-anthology:0.0.1

docker push registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-information-retrievers/ir-anthology:0.0.1
```

### Milestone 2

```console
tira-run --input-directory ${PWD}/ir-anthology-dataset --output-directory ${PWD}/bm25-output --image ir-lab-milestone-02 --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook pyterrier-bm25.ipynb'

tira-run --output-directory ${PWD}/bm25-output --image information-retrievers-qrels --allow-network true --command 'diffir --dataset iranthology-ir-lab-sose2023-information-retrievers --web $outputDir/run.txt > $outputDir/run.html'

tira-run --input-directory ${PWD}/bm25-output --image information-retrievers-qrels --allow-network true --command 'ir_measures iranthology-ir-lab-sose2023-information-retrievers $inputDataset/run.txt nDCG@10 MRR P@10 Recall@100'

docker tag ir-lab-milestone-02 registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-information-retrievers/milestone-02:0.0.1
```
