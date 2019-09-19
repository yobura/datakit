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

```sql
CREATE TABLE story (
    id bigserial NOT NULL,
    title varchar(1000) NOT NULL DEFAULT "Untitled story",
    article varchar(1000) NULL,
    CONSTRAINT story_pk PRIMARY KEY (id)
);
```