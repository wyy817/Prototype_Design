import json
import os
from pathlib import Path

def get_data_path(filename):
    """Get the absolute path to a data file"""
    current_dir = Path(__file__).parent.parent
    return current_dir / "data" / filename

def load_json(filename):
    """Load JSON data from data directory"""
    try:
        with open(get_data_path(filename), 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filename} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Warning: {filename} contains invalid JSON")
        return {}

def load_all_data():
    """Load all required data files"""
    competitors = load_json('competitors.json')
    market = load_json('market_data.json')
    segments = load_json('customer_segments.json')
    financials = load_json('dingdong_financials.json')
    
    return competitors, market, segments, financials
