var get = document.getElementById("get");
var set = document.querySelector("#nn");
var out = document.getElementById("output");
var files = new FormData();
var filename;
var loadFile = function (event) {
get.src = URL.createObjectURL(event.target.files[0]);
filename = event.target.files[0];
files.append('file', filename, filename["name"]);
out.innerText="";
}
set.addEventListener("click", function() {
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function () {
if (this.readyState == 4 && this.status == 200) {
if(this.responseText==='"Covid"\n'){
out.style.color="red";
}
if(this.responseText==='"Normal"\n'){
out.style.color="green";
}
out.innerText = this.responseText;
files.delete('file');
}
}
xhr.open('POST', 'http://127.0.0.1:5000/', true);
xhr.onload = function () {
if (xhr.status === 200) {
alert('File successfully uploaded');
} else {
alert('File upload failed!');
}
};
xhr.send(files);
}
, false
)
