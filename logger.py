"""
Logger module for the Simple Rule-Based Chatbot.

This module handles recording user and bot conversation interactions to a text log file
with timestamp formatting and automated directory creation.
"""

from datetime import datetime
from pathlib import Path
from typing import Union, List


def log_conversation(
    user_message: str,
    bot_response: str,
    log_dir: Union[str, Path] = "logs",
    log_file: str = "conversation_history.txt"
) -> Path:
    """
    Log a conversation turn (user message and bot response) to a text file with a timestamp.

    Args:
        user_message (str): The user's input text.
        bot_response (str): The bot's response text.
        log_dir (str | Path): Directory path for storing log files.
        log_file (str): Log filename.

    Returns:
        Path: Path object pointing to the written log file.
    """
    dir_path = Path(log_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / log_file

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"[{timestamp}]\n"
        f"User: {user_message}\n"
        f"Bot: {bot_response}\n\n"
    )

    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as err:
        print(f"[Error] Could not write to conversation log at {file_path}: {err}")

    return file_path


def read_conversation_history(
    log_dir: Union[str, Path] = "logs",
    log_file: str = "conversation_history.txt",
    max_lines: int = 50
) -> List[str]:
    """
    Read recent lines from the conversation history log file.

    Args:
        log_dir (str | Path): Directory path where logs are stored.
        log_file (str): Log filename.
        max_lines (int): Maximum number of recent lines to read.

    Returns:
        List[str]: List of log line strings.
    """
    file_path = Path(log_dir) / log_file
    if not file_path.exists():
        return ["No conversation history found."]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines[-max_lines:] if len(lines) > max_lines else lines
    except Exception as err:
        return [f"[Error] Failed to read conversation history: {err}"]
