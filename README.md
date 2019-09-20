# Data Kit

构思中，希望制作一个快速操作数据库的工具集。用Yaml文件来增强数据操作。

- CSV导入数据库
- 自动生成HTTP接口

```yaml
table:
  name: story
  fields:
    id:
      type: auto_increment
    title:
      type: varchar
      length: 1000
      default: "Untitled story"
      nullable: false

    article:
      type: text
      default: "Writing"
      nullable: true


  schema: public
  database: story
```

Postgres

```sql
CREATE TABLE story (
    id bigserial NOT NULL,
    title varchar(1000) NOT NULL DEFAULT "Untitled story",
    article text NULL,
    CONSTRAINT story_pk PRIMARY KEY (id)
);
```

## CSV 导入数据库

使用`dk load`指令加载csv文件，这个过程会自动创建对应的csv表格。

```
$ dk load --table story stories.csv
```
