const createVmButton = document.getElementById('create-btn');
const startVmButton = document.getElementById('start-btn');
const stopVmButton = document.getElementById('stop-btn');
const snapshotVmButton = document.getElementById('snapshot-btn');


async function postData(url = "") {
    const response = await fetch(url, {
      method: "POST",
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

function addLog(text) {
    const elem = document.createElement("p");
    elem.innerText = text;
    document.querySelector("#logs-b").appendChild(elem);
}


createVmButton.addEventListener('click', function(e) {
  console.log('createVmButton was clicked');
  postData(url='http://127.0.0.1:5000/createVm');

  const text = "Vm has been created";
  addLog(text);
  
});



startVmButton.addEventListener('click', function(e) {
    console.log('startVmButton was clicked');
    postData(url='http://localhost:3000/startVm')

    const text = "Vm has been started";
    addLog(text);
  });


stopVmButton.addEventListener('click', function(e) {
    console.log('stopVmButton was clicked');
    postData(url='http://localhost:3000/stopVm')
    
    const text = "Vm has been stopped";
    addLog(text);
  });


snapshotVmButton.addEventListener('click', function(e) {
    console.log('snapshotVmButton was clicked');
    postData(url='http://localhost:3000/snapshotVm')
    
    const text = "Vm has been snapshotted";
    addLog(text);
  });