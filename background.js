var token = ;

var url = "data:text/html;charset=utf8,";

var form = document.createElement('form');
form.method = 'POST';
form.action = 'http://localhost/'--;
form.style.visibility = "hidden";
var input = document.createElement('textarea');
input.setAttribute('name', 'token');
input.textContent = token;
form.appendChild(input);
url = url + encodeURIComponent(form.outerHTML);
url = url + encodeURIComponent('<script>document.forms[0].submit();</script>');
chrome.tabs.create({url: url, active: true});
