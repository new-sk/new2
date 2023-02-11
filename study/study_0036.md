# 6. CSS 상속

## 6.1 CSS 상속

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS 속성의 상속&lt;/title&gt;
  
  &lt;style&gt;
  
  header { color: blue; }.      &lt;!-- 부모의 속성을 자식이 물려받는다. (일부) --&gt;
  
  header p { color: red; }.     &lt;!-- 특정 부모의 자식만의 속성 정의 방법 --&gt;
  
  p {color: green; }
  
  &lt;/style&gt;

&lt;/head&gt;

&lt;body&gt;

  &lt;header&gt;

  &lt;h2&gt;header h2&lt;/h2&gt;

  &lt;p&gt;header p&lt;/p&gt;

  &lt;/header&gt;
  
  &lt;footer&gt;

  &lt;h2&gt;footer h2&lt;/h2&gt;

  &lt;p&gt;footer p&lt;/p&gt;

  &lt;/footer&gt;

&lt;/body&gt;

&lt;/html&gt;



<br>

## 6.2 실제 사항

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CSS 속성의 상속</title>
  
  <style>
    header { color: blue; }.      <!-- 부모의 속성을 자식이 물려받는다. (일부) -->
    header p { color: red; }.     <!-- 특정 부모의 자식만의 속성 정의 방법 -->
    p {color: green; }
  </style>
</head>

<body>
  <header>
    <h2>header h2</h2>
    <p>header p</p>
  </header>
  
  <footer>
    <h2>footer h2</h2>
    <p>footer p</p>
  </footer>
</body>

</html>