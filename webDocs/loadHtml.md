
This is kind of a hack:
$("#header").load('header.html', function() {
  $("#home-tab").addClass("active");
});
It lets you load an html file
into MULTIPLE html files
this is incredibly useful in the case of, say, a multi-page website with the same header (modulo active element) in each site

