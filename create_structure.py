from pathlib import Path 


#project path 

folder_path = [
    "app",
    "app/templates",
    "app/static/css",
    "app/static/js",
    "worker",
    "infra",
    "scripts",
    "docs",
    ]


#project files 

files = [
    #root files
    "Requirements.txt",
    ".env",
    ".gitignore",
    "README.md",


    #Backend files

    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/db.py",
    "app/aws.py",
    "app/vector.py",
    "app/rag.py",
    "app/memory.py",
    "app/guadrail.py",
    "app/oberservability.py",


    # frontend files
    "app/templates/index.html",
    "app/static/css/style.css",
    "app/static/js/app.js",    


    #Document ingestion files
    "worker/__init__.py",
    "worker/ingest.py",


    # Data base 

    "infra/db_schema.sql",
    "scripts/init_db.py",

    # Documentation files
    "docs/SETUP.md",
    "docs/RIUS_OBERVABILITY.md",
]





def create_structure():
    # Create folders
    for folder in folder_path:
        Path(folder).mkdir(parents=True, exist_ok=True)

    # Create files
    for file in files:
        path = Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)  
        path.touch(exist_ok=True)  


    print("Project structure created successfully.")
    print(f"Total folders created: {len(folder_path)}")
    print(f"Total files : {len(files)}")


if __name__ == "__main__":
    create_structure()

