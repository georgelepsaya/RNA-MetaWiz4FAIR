import json
from schemas.minseqe import Minseqe
import sys

if __name__ == "__main__":
    if sys.argv[1] == 'minseqe':
        minseqe_schema = Minseqe.model_json_schema()
        print("Converted MINSEQE model to JSON Schema:")
        minseqe_json = json.dumps(minseqe_schema, indent=2)
        print(minseqe_json)
        save_path = "jsonschema"
        print(f"Saving JSON Schema to '{save_path}/'.")
        with open(f"{save_path}/minseqe_schema.json", "w") as f:
            f.write(minseqe_json)
