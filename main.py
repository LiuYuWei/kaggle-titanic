"""This file is main file."""
# import relation package.
import argparse
import sys
import uvicorn

# import project package.
from src.app.data_etl_app import DataEtlApp
from src.app.train_eval_app import TrainEvalApp
from src import create_app

app = create_app()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is main file.')
    parser.add_argument('--mode', type=str, help='Mode', required=True)
    parser.add_argument('--model', type=str, help='Model')
    args = parser.parse_args()
    if args.mode == "etl":
        data_etl_app = DataEtlApp()
        data_etl_app.start()
    elif args.mode == "train_eval":
        train_eval_app = TrainEvalApp()
        train_eval_app.start(args.model)
    elif args.mode == "serving":
        uvicorn.run('main:app')
    else:
        sys.exit(1)
