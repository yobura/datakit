from io import StringIO

class DataType:
    pass

class NumbericType:
    pass

class IntType:
    pass

class Table:
    def __init__(self, name, columns, database, schema='public'):
        self.name = name
        self.columns = columns
        self.database = database
        self.schema=schema

class StructureQueryLanguage:
    def is_primary_key(self, column):
        pass

class PostgresCreateDDL(StructureQueryLanguage):
    def to_ddl(self):
        for obj in self.objects:
            if isinstance(obj, Table):
                self.table_ddl(obj)

    def table_ddl(self, table):
        ddl = StringIO("CREATE TABLE ")
        ddl.write(table.name)
        ddl.write("\n")
        ddl.write(self.columns_to_text(self, table.columns))

        return ddl

    def columns_ddl(self, columns):
        ddl = StringIO()

        primary_key = None
        for column in columns:
            ddl.write(self.column_to_text(column))
            if self.is_primary_key(column):
                primary_key = column

        return ddl

    def column_ddl(self, column):
        ddl = StringIO()
        ddl.write(column.name)
        ddl.write(' ')
        ddl.write(column.type.to_text())
        ddl.write(column.nullable.to_text())
        ddl.write(column.default.to_text())

        return ddl

class CSVTranslater:
    def __init__(self, path):
        pass

    def yaml(self):
        pass

    def to_structure_query_language(self):
        pass

class YamlDefine:

    def __init__(self, yaml):
        pass

    def parse(self):
        objects = []
        for key in self.structures:
            obj = self.structures

            if self.instance_of_table(obj):
                objects.append(self.assemble_table(obj))

            if self.instance_of_query(obj):
                objects.append(self.assemble_query(obj))

        return objects

    def instance_of_table(self, table):
        pass

    def instance_of_query(self, query):
        pass

    def parse_table(self, table):
        pass

    def parse_query(self, query):
        pass

    def to_structure_query_language(self):
        self.structure_query_language.to_text(self.objects)