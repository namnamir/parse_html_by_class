# Parse HTML files by classes

It is a simple Python script which parses HTML content based on the classes of the HTML tags.

For example: use this code to get all in-line ASCII arts from http://1lineart.kulaone.com/


```     
        <span class="artTitle ng-binding">superDonger</span><br>
        <span class="artWork ng-binding">─=≡Σ((( つ◕ل͜◕)つ</span><br>
        <span class="artCategory ng-binding">superdonger, face, fun</span>
```

then you just simple need to say that you are looking for class *artWork ng-binding* in *span* tag by loading the file and the following script.

```     
        input_soup = BeautifulSoup (inputf.read())
        ASCII  = input_soup.findAll("span", {"class":"artWork ng-binding"})
        print str(ASCII[i].contents[0])
```
