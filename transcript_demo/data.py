# data.py
EXAMPLE_ANALYSIS = {
    "session_id": "demo-001",
    "transcript": (
        "A soap bar is a small solid block used for cleaning the body. "
        "It dissolves in warm water and creates a smooth lather with a fresh citrus scent. "
        "You rub it gently on wet skin to remove grease and dirt, then rinse thoroughly. "
        "For example, before surgery nurses scrub with antimicrobial soap to reduce infection risk."
    ),
    "overall_score": 78,
    "complexity_metrics": {
        "word_count": 64,
        "unique_word_ratio": 0.72,
        "avg_word_length": 4.6
    },
    "coherence_metrics": {
        "sentence_count": 4,
        "has_clear_structure": True,
        "uses_connectives": True,
        "repetition_score": 2
    },
    "tangentiality_metrics": {"on_topic_ratio": 0.86},
    "semantic_analysis": {
        "has_definition": True,
        "has_function": True,
        "has_examples": True,
        "has_sensory_description": True,
        "matched_keywords": {
            "definition": ["soap", "block", "cleaning"],
            "function":   ["remove", "scrub", "rinse", "dissolves"],
            "examples":   ["for", "example", "surgery", "nurses"],
            "sensory":    ["smooth", "fresh", "citrus", "scent", "warm"]
        }
    },
    "flags": [
        {"severity": "low", "message": "Mild repetition detected", "evidence": "Repeated cleaning verbs"},
    ]
}
