# 7. CSS 우선순위

## 7.1 CSS 우선순위

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;
  
  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS 우선 순위&lt;/title&gt;
  
  &lt;style&gt;

  p { color: red; }

  p { color: blue; }  &lt;!-- 순서 :  늦게 나온 것으로 선택 --&gt;
  
  header h3 { background-color: green; }   &lt;!-- 디테일. 하게 정의된 것으로 선택 --&gt;
  
  h3 { background-color: blue; }
  
  #color { color: yellow; }     &lt;!-- 선택자:  style &gt; ID &gt; class &gt; type --&gt;
  .color { color: pink; }
  h4 { color: gray; }
  &lt;/style&gt;

&lt;/head&gt;

&lt;body&gt;

  &lt;p&gt;순서 캐스케이딩&lt;/p&gt;

  &lt;header&gt;

  &lt;h3&gt;디테일 캐스케이딩&lt;/h3&gt;

  &lt;/header&gt;

  &lt;h4 style = "color:green;" id="color" class="color"&gt;SICT 선택자 캐스케이딩&lt;/h4&gt;

  &lt;h4 id="color" class="color"&gt;_ICT 선택자 캐스케이딩&lt;/h4&gt;

  &lt;h4 class="color"&gt;__CT 선택자 캐스케이딩&lt;/h4&gt;

  &lt;h4&gt;___T 선택자 캐스케이딩&lt;/h4&gt;
  
&lt;/body&gt;

&lt;/html&gt;



<br>

## 7.2 실제 사항

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CSS 우선 순위</title>
  
  <style>
      p { color: red; }
      p { color: blue; }  <!-- 순서 :  늦게 나온 것으로 선택 -->
      
      header h3 { background-color: green; }   <!-- 디테일. 하게 정의된 것으로 선택 -->
      h3 { background-color: blue; }
      
      #color { color: yellow; }     <!-- 선택자:  style > ID > class > type -->
      .color { color: pink; }
      h4 { color: gray; }
  </style>

</head>
<body>
  <p>순서 캐스케이딩</p>

  <header>
    <h3>디테일 캐스케이딩</h3>
  </header>

  <h4 style = "color:green;" id="color" class="color">SICT 선택자 캐스케이딩</h4>
  <h4 id="color" class="color">_ICT 선택자 캐스케이딩</h4>
  <h4 class="color">__CT 선택자 캐스케이딩</h4>
  <h4>___T 선택자 캐스케이딩</h4>
  
</body>
</html>