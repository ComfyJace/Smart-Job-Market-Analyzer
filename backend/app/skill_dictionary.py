SKILL_DEFINITIONS = {
    "python": {
        "aliases": ["python", "python3", "python 3"],
        "short_aliases": ["py"],
        "category": "language",
    },
    "sql": {
        "aliases": ["sql"],
        "short_aliases": [],
        "category": "database",
    },
    "pandas": {
        "aliases": ["pandas"],
        "short_aliases": ["pd"],
        "category": "library",
    },
    "numpy": {
        "aliases": ["numpy", "numerical python"],
        "short_aliases": ["np"],
        "category": "library",
    },
    "machine learning": {
        "aliases": ["machine learning", "machine-learning"],
        "short_aliases": ["ml"],
        "category": "concept",
    },
    "deep learning": {
        "aliases": ["deep learning", "deep-learning"],
        "short_aliases": ["dl"],
        "category": "concept",
    },
    "pytorch": {
        "aliases": ["pytorch", "torch"],
        "short_aliases": [],
        "category": "framework",
    },
    "tensorflow": {
        "aliases": ["tensorflow"],
        "short_aliases": ["tf"],
        "category": "framework",
    },
    "aws": {
        "aliases": ["aws", "amazon web services"],
        "short_aliases": [],
        "category": "cloud",
    },
    "docker": {
        "aliases": ["docker", "dockerized"],
        "short_aliases": [],
        "category": "devops",
    },
    "kubernetes": {
        "aliases": ["kubernetes"],
        "short_aliases": ["k8s"],
        "category": "devops",
    },
    "java": {
        "aliases": ["java"],
        "short_aliases": [],
        "category": "language",
    },
    "c++": {
        "aliases": ["c++", "cpp", "c plus plus"],
        "short_aliases": [],
        "category": "language",
    },
    "javascript": {
        "aliases": ["javascript"],
        "short_aliases": ["js"],
        "category": "language",
    },
    "postgresql": {
        "aliases": ["postgresql", "postgres", "postgre", "postgres sql"],
        "short_aliases": [],
        "category": "database",
    },
    "selenium": {
        "aliases": ["selenium", "selenium webdriver"],
        "short_aliases": [],
        "category": "testing",
    },
    "fastapi": {
        "aliases": ["fastapi", "fast api"],
        "short_aliases": [],
        "category": "framework",
    },
    "scikit-learn": {
        "aliases": ["scikit-learn", "scikit learn", "sklearn"],
        "short_aliases": [],
        "category": "framework",
    },
}

CATEGORY_TEMPLATES = {
    "language": {
        "prefixes": [["experience", "with"], ["experience", "in"], ["proficiency", "in"]],
        "suffixes": [["developer"], ["programming"], ["scripting"]],
    },
    "framework": {
        "prefixes": [["experience", "with"], ["knowledge", "of"], ["hands-on", "experience", "with"]],
        "suffixes": [["framework"], ["development"], ["implementation"]],
    },
    "library": {
        "prefixes": [["experience", "with"], ["using"], ["knowledge", "of"]],
        "suffixes": [["library"]],
    },
    "cloud": {
        "prefixes": [["experience", "with"], ["working", "with"], ["knowledge", "of"]],
        "suffixes": [["cloud"], ["services"], ["deployment"]],
    },
    "devops": {
        "prefixes": [["experience", "with"], ["hands-on", "experience", "with"], ["knowledge", "of"]],
        "suffixes": [["containers"], ["automation"], ["orchestration"], ["deployment"]],
    },
    "database": {
        "prefixes": [["experience", "with"], ["proficiency", "in"], ["knowledge", "of"]],
        "suffixes": [["database"], ["queries"], ["sql"]],
    },
    "concept": {
        "prefixes": [["experience", "with"], ["knowledge", "of"], ["understanding", "of"], ["background", "in"]],
        "suffixes": [["models"], ["algorithms"], ["techniques"], ["methods"]],
    },
    "testing": {
        "prefixes": [["experience", "with"], ["knowledge", "of"], ["hands-on", "experience", "with"]],
        "suffixes": [["testing"], ["automation"], ["webdriver"]],
    },
}

SPECIAL_CASE_PATTERNS = {
    "c++": [["c", "plus", "plus"]],
    "fastapi": [["fast", "api"]],
    "scikit-learn": [["scikit", "learn"]],
    "aws": [["amazon", "web", "services"]],
    "machine learning": [["ml", "engineer"]],
}

def get_skill_definitions():
    return SKILL_DEFINITIONS

def get_canonical_skill_names(skill_definitions):
    return list(skill_definitions.keys())

def get_alias_map(include_short_aliases: bool = False):
    alias_map = {}

    for canonical_skill, meta in SKILL_DEFINITIONS.items():
        for alias in meta["aliases"]:
            alias_map[alias.lower()] = canonical_skill
        
        if include_short_aliases:
            for short_alias in meta.get("short_aliases", []):
                alias_map[short_alias.lower()] = canonical_skill

    return alias_map

def build_alias_to_skill(skill_definitions):
    alias_to_skill = {}
    for skill, meta in skill_definitions.items():
        for alias in meta["aliases"]:
            alias_to_skill[alias.lower()] = skill
    return alias_to_skill


def build_short_alias_to_skill(skill_definitions):
    short_alias_to_skill = {}
    for skill, meta in skill_definitions.items():
        for alias in meta.get("short_aliases", []):
            short_alias_to_skill[alias.lower()] = skill
    return short_alias_to_skill

def validate_skill_definitions(skill_definitions, category_templates):
    for skill, meta in skill_definitions.items():
        if "aliases" not in meta or not meta["aliases"]:
            raise ValueError(f"{skill} must have at least one alias")
        if "category" not in meta:
            raise ValueError(f"{skill} is missing a category")
        if meta["category"] not in category_templates:
            raise ValueError(f"{skill} has unknown category: {meta['category']}")