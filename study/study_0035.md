# 5. 선택자

## 5.1 선택자

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS 선택자&lt;/title&gt;
  
  &lt;style&gt;

  h2 { color:red; }   &lt;!-- type  태그명으로 사용  --&gt;

  .coding { color:green; }  &lt;!-- class  여러군데 사용  --&gt;

  #coding { color:yellow; }  &lt;!-- ID 한군데에서만 사용 --&gt;

  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;

&lt;!-- 우선순위  ID &gt; Class &gt; Type --&gt;

&lt;h2&gt;TYPE : 기본 red&lt;/h2&gt;

&lt;h2 class="coding"&gt;CLASS(.) : green&lt;/h2&gt;

&lt;h2 id="coding"&gt;ID(#) : yellow&lt;/h2&gt;

&lt;/body&gt;

&lt;/html&gt;



<br>

## 5.2 실제 사항

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CSS 선택자</title>
  
  <style>
      h2 { color:red; }   <!-- type  태그명으로 사용  -->
      .coding { color:green; }  <!-- class  여러군데 사용  -->
      #coding { color:yellow; }  <!-- ID 한군데에서만 사용 -->
  </style>
  
</head>
<body>

<!-- 우선순위  ID > Class > Type -->
<h2>TYPE : 기본 red</h2>
<h2 class="coding">CLASS(.) : green</h2>
<h2 id="coding">ID(#) : yellow</h2>

</body>
</html>