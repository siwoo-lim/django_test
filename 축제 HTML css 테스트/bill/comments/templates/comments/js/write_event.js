var content_text;

function content(){
  var ctt = document.getElementById("input_comments").value;
  content_text = ctt;
}

var spawn = require('child_process').spawn,
    py = spawn('python', ['djangocomment.py']);

function submit(){
  data_from_django = {{ my_data }};
  widget.init(data_from_django);
  content();
  //var NewRoom = document.createElement('TR');
  //postlist.appendChild(NewRoom);
  //var NewPost = document.createElement('TD');
  //postlist.appendChild(NewPost);
  //NewPost.innerText=title_text;
  //var NewContent = document.createElement('TD');
  //postlist.appendChile(NewContent);
  //NewContent.innerText=content_text;
}
