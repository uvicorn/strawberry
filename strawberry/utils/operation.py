from typing import Optional, cast

from graphql.language import DocumentNode, OperationDefinitionNode, OperationType


def get_first_operation(
    graphql_document: DocumentNode,
) -> Optional[OperationDefinitionNode]:
    return next(
        (
            definition
            for definition in graphql_document.definitions
            if isinstance(definition, OperationDefinitionNode)
        ),
        None,
    )


def get_operation_type(
    graphql_document: DocumentNode, operation_name: Optional[str] = None
) -> OperationType:
    definition: Optional[OperationDefinitionNode] = None

    if operation_name:
        for d in graphql_document.definitions:
            d = cast(OperationDefinitionNode, d)
            if d.name and d.name.value == operation_name:
                definition = d
                break
    else:
        definition = get_first_operation(graphql_document)

    if not definition:
        raise RuntimeError("Can't get GraphQL operation type")

    return definition.operation
