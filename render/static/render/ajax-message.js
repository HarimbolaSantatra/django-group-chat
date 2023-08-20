function loadMessage(roomName){
	var xhr = new XMLHttpRequest();
	xhr.open('GET', `http://${window.location.host}/chat/load/${roomName}`, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.responseType = 'json';
	xhr.send();
	xhr.onload = function(){
		if(xhr.status === 200) {
			addResponseToUI(xhr.response);
		}
	}
}

const loadingBtn = document.querySelector('#load-more-btn');

loadingBtn.addEventListener('click', () => {
	const room_name = document.querySelector("#chat-message-room").value;
	loadMessage(room_name);
})

// On document ready, make first AJAX request to load the first page
document.addEventListener("DOMContentLoaded", function() {
	const room_name = document.querySelector("#chat-message-room").value;
	loadMessage(room_name);
});
