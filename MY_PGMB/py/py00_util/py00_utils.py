def load_sql_query(filename, query_name):

  with open(filename, "r", encoding="utf-8") as file:
      queries = file.read().split("-- ")  # 주석을 기준으로 분할
  
  query_dict = {}
  for query in queries:
      lines = query.strip().split("\n")
      if len(lines) > 1:
          name = lines[0].strip()  # 첫 줄을 쿼리 이름으로 사용
          sql = "\n".join(lines[1:]).strip()  # 나머지를 SQL 문으로 저장
          query_dict[name] = sql
  
  return query_dict.get(query_name, None)  # 요청한 쿼리 반환
