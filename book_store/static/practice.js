var xhr = new XMLHttpRequest();
xhr.open("POST", "{% url 'save_comment' %}", true);

const commentBtn = document.querySelector("#commentFrm");
const commentList = document.querySelector("#comment-list");
const total = document.querySelector("h4 > span");
const list = [];

function Comment(content) {
  this.userid = "사용자";
  this.content = content;
  this.date = new Date().toLocaleDateString();
}

function createRow(userid, content, date) {
  const ul = document.createElement("ul");
  const li1 = document.createElement("li");
  const li2 = document.createElement("li");
  const li3 = document.createElement("li");

  ul.append(li1);
  ul.append(li2);
  ul.append(li3);

  ul.setAttribute("class", "comment-row");
  li1.setAttribute("class", "comment-id");
  li2.setAttribute("class", "comment-content");
  li3.setAttribute("class", "comment-date");

  li1.innerHTML = userid;
  li2.innerHTML = content;
  li3.innerHTML = date;

  return ul;
}

function drawing() {
  commentList.innerHTML = "";
  for (let i = list.length - 1; i >= 0; i--) {
    const row = createRow(list[i].userid, list[i].content, list[i].date);
    commentList.append(row);
  }
}

function totalRecord() {
  total.innerHTML = `(${list.length})`;
}
function commentBtnHandler(e) {
  e.preventDefault();
  const input = e.target.content;
  if (input.value === "") {
    alert("내용을 넣고 등록 버튼을 눌러주세요.");
    return;
  }
  const commentObj = new Comment(input.value);
  list.push(commentObj);
  totalRecord();

  // AJAX를 사용하여 서버에 댓글을 저장하는 부분 추가
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "{% url 'save_comment' %}", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      console.log("댓글이 성공적으로 저장되었습니다.");
    }
  };
  xhr.send(JSON.stringify(commentObj));

  drawing();
  e.target.reset();
}

totalRecord();
commentBtn.addEventListener("submit", commentBtnHandler);