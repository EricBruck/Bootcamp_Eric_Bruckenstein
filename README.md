# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Class Materials Rules
- Each stage's handouts go in their own subfolder, named exactly as the course
folder, e.g. `class_materials/stage01_problem-framing-and-scoping/`.
- Run lecture notebooks in place from that folder.
- Copy a homework starter into `homework/homeworkN/` before working on it.
## Project Folder Rules
- Keep project files organized and clearly named.
- The project folder structure is set up in Stage 02.

## Data Storage Architecture
**Folder Structure:** - `data/raw/`: Stores immutable, unedited datasets right after ingestion.
- `data/processed/`: Stores cleaned, validated datasets ready for analysis or modeling.

**Format Choices:** - **CSV** is used primarily for the `raw/` directory because of its interoperability, ease of auditing, and human readability.
- **Parquet** is leveraged for the `processed/` directory due to its columnar compression, automatic datatype enforcement (schemas), and rapid read/write speeds for large downstream workflows.

**Environment Configurations:** File pathways are controlled using `python-dotenv` variables (`DATA_DIR_RAW` and `DATA_DIR_PROCESSED`). This prevents brittle, hard-coded string paths from breaking on differing machines and enforces uniform directory targets across all project scripts.

## Data Storage Architecture
**Folder Structure:** - `data/raw/`: Stores immutable, unedited datasets right after ingestion.
- `data/processed/`: Stores cleaned, validated datasets ready for analysis or modeling.

**Format Choices:** - **CSV** is used primarily for the `raw/` directory because of its interoperability, ease of auditing, and human readability.
- **Parquet** is leveraged for the `processed/` directory due to its columnar compression, automatic datatype enforcement (schemas), and rapid read/write speeds for large downstream workflows.

**Environment Configurations:** File pathways are controlled using `python-dotenv` variables (`DATA_DIR_RAW` and `DATA_DIR_PROCESSED`). This prevents brittle, hard-coded string paths from breaking on differing machines and enforces uniform directory targets across all project scripts.
