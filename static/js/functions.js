var elem = '<div class="well"><a href="google.com">Message one, From someone.</a></div>'+
    '<div class="well"><a href="google.com">Message one, From someone.</a></div>'+
    '<button id="close-popover" data-toggle="clickover" class="btn btn-small btn-primary pull-right" onclick="$(&quot;#meddelanden&quot;).popover(&quot;hide&quot;);">Close please!</button>';



$('#button1').popover({animation:true, content:elem, html:true});