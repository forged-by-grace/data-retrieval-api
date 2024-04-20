import os
import argparse


class ModelCreator:
    def __init__(self, model_name):
        self.model_name = model_name


    def create_model_files(self):
        model_dir = f"./src/models/{self.model_name.lower()}"
        os.makedirs(model_dir)

        # Validate model name
        if not self.model_name.isidentifier():
            raise ValueError("Invalid model name. Model name must be a valid Python identifier.")

        # Validate table name pattern
        table_name = f"tab{self.model_name}"
        if not table_name.isidentifier():
            raise ValueError("Invalid table name pattern. Table name must follow the pattern 'tab<ModelName>'.")

        # Create model_name.py
        with open(f"{model_dir}/{self.model_name.lower()}.py", "w") as f:
            # Create the Document base class with validation using both SQLALCHEMY and declarative base class
            f.write("from sqlalchemy import Column, Integer, String, DateTime, Text\n")
            f.write("from src.database.database import Base\n")
            f.write("from datetime import datetime\n\n")


            f.write("class Document(Base):\n")
            f.write(f"  __tablename__ = '{table_name}'\n\n")
            f.write(f"  id = Column(Integer(), primary_key=True, index=True)\n")
            f.write(f"  model_name = Column(String, index=True, nullable=False)\n")
            f.write(f"  created_at = Column(DateTime(), default=datetime.now(), nullable=False)\n")
            f.write(f"  updated_at = Column(DateTime(), nullable=True)\n\n")

            f.write(f"class {self.model_name.title()}(Document):\n")
            f.write(f"    pass\n")

        # Create model_name.json 
        with open(f"{model_dir}/{self.model_name.lower()}.json", "w") as f:
            f.write('{\n')
            f.write('    "fields": [\n')
            f.write('        {\n')
            f.write('            "id": "123456adased",\n')
            f.write('            "type": "string",\n')
            f.write('            "optional": "False"\n')
            f.write('        },\n')
            f.write('        {\n')
            f.write(f'            "model_name": "{self.model_name.lower()}",\n')
            f.write('            "type": "string",\n')
            f.write('            "optional": "False"\n')
            f.write('        },\n')
            f.write('        {\n')
            f.write('            "created_at": "19-04-2023T06:28:234",\n')
            f.write('            "type": "datetime",\n')
            f.write('            "optional": "False"\n')
            f.write('        },\n')
            f.write('        {\n')
            f.write('            "updated_at": "19-04-2023T06:28:234",\n')
            f.write('            "type": "datetime",\n')
            f.write('            "optional": "True"\n')
            f.write('        }\n')
            f.write('    ]\n')
            f.write('}\n')

def main():
    parser = argparse.ArgumentParser(description="CLI tool to create new models in the database.")
    parser.add_argument("command", type=str, help="Command to be carried out on the model. E.g (create-model, delete-model, etc.)")
    parser.add_argument("model_name", type=str, help="Name of the model to create")
    args = parser.parse_args()

    # Validate command
    if args.command == 'create-model':
        model_creator = ModelCreator(args.model_name)
        model_creator.create_model_files()
        print(f"Model '{args.model_name}' created successfully.")
    else: 
        raise ValueError("Invalid command. Supported command include; 'create-model': Used for creating new model structure.")   


if __name__ == "__main__":
    main()
