"""
Knowledge base loader and query matcher for the Simple Rule-Based Chatbot.

This module handles reading the domain Q&A dataset from a JSON file and searching
for matching topics based on user query keyword matching.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, Optional, Union


def load_knowledge_base(file_path: Union[str, Path] = "data/knowledge_base.json") -> Dict[str, str]:
    """
    Load the domain knowledge base from a JSON file.

    Args:
        file_path (str | Path): Path to the knowledge base JSON file.

    Returns:
        Dict[str, str]: Dictionary mapping domain terms to their answers.
                        Returns empty dict if file is missing or invalid.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"[Warning] Knowledge base file not found at: {path}")
        return {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return {str(k).lower(): str(v) for k, v in data.items()}
            else:
                print(f"[Warning] Invalid knowledge base format in {path}. Expected JSON object.")
                return {}
    except json.JSONDecodeError as err:
        print(f"[Error] Failed to parse JSON in knowledge base file {path}: {err}")
        return {}
    except Exception as err:
        print(f"[Error] Unexpected error loading knowledge base file {path}: {err}")
        return {}


def normalize_query(query: str) -> str:
    """
    Normalize query text by lowercasing and removing punctuation.

    Args:
        query (str): Raw input query string.

    Returns:
        str: Normalized query string.
    """
    if not query:
        return ""
    text = query.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def search_knowledge_base(user_input: str, kb_data: Dict[str, str]) -> Optional[str]:
    """
    Search the knowledge base for a matching topic based on user input.

    Args:
        user_input (str): User input message.
        kb_data (Dict[str, str]): Loaded knowledge base key-value pairs.

    Returns:
        Optional[str]: Found answer from knowledge base or None if no match.
    """
    if not user_input or not kb_data:
        return None

    normalized_input = normalize_query(user_input)
    if not normalized_input:
        return None

    # Step 1: Check for exact key substring match in user query (best match)
    # Sort keys by length descending to match longer phrases first (e.g. "supervised learning" before "learning")
    sorted_keys = sorted(kb_data.keys(), key=len, reverse=True)

    for key in sorted_keys:
        normalized_key = normalize_query(key)
        # Word boundary check for the topic key inside input
        pattern = r"\b" + re.escape(normalized_key) + r"\b"
        if re.search(pattern, normalized_input):
            return kb_data[key]

    # Step 2: Fallback keyword overlap matching if no word-boundary match occurred
    query_tokens = set(normalized_input.split())
    best_match_key = None
    max_score = 0.0

    for key in sorted_keys:
        key_tokens = set(normalize_query(key).split())
        if not key_tokens:
            continue

        # Calculate overlap coefficient
        intersection = query_tokens.intersection(key_tokens)
        if intersection:
            score = len(intersection) / len(key_tokens)
            if score > max_score and score >= 0.5:
                max_score = score
                best_match_key = key

    if best_match_key:
        return kb_data[best_match_key]

    return None
