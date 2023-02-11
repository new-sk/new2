# 3. 구조 (header, nav, main, article, footer)


## 3.1 구조

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;세번째 실습&lt;/title&gt;

&lt;/head&gt;

&lt;body&gt;

  &lt;!-- HTML5 header, nav, main, article, footer 등이라고 함: 확인필요 --&gt;

  &lt;header&gt;

  &lt;h1&gt; &lt;img src="./img/s0032.png" alt="회사로고"&gt;구글&lt;/h1&gt;  
  
  &lt;nav&gt;
 
  &lt;li&gt;&lt;a herf="#"&gt;홈&lt;/a&gt;&lt;/li&gt;

  &lt;li&gt;&lt;a herf="#"&gt;회사 소개&lt;/a&gt;&lt;/li&gt;

  &lt;li&gt;&lt;a herf="#"&gt;연락처&lt;/a&gt;&lt;/li&gt;
  &lt;/nav&gt;
  &lt;/header&gt;
  
  &lt;main role="main"&gt;
    
  &lt;article&gt;
  
  &lt;h2&gt;회사 소개&lt;/h2&gt;
  
  &lt;p&gt;회사 소개에 대한 본문 내용&lt;/p&gt;
  
  &lt;/article&gt;
  
  &lt;/main&gt;
  
  &lt;footer&gt;
  
  &lt;div&gt;&lt;p&gt;경기도 성남시&lt;/p&gt;&lt;/div&gt;  &lt;!-- 별도 div로 작성 ??? --&gt;

  &lt;div&gt;&lt;p&gt;010-111-2222&lt;/p&gt;&lt;/div&gt;  
  
  &lt;/footer&gt;

  &lt;!--  Block & Inline :  줄바꿈, 공간만들기, 상하배치 가능한 것은 Block이고, 아니면 Inline임 --&gt;

  &lt;h1&gt;Hello&lt;/h1&gt;&lt;h1&gt;Hello&lt;/h1&gt;&lt;h1&gt;Hello&lt;/h1&gt;
  
  &lt;a&gt;Bye&lt;/a&gt;

  &lt;a&gt;Bye&lt;/a&gt;

  &lt;a&gt;Bye&lt;/a&gt;

&lt;/body&gt;

&lt;/html&gt;  


<br>

## 2.5 실제 사항

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>세번째 실습</title>
</head>
<body>

  <!-- HTML5 header, nav, main, article, footer 등이라고 함: 확인필요 -->
  <header>
    <h1><img src="./img/s0032.png" alt="회사로고">구글</h1>  
    
    <nav>
        <li><a herf="#">홈</a></li>
        <li><a herf="#">회사 소개</a></li>
        <li><a herf="#">연락처</a></li>
    </nav>
  </header>
  
  <main role="main">
    <article>
      <h2>회사 소개</h2>
      <p>회사 소개에 대한 본문 내용</p>
    </article>
  </main>
  
  <footer>
    <div><p>경기도 성남시</p></div>  <!-- 별도 div로 작성 ??? -->
    <div><p>010-111-2222</p></div>  
  </footer>

  <!--  Block & Inline :  줄바꿈, 공간만들기, 상하배치 가능한 것은 Block이고, 아니면 Inline임 -->

  <h1>Hello</h1><h1>Hello</h1><h1>Hello</h1>
  
  <a>Bye</a>
  <a>Bye</a>
  <a>Bye</a>

</body>
</html>  
