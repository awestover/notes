/*
Go to
 chrome://extensions/
and upload this folder
*/

console.log("test test");

let ps = document.getElementsByTagName('p');


/*
for(elt of ps)
{
  elt.style['background-color']='#FF00FF';
}
*/

var img = new Image();
var div = document.getElementsByTagName('body')[0];

img.onload = function() {
  div.appendChild(img);
};

// img.src = 'https://wallpaperbrowse.com/media/images/cat-1285634_960_720.png';
img.src=chrome.extension.getURL("data/shark.png")



//
