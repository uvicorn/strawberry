import typing

import strawberry
from strawberry.extensions import Extension
from strawberry.file_uploads import Upload


class MyExtension(Extension):
    def get_results(self):
        return {"example": "example"}


@strawberry.input
class FolderInput:
    files: typing.List[Upload]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def read_text(self, text_file: Upload) -> str:
        return text_file.read().decode()

    @strawberry.mutation
    def read_files(self, files: typing.List[Upload]) -> typing.List[str]:
        return [file.read().decode() for file in files]

    @strawberry.mutation
    def read_folder(self, folder: FolderInput) -> typing.List[str]:
        return [file.read().decode() for file in folder.files]


@strawberry.type
class Query:
    hello: str = "🍓"

    @strawberry.field
    def hi(self, name: str) -> str:
        return f"Hi {name}!"


schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[MyExtension])
