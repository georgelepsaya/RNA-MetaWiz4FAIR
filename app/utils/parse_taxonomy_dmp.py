from collections import defaultdict
from typing import Any


def parse_names_dmp(file_path: str):
    names: dict[str, dict[str, Any]] = defaultdict(lambda: {"synonyms": []})
    
    with open(file_path, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split("|")]
            tax_id, name_txt, _, name_class = parts[:4]
            if name_class == "scientific name":
                names[tax_id]["scientific_name"] = name_txt
            elif name_class == "synonym":
                names[tax_id]["synonyms"].append(name_txt)

    return names


def parse_nodes_dmp(file_path: str):
    nodes: dict[str, dict[str, str]] = {}

    with open(file_path, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split("|")]
            tax_id, parent_tax_id, rank = parts[0], parts[1], parts[2]
            nodes[tax_id] = {"parent": parent_tax_id, "rank": rank}
    
    return nodes
