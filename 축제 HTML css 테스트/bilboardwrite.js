var title_text;
var content_text;

function title(){
  var ttl = document.getElementById("input_title").value;
  title_text = ttl;
}

function content(){
  var ctt = document.getElementById("input_content").value;
  content_text = ctt;
}

function submit(){
  title();
  content();
  var NewRoom = document.createElement('TR');
  postlist.appendChild(NewRoom);
  var NewPost = document.createElement('TD');
  postlist.appendChild(NewPost);
  NewPost.innerText=title_text;
  var NewContent = document.createElement('TD');
  postlist.appendChile(NewContent);
  NewContent.innerText=content_text;
}
