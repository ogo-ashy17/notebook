from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(first_name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, first_name):
        return f"Hello {first_name}!"
    
    def resolve_goodbye(root, info):
        return "See ya!"
    
schema = Schema(query=Query)

# type Query {
#     hello(firstName: String = "stranger"): String
#     goodby: String
# }

query_string = '{ hello }'
result = schema.execute(query_string)
print(result.data['hello'])  # "Hello stranger!"

query_with_argument = '{ hello(firstName: "GraphQL") }'
result = schema.execute(query_with_argument)
print(result.data['hello'])  # "Hello GraphQL!"

query_string = '{ goodbye }'
result = schema.execute(query_string)
print(result)
