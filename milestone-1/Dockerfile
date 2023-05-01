FROM webis/tira-ir-datasets-starter:0.0.54

COPY iranthology.py milestone-1-documents.jsonl milestone-1-topics.xml milestone-1.ipynb /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

ENTRYPOINT [ "/irds_cli.sh" ]
