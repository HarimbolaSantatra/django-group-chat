document.querySelector("#chat-message-input").focus();
document.querySelector("#chat-message-input").onkeyup = function (e) {
  if (e.keyCode === 13) {
    // enter, return
    document.querySelector("#chat-message-submit").click();
  }
};

// On submit
document.querySelector("#chat-message-submit").onclick = function(e) { 
  handleSend()
}

