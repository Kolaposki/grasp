# encoding: utf-8

from grasp import *

v1 = {'x': 1, 'y': 2}
v2 = {'x': 3, 'y': 4}
v3 = {'x': 5, 'y': 6}
v4 = {'x': 7, 'y': 0}

assert round( distance(v1, v2)              , 2) ==  2.83
assert round(      dot(v1, v2)              , 2) == 11.00
assert round(     norm(v1)                  , 2) ==  2.24
assert round(      cos(v1, v2)              , 2) ==  0.02
assert round(      knn(v1, (v2, v3))[0][0]  , 2) ==  0.98
assert             knn(v1, (v2, v3))[0][1]       ==  v2
assert          sparse(v4)                       == {'x': 7}
assert              tf(v4)                       == {'x': 1, 'y': 0}
assert       features((v1, v2))                  == set(('x', 'y'))
assert next(    tfidf((v1, v2)))['x']            ==  0.25
assert       centroid((v1, v2))                  == {'x': 2, 'y': 3}

assert scan(u'Here, kitty kitty!'              ) == [4, 17]
assert scan(u'Here, kitty!'                    ) == [4, 11]

assert tokenize(u'(hello) (:'                  ) == u'( hello ) (:'
assert tokenize(u'References [123] (...) :-)'  ) == u'References [123] (...) :-)'
assert tokenize(u'Cats &amp; dogs &#38; etc.'  ) == u'Cats &amp; dogs &#38; etc.'
assert tokenize(u"I'll eat pizza w/ tuna :-)"  ) == u"I 'll eat pizza w/ tuna :-)"
assert tokenize(u'Google (http://google.com)'  ) == u'Google ( http://google.com )'
assert tokenize(u'Also see: www.google.com.'   ) == u'Also see : www.google.com .'
assert tokenize(u'e.g., google.de, google.be'  ) == u'e.g. , google.de , google.be'
assert tokenize(u'One! 😍 Two :) :) Three'     ) == u'One ! 😍\nTwo :) :)\nThree'
assert tokenize(u'Aha!, I see:) Super'         ) == u'Aha ! , I see :)\nSuper'
assert tokenize(u"U.K.'s J. R. R. Tolkien"     ) == u"U.K. 's J. R. R. Tolkien"
assert tokenize(u'your.name@gmail.com!'        ) == u'your.name@gmail.com !'
assert tokenize(u'http://google.com?p=1'       ) == u'http://google.com?p=1'
assert tokenize(u'"Citation." Next p.5'        ) == u'" Citation . "\nNext p.5'
assert tokenize(u'"Oh! Nice!" he said'         ) == u'" Oh ! Nice ! " he said'
assert tokenize(u'"Oh!" Nice.'                 ) == u'" Oh ! "\nNice .'
assert tokenize(u'Oh... Nice.'                 ) == u'Oh ...\nNice .'
assert tokenize(u'Oh! #wow Nice.'              ) == u'Oh ! #wow\nNice .'
assert tokenize(u'Hello.Hello! 20:10'          ) == u'Hello .\nHello !\n20:10'
assert tokenize(u'pre-\ndetermined'            ) == u'predetermined'

assert Tagged('//PUNC')                          == [('/', 'PUNC')]

s1 = u"Here/PRON 's/VERB my/PRON new/ADJ cool/ADJ cat/NOUN café/NOUN !/PUNC :-D/:)"
s2 = u'1\/2/NUM'

assert list(map(u, chunk(r'^? ?'         , s1))) == [u"Here/PRON 's/VERB"]
assert list(map(u, chunk(r'^-'           , s1))) == [u'Here/PRON']
assert list(map(u, chunk(r'^PRON'        , s1))) == [u'Here/PRON']
assert list(map(u, chunk(r'PRON'         , s1))) == [u'Here/PRON', u'my/PRON']
assert list(map(u, chunk(r'BE'           , s1))) == [u"'s/VERB"]
assert list(map(u, chunk(r'VERB'         , s1))) == [u"'s/VERB"]
assert list(map(u, chunk(r'AD[JV]'       , s1))) == [u'new/ADJ', u'cool/ADJ']
assert list(map(u, chunk(r'ADJ'          , s1))) == [u'new/ADJ', u'cool/ADJ']
assert list(map(u, chunk(r'ADJ+'         , s1))) == [u'new/ADJ cool/ADJ']
assert list(map(u, chunk(r'ADJ+ NOUN'    , s1))) == [u'new/ADJ cool/ADJ cat/NOUN']
assert list(map(u, chunk(r'ADJ|NOUN+'    , s1))) == [u'new/ADJ cool/ADJ cat/NOUN café/NOUN']
assert list(map(u, chunk(u'ADJ ca-'      , s1))) == [u'cool/ADJ cat/NOUN']
assert list(map(u, chunk(u'ca-'          , s1))) == [u'cat/NOUN', u'café/NOUN']
assert list(map(u, chunk(u'Ca-'          , s1))) == [u'cat/NOUN', u'café/NOUN']
assert list(map(u, chunk(u'-é'           , s1))) == [u'café/NOUN']
assert list(map(u, chunk(u'-é/NOUN'      , s1))) == [u'café/NOUN']
assert list(map(u, chunk(u'-é/noun'      , s1))) == []
assert list(map(u, chunk(u'-é/VERB'      , s1))) == []
assert list(map(u, chunk(r'NOUN ? ?$'    , s1))) == [u'café/NOUN !/PUNC :-D/:)']
assert list(map(u, chunk(r'PUNC ?$'      , s1))) == [u'!/PUNC :-D/:)']
assert list(map(u, chunk(r':\) ?$'       , s1))) == [u':-D/:)']
assert list(map(u, chunk(r':\)'          , s1))) == [u':-D/:)']
assert list(map(u, chunk(r'1/2'          , s2))) == []
assert list(map(u, chunk(r'1\/2'         , s2))) == [u'1\\/2/NUM']
assert list(map(u, chunk(r'1\/2/NUM'     , s2))) == [u'1\\/2/NUM']

assert u(list(constituents(s1))[0][0])           == u'Here/PRON'
assert u(list(constituents(s1))[1][0])           == u"'s/VERB"
assert u(list(constituents(s1))[2][0])           == u'my/PRON new/ADJ cool/ADJ cat/NOUN café/NOUN'
assert u(list(constituents(s1))[3][0])           == u'!/PUNC'
assert   list(constituents(s1))[0][1]            == u'NP'
assert   list(constituents(s1))[1][1]            == u'VP'
assert   list(constituents(s1))[2][1]            == u'NP'
assert   list(constituents(s1))[3][1]            == u''

assert list( chngrams('cats', 2))                == ['ca', 'at', 'ts']
assert list(   ngrams(('cats', '&', 'dogs'), 2)) == [('cats', '&'), ('&', 'dogs')]
assert list(   ngrams('cats & dogs', 2))         == [('cats', '&'), ('&', 'dogs')]
assert list(skipgrams('cats & dogs', 1))         == [('cats', ('&',)), ('&', ('cats', 'dogs')), 
                                                     ('dogs', ('&',))]

e1 = DOM('<div id="main"><div class="story"><p>1</p><p>2</p></div</div>')
e2 = DOM('<div><a href="http://www.site.com">x</a></div>')

assert list(map(u, e1('#main'                ))) == [u(e1)]
assert list(map(u, e1('*#main'               ))) == [u(e1)]
assert list(map(u, e1('div#main'             ))) == [u(e1)]
assert list(map(u, e1('.story'               ))) == [u'<div class="story"><p>1</p><p>2</p></div>']
assert list(map(u, e1('div div'              ))) == [u'<div class="story"><p>1</p><p>2</p></div>']
assert list(map(u, e1('div < p'              ))) == [u'<div class="story"><p>1</p><p>2</p></div>']
assert list(map(u, e1('div > p'              ))) == [u'<p>1</p>', u'<p>2</p>']
assert list(map(u, e1('div div p'            ))) == [u'<p>1</p>', u'<p>2</p>']
assert list(map(u, e1('div p:first-child'    ))) == [u'<p>1</p>']
assert list(map(u, e1('div p:nth-child(1)'   ))) == [u'<p>1</p>']
assert list(map(u, e1('div p:nth-child(2)'   ))) == [u'<p>2</p>']
assert list(map(u, e1('p:not(":first-child")'))) == [u'<p>2</p>']
assert list(map(u, e1('div p:contains("2")'  ))) == [u'<p>2</p>']
assert list(map(u, e1('p + p'                ))) == [u'<p>2</p>']
assert list(map(u, e1('p ~ p'                ))) == [u'<p>2</p>']
assert list(map(u, e2('*[href]'              ))) == [u'<a href="http://www.site.com">x</a>']
assert list(map(u, e2('a[href^="http://"]'   ))) == [u'<a href="http://www.site.com">x</a>']
assert list(map(u, e2('a[href$=".com"]'      ))) == [u'<a href="http://www.site.com">x</a>']
assert list(map(u, e2('a[href*="site"]'      ))) == [u'<a href="http://www.site.com">x</a>']

assert plaintext(e2                            ) == u'x'
assert plaintext(e2, keep={'a': []}            ) == u'<a>x</a>'
assert plaintext(e2, keep={'a': ['href']}      ) == u'<a href="http://www.site.com">x</a>'
assert plaintext(e2, ignore='a'                ) == u''
assert plaintext(u'<a>b</a>\nc'                ) == u'b c'
assert plaintext('<a>b </a>c'                  ) == u'b c'
assert plaintext('<p>b </p>c'                  ) == u'b\n\nc'

assert sep     (u"'a's b, c (d).'"             ) == u"'a 's b , c ( d ) . '"
assert encode  (u'<a> & <b>'                   ) == u'&lt;a&gt; &amp; &lt;b&gt;'
assert decode  (u'&lt;a&gt; &amp; &lt;b&gt;'   ) == u'<a> & <b>'
assert decode  (u'http://google.com?q=%22x%22' ) == u'http://google.com?q="x"'
assert decode  (u'decode("%22") = "%22"'       ) == u'decode("%22") = "%22"'
assert detag   (u'<a>b</a>\nc'                 ) == u'b\nc'
assert detag   (u'<a>a</a>&<b>b</b>'           ) == u'a&b'
assert destress(u'pâté'                        ) == u'pate'
assert deflood (u'Woooooow!!!!!!'         , n=3) == u'Wooow!!!'
assert decamel (u'HTTPError404NotFound'        ) == u'http_error_404_not_found'
assert sg      (u'cats'                        ) == u'cat'
assert sg      (u'mice'                        ) == u'mouse'
assert sg      (u'pussies'                     ) == u'pussy'
assert sg      (u'cheeses'                     ) == u'cheese'

assert u(date(0                               )) == u'1970-01-01 01:00:00'
assert u(date(2000, 12, 31                    )) == u'2000-12-31 00:00:00'
assert u(date(2000, 12, 31) - 60 * 60 * 24     ) == u'2000-12-30 00:00:00'
assert   date(2000, 12, 31) .format('%Y-%m-%d' ) == u'2000-12-31'
assert u(date('Dec 31 2000', format='%b %d %Y')) == u'2000-12-31 00:00:00'

assert when('Mon Dec 31 2000'                  ) == [u'Mon Dec 31 2000']
assert when('Monday December 31, 2000.'        ) == [u'Monday December 31', u'2000']
assert when('Monday, December 31st 2000'       ) == [u'Monday', u'December 31st 2000']
assert when('Monday 31st of December, 2000'    ) == [u'Monday 31st of December', u'2000']
assert when('2000/12/31'                       ) == [u'2000/12/31']
assert when('23:59 p.m.'                       ) == [u'23:59 p.m.']
assert when('23:59'                            ) == [u'23:59']
assert when('12pm'                             ) == [u'12pm']
assert when('2 weeks ago'                      ) == [u'2 weeks ago']
assert when('5th century'                      ) == [u'5th century']
assert when('100 years'                        ) == [u'100 years']
assert when('1950-2000'                        ) == [u'1950-2000']
assert when('2101 AD'                          ) == [u'2101 AD']
assert when('day one'                          ) == [u'day one']
assert when('the day after tomorrow'           ) == [u'the day after tomorrow']
assert when('the first day of March'           ) == [u'the first day of March']

t = trie({'abc*': 1, 'xyz': 1})

assert len(list(t.search('abcd', etc='*'     ))) == 1
assert len(list(t.search('xyz'               ))) == 1
assert len(list(t.search('xyzz', sep=None    ))) == 1
assert len(list(t.search('xyzz'              ))) == 0
